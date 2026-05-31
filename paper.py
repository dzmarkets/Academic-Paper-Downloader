import urllib.request
import urllib.parse
import json
import re
import os
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import threading

# Define target paper metadata
DOI = "10.1145/3375633"
TITLE = "Certifying compilation with de Bruijn indices"  # Used if DOI fails or for ResearchGate search
abort_requested = False
discovered_urls = []

# Configuration
UNPAYWALL_EMAIL = "researcher@domain.com"
SCIHUB_DOMAINS = [
    "https://sci-hub.se",
    "https://sci-hub.st",
    "https://sci-hub.ru",
    "https://sci-hub.africa",
    "https://sci-net.xyz"
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5'
}

# Set up a cookie processor to maintain sessions across redirects (crucial for ResearchGate)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
opener.addheaders = [(k, v) for k, v in HEADERS.items()]
urllib.request.install_opener(opener)


def get_user_country():
    """Detect the user's country via IP geolocation (ipapi.co). Returns ISO 3166-1 alpha-2 code."""
    try:
        req = urllib.request.Request('https://ipapi.co/json/', headers=HEADERS)
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = json.loads(resp.read().decode())
        return data.get('country_code', '').upper()
    except Exception:
        pass
    # Fallback: ip-api.com
    try:
        req = urllib.request.Request('http://ip-api.com/json/?fields=countryCode', headers=HEADERS)
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = json.loads(resp.read().decode())
        return data.get('countryCode', '').upper()
    except Exception:
        return ''


def clean_filename(title_str):
    """Clean the title so operating systems allow it as a valid filename."""
    return re.sub(r'[\\/*?:"<>|]', "", title_str)


def register_discovered_url(url, label):
    """Register a URL discovered during the pipeline for fallback web browser launching."""
    global discovered_urls
    if not url:
        return
    # Avoid duplicate URLs
    if url not in [item[0] for item in discovered_urls]:
        is_pdf = any(ext in url.lower() for ext in [".pdf", "pdf?", "/pdf/", "/download", "file/"])
        rank = 1 if is_pdf else 2
        discovered_urls.append((url, rank, label))


def resolve_rg_pdf_url(rg_pub_url):
    """Fetch a ResearchGate publication page and extract its direct PDF/download link."""
    print(f"[INFO] Resolving direct PDF for ResearchGate publication: {rg_pub_url}")
    try:
        # fetch_html_resilient handles the curl fallback automatically if blocked by 403 Forbidden!
        page_source = fetch_html_resilient(rg_pub_url)
        if not page_source:
            return rg_pub_url
            
        # Use our robust regexes to find the download link
        download_matches = re.findall(r'href="([^"]*?publication/\d+_[^"]+/link/[a-f0-9]+/download)"', page_source)
        download_matches += re.findall(r'href="([^"]*?publication/\d+_[^"]+/file/[^"]+)"', page_source)
        download_matches = list(set(download_matches))
        
        if download_matches:
            link = download_matches[0].strip()
            if link.startswith('http'):
                target_url = link
            else:
                parsed_base = urllib.parse.urlparse(rg_pub_url)
                base_domain = f"{parsed_base.scheme}://{parsed_base.netloc}"
                if link.startswith('/'):
                    target_url = base_domain + link
                else:
                    target_url = base_domain + '/' + link
            print(f"[INFO] Resolved direct PDF download URL: {target_url}")
            return target_url
            
    except Exception as e:
        print(f"[WARNING] Failed to resolve direct ResearchGate PDF: {e}")
        
    return rg_pub_url


def view_document_in_browser(doi, paper_title, is_book=False):
    """Resolve the paper and open it in the default web browser for viewing."""
    def open_thread():
        url = None
        if doi:
            ident = doi.strip()
            if ident.startswith("http://") or ident.startswith("https://"):
                if "researchgate.net/publication/" in doi:
                    url = resolve_rg_pdf_url(doi)
                else:
                    url = doi
            elif ":" in ident:
                prefix, key = ident.split(":", 1)
                prefix = prefix.strip().lower()
                key = key.strip()
                if prefix == "ia":
                    url = f"https://archive.org/details/{key}"
                elif prefix == "isbn":
                    url = f"https://openlibrary.org/isbn/{key}"
                elif prefix == "ol":
                    clean_key = key.lstrip('/')
                    if not clean_key.startswith("works/") and not clean_key.startswith("books/") and not clean_key.startswith("authors/"):
                        clean_key = f"works/{clean_key}"
                    url = f"https://openlibrary.org/{clean_key}"
                else:
                    if is_book:
                        url = f"https://openlibrary.org/search?q={urllib.parse.quote(paper_title)}"
                    else:
                        url = f"https://doi.org/{doi}"
            else:
                if is_book:
                    url = f"https://openlibrary.org/search?q={urllib.parse.quote(paper_title)}"
                else:
                    url = f"https://doi.org/{doi}"
        else:
            # Fallback to search query
            if is_book:
                url = f"https://openlibrary.org/search?q={urllib.parse.quote(paper_title)}"
            else:
                url = f"https://www.google.com/search?q={urllib.parse.quote(paper_title)}"
            
        print(f"\n[INFO] Opening document for viewing in browser: {url}")
        try:
            import webbrowser
            webbrowser.open(url)
        except Exception as e:
            print(f"[ERROR] Failed to open document in browser: {e}")
            
    t = threading.Thread(target=open_thread)
    t.daemon = True
    t.start()


def download_file(url, filename, referer=None, cookie=None):
    """Helper to perform standard binary file downloads with PDF validation."""
    global abort_requested
    if abort_requested:
        print("[INFO] Download aborted by user.")
        return False

    # Ensure all downloads route to a dedicated Downloads folder rather than the root
    downloads_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Downloads")
    if not os.path.isabs(filename):
        filename = os.path.join(downloads_dir, filename)
        
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
    except Exception as e:
        print(f"[WARNING] Failed to create parent directory: {e}. Falling back to local root.")
        filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.basename(filename))

    content = None
    try:
        headers = HEADERS.copy()
        if referer:
            headers['Referer'] = referer
        if cookie:
            headers['Cookie'] = cookie
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=25) as response:
            if abort_requested:
                print("[INFO] Download aborted by user.")
                return False
            content = response.read()
    except Exception as e:
        print(f"[WARNING] urllib download failed: {e}. Trying system curl fallback...")
        content = None

    # Fallback to system curl command if urllib failed (or did not return a valid PDF and we expect a PDF)
    is_pdf = filename.lower().endswith('.pdf')
    needs_curl = not content or (is_pdf and not content.startswith(b'%PDF'))
    if needs_curl:
        try:
            import subprocess
            print(f"[INFO] Bypassing via native system curl...")
            cmd = ["curl", "-s", "-L", "-H", f"User-Agent: {HEADERS['User-Agent']}", "-H", f"Accept: {HEADERS['Accept']}"]
            if referer:
                cmd += ["-H", f"Referer: {referer}"]
            if cookie:
                cmd += ["-H", f"Cookie: {cookie}"]
            cmd += ["-o", filename, url]
            res = subprocess.run(cmd, capture_output=True)
            if res.returncode == 0 and os.path.exists(filename):
                with open(filename, "rb") as f:
                    content = f.read()
        except Exception as curl_err:
            print(f"[ERROR] Native curl fallback failed: {curl_err}")
            return False

    # Validate PDF magic bytes if we expect a PDF
    if is_pdf:
        if not content or not content.startswith(b'%PDF'):
            print(f"[WARNING] Downloaded content from {url} is not a valid PDF! (Size: {len(content) if content else 0} bytes)")
            if content and (b'<html' in content.lower() or b'<!doctype' in content.lower()):
                print("[TIP] The server served an HTML page/blocker instead of the raw PDF.")
            if os.path.exists(filename):
                try:
                    os.remove(filename)
                except:
                    pass
            return False
        
    # Ensure content is saved to disk
    with open(filename, "wb") as out_file:
        out_file.write(content)
    print(f"[SUCCESS] Saved flawlessly inside Downloads folder: '{os.path.basename(filename)}'")
    print(f"[INFO] Absolute Location: {filename}")
    return True


def resolve_title_to_doi(title):
    """Query Crossref API to resolve a title to a DOI."""
    if not title:
        return None
    print(f"\n--- [RESOLVING] Searching Crossref for DOI of '{title}' ---")
    url = f"https://api.crossref.org/works?query={urllib.parse.quote(title)}&rows=1"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            
        items = data.get('message', {}).get('items', [])
        if items:
            best_match = items[0]
            resolved_doi = best_match.get('DOI')
            resolved_title = best_match.get('title', [title])[0]
            print(f"[INFO] Closest match on Crossref: '{resolved_title}'")
            print(f"[INFO] Resolved DOI: {resolved_doi}")
            return resolved_doi
    except Exception as e:
        print(f"[WARNING] Crossref resolution failed: {e}")
    return None


def search_crossref(query, offset=0, rows=5, type_filter="All", author=""):
    """Query Crossref API for title+author keywords, return paginated list with OA check."""
    if not query:
        return []
    # Strip surrounding quotes, brackets or extra whitespace the user may type
    clean_query = query.strip().strip('"').strip("'").strip('[').strip(']').strip()
    clean_author = author.strip().strip('"').strip("'") if author else ""
    # Retrieve more rows to ensure we have enough valid ones after filtering
    crossref_rows = 30 + offset
    # Build URL: use query.title when title given, query.author when author given
    url = "https://api.crossref.org/works?"
    if clean_query and clean_author:
        url += f"query={urllib.parse.quote(clean_query)}&query.author={urllib.parse.quote(clean_author)}"
    elif clean_query:
        url += f"query={urllib.parse.quote(clean_query)}"
    elif clean_author:
        url += f"query.author={urllib.parse.quote(clean_author)}"
    else:
        return []
    url += f"&rows={crossref_rows}&offset=0"
    if type_filter == "Papers":
        url += "&filter=type:journal-article"
    elif type_filter == "Books":
        url += "&filter=type:book"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
        
        items = data.get('message', {}).get('items', [])
        filtered_items = []
        for item in items:
            doi = item.get('DOI', '')
            if not doi:
                continue
                
            # Check authors - strictly exclude if empty or missing
            authors_list = item.get('author', [])
            if not authors_list:
                continue
                
            authors = []
            for a in authors_list:
                family = a.get('family', '')
                given = a.get('given', '')
                if family:
                    authors.append(f"{given} {family}".strip())
            if not authors:
                continue
            authors_str = ", ".join(authors)
            
            title = item.get('title', ['No Title'])[0]
            
            # Journal/publisher name
            journal = "Unknown Publisher"
            container_title = item.get('container-title')
            publisher = item.get('publisher', '')
            if container_title and len(container_title) > 0 and container_title[0]:
                journal = container_title[0]
            elif publisher:
                journal = publisher
                
            # Format year
            year = "n.d."
            published = item.get('published-print') or item.get('published-online') or item.get('created')
            if published:
                date_parts = published.get('date-parts', [[]])[0]
                if date_parts:
                    year = str(date_parts[0])
                    
            filtered_items.append({
                'title': title,
                'doi': doi,
                'authors': authors_str,
                'year': year,
                'journal': journal,
                'is_oa': False
            })
            
        # Page the filtered items
        page_items = filtered_items[offset : offset + rows]
        
        for idx, item in enumerate(page_items):
            item['original_index'] = idx
            
        import concurrent.futures
        
        def check_oa(res_item):
            item_doi = res_item['doi']
            up_url = f"https://api.unpaywall.org/v2/{item_doi}?email={UNPAYWALL_EMAIL}"
            try:
                up_req = urllib.request.Request(up_url, headers=HEADERS)
                with urllib.request.urlopen(up_req, timeout=3) as up_res:
                     up_data = json.loads(up_res.read().decode())
                     if up_data.get('is_oa') or up_data.get('best_oa_location'):
                         res_item['is_oa'] = True
            except Exception:
                pass
            return res_item
            
        final_page_items = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(check_oa, pi) for pi in page_items]
            for fut in concurrent.futures.as_completed(futures):
                try:
                    final_page_items.append(fut.result())
                except Exception:
                    pass
                    
        final_page_items.sort(key=lambda x: x.get('original_index', 99))
        return final_page_items
    except Exception as e:
        print(f"[ERROR] Crossref search failed: {e}")
        return []


def search_openlibrary(query, author="", offset=0, rows=5):
    """Query OpenLibrary API for books — much more accurate than Crossref for book searches."""
    if not query:
        return []
    clean_query = query.strip().strip('"').strip("'").strip('[').strip(']').strip()
    clean_author = author.strip().strip('"').strip("'") if author else ""
    
    params = f"title={urllib.parse.quote(clean_query)}"
    if clean_author:
        params += f"&author={urllib.parse.quote(clean_author)}"
    params += "&fields=title,author_name,first_publish_year,isbn,publisher,key,ia&limit=50"
    url = f"https://openlibrary.org/search.json?{params}"
    
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=12) as response:
            data = json.loads(response.read().decode())
        
        docs = data.get('docs', [])
        filtered = []
        for doc in docs:
            title = doc.get('title', '')
            if not title:
                continue
            author_names = doc.get('author_name', [])
            if not author_names:
                continue
            authors_str = ", ".join(author_names[:4])  # cap at 4 authors
            year = str(doc.get('first_publish_year', 'n.d.'))
            publishers = doc.get('publisher', [])
            publisher_str = publishers[0] if publishers else "OpenLibrary"
            
            # Retrieve identifiers to build a pseudo-DOI for the pipeline
            ol_key = doc.get('key', '')  # e.g. /works/OL12345W
            isbns = doc.get('isbn', [])
            ia_ids = doc.get('ia', [])
            
            doi = ""
            if ia_ids:
                doi = f"ia:{ia_ids[0]}"
            elif isbns:
                doi = f"isbn:{isbns[0]}"
            elif ol_key:
                doi = f"ol:{ol_key.replace('/works/', '')}"
                
            filtered.append({
                'title': title,
                'doi': doi,
                'ol_key': ol_key,
                'authors': authors_str,
                'year': year,
                'journal': publisher_str,
                'is_oa': True,  # OpenLibrary books are typically openly accessible
                'source': 'openlibrary'
            })
        
        page_items = filtered[offset: offset + rows]
        for idx, item in enumerate(page_items):
            item['original_index'] = idx
        return page_items
    except Exception as e:
        print(f"[ERROR] OpenLibrary search failed: {e}")
        return []


def search_openalex_by_author(author_name, offset=0, rows=5, type_filter="All"):
    """Search OpenAlex for works by author name.
    
    OpenAlex first resolves the name to an author entity, then fetches their
    full publication list — giving accurate results for authors not well-indexed
    by Crossref (e.g. French/Algerian researchers, non-English publications).
    Falls back to Crossref query.author if OpenAlex finds nothing.
    """
    if not author_name:
        return []
    clean_name = author_name.strip().strip('"').strip("'")
    
    # OpenAlex requires a polite mailto in the User-Agent for best rate limits
    oa_headers = {**HEADERS, 'User-Agent': f'PaperDownloader/2.1 (mailto:{UNPAYWALL_EMAIL})'}
    
    # Step 1: Resolve author name → OpenAlex author ID
    author_id = None
    try:
        author_url = f"https://api.openalex.org/authors?search={urllib.parse.quote(clean_name)}&per_page=5"
        req = urllib.request.Request(author_url, headers=oa_headers)
        with urllib.request.urlopen(req, timeout=12) as resp:
            adata = json.loads(resp.read().decode())
        authors_found = adata.get('results', [])
        if authors_found:
            author_id = authors_found[0].get('id', '')  # e.g. https://openalex.org/A123456
            print(f"[INFO] OpenAlex author resolved: {authors_found[0].get('display_name')} → {author_id}")
    except Exception as e:
        print(f"[WARNING] OpenAlex author lookup failed: {e}")
    
    results = []
    
    # Step 2a: Fetch works by resolved author ID (most accurate)
    if author_id:
        try:
            filter_parts = [f"authorships.author.id:{author_id}"]
            if type_filter == "Papers":
                filter_parts.append("type:journal-article")
            elif type_filter == "Books":
                filter_parts.append("type:book")
            filter_str = ",".join(filter_parts)
            
            works_url = (f"https://api.openalex.org/works"
                         f"?filter={urllib.parse.quote(filter_str)}"
                         f"&per_page=50&sort=publication_year:desc")
            req = urllib.request.Request(works_url, headers=oa_headers)
            with urllib.request.urlopen(req, timeout=12) as resp:
                wdata = json.loads(resp.read().decode())
            works = wdata.get('results', [])
            
            for work in works:
                title = work.get('title', '')
                if not title:
                    continue
                doi = work.get('doi', '') or ''
                if doi.startswith('https://doi.org/'):
                    doi = doi[len('https://doi.org/'):]
                authorships = work.get('authorships', [])
                auth_names = [a.get('author', {}).get('display_name', '')
                              for a in authorships if a.get('author', {}).get('display_name')]
                if not auth_names:
                    continue
                year = str(work.get('publication_year', 'n.d.'))
                primary_loc = work.get('primary_location') or {}
                source = primary_loc.get('source') or {}
                journal = source.get('display_name', 'Unknown Journal')
                is_oa = (work.get('open_access') or {}).get('is_oa', False)
                results.append({
                    'title': title,
                    'doi': doi,
                    'authors': ', '.join(auth_names[:4]),
                    'year': year,
                    'journal': journal,
                    'is_oa': is_oa,
                    'source': 'openalex'
                })
        except Exception as e:
            print(f"[WARNING] OpenAlex works fetch failed: {e}")
    
    # Step 2b: Fallback — Crossref query.author if OpenAlex returned nothing
    if not results:
        print(f"[INFO] OpenAlex returned no results, falling back to Crossref author search...")
        results = search_crossref("", offset=0, rows=50, type_filter=type_filter, author=clean_name)
    
    if not results:
        return []
    
    page_items = results[offset: offset + rows]
    for idx, item in enumerate(page_items):
        item['original_index'] = idx
    return page_items


def fetch_html_resilient(url):
    """Fetch HTML content from a URL using urllib first, falling back to native system curl on block/failure."""
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=12) as response:
            return response.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"[WARNING] urllib fetch failed: {e}. Trying native system curl fallback...")
        try:
            import subprocess
            cmd = ["curl", "-s", "-L", "-H", f"User-Agent: {HEADERS['User-Agent']}", "-H", f"Accept: {HEADERS['Accept']}", url]
            res = subprocess.run(cmd, capture_output=True)
            if res.returncode == 0:
                return res.stdout.decode('utf-8', errors='ignore')
            else:
                print(f"[WARNING] curl returned error code: {res.returncode}")
        except Exception as curl_err:
            print(f"[ERROR] Native curl fallback failed: {curl_err}")
    return ""


def resolve_researchgate_profile(author_name):
    """Resolve an author's ResearchGate profile URL using Yahoo and DuckDuckGo search engines."""
    if not author_name:
        return None
    clean_name = author_name.strip().strip('"').strip("'")
    
    # Method 1: Yahoo Search (extremely reliable, bypassed captcha walls)
    print(f"[INFO] Resolving ResearchGate profile for '{clean_name}' via Yahoo...")
    try:
        search_query = f'"{clean_name}" site:researchgate.net/profile/'
        yahoo_url = f"https://search.yahoo.com/search?p={urllib.parse.quote(search_query)}"
        html = fetch_html_resilient(yahoo_url)
        if html:
            ru_links = re.findall(r'RU=([^/&"]+)', html)
            for val in ru_links:
                unquoted = urllib.parse.unquote(val)
                if "researchgate.net/profile/" in unquoted:
                    profile_url = unquoted.split('/RK=')[0]
                    profile_match = re.match(r'(https?://(?:www\.)?researchgate\.net/profile/[^/]+)', profile_url)
                    if profile_match:
                        resolved = profile_match.group(1)
                        print(f"[INFO] Yahoo resolved profile: {resolved}")
                        return resolved
    except Exception as e:
        print(f"[WARNING] Yahoo profile resolution failed: {e}")
        
    # Method 2: DuckDuckGo Search (original fallback)
    print(f"[INFO] Resolving ResearchGate profile for '{clean_name}' via DuckDuckGo...")
    try:
        search_query = f'"{clean_name}" site:researchgate.net/profile/'
        ddg_url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(search_query)}"
        html = fetch_html_resilient(ddg_url)
        if html:
            encoded_links = re.findall(r'uddg=(https?%3A%2F%2F[^&"]*researchgate\.net%2Fprofile%2F[^&"]*)', html)
            if encoded_links:
                resolved = urllib.parse.unquote(encoded_links[0])
                print(f"[INFO] DuckDuckGo resolved profile: {resolved}")
                return resolved
                
            links = re.findall(r'href="([^"]*researchgate\.net/profile/[^"]*)"', html)
            if links:
                resolved = urllib.parse.unquote(links[0]).split("&")[0]
                print(f"[INFO] DuckDuckGo resolved profile (direct): {resolved}")
                return resolved
    except Exception as e:
        print(f"[WARNING] DuckDuckGo profile resolution failed: {e}")
        
    return None


def search_researchgate_by_author(author_name, offset=0, rows=5, type_filter="All"):
    """Query Resolved ResearchGate profile to extract publication entries for an author search."""
    profile_url = resolve_researchgate_profile(author_name)
    if not profile_url:
        print("[WARNING] ResearchGate profile resolution found nothing.")
        return []
        
    try:
        print(f"[INFO] Fetching ResearchGate profile: {profile_url}")
        page_html = fetch_html_resilient(profile_url)
        if not page_html:
            raise Exception("Resilient fetch returned empty content")
            
        parts = page_html.split('gtm-research-item')
        results = []
        
        for part in parts[1:]:
            # 1. Parse Title and Link
            link_match = re.search(r'href="([^"]*researchgate\.net/publication/[^"]*)"[^>]*>(.*?)</a>', part)
            if not link_match:
                link_match = re.search(r'href="(/publication/[^"]+)"[^>]*>(.*?)</a>', part)
                
            if not link_match:
                continue
                
            pub_url = link_match.group(1)
            if pub_url.startswith('/'):
                pub_url = "https://www.researchgate.net" + pub_url
            title = re.sub('<[^<]+?>', '', link_match.group(2)).strip()
            
            # 2. Parse Type
            type_match = re.search(r'class="[^"]*nova-legacy-v-entity-item__badge[^"]*"[^>]*>(.*?)</span>', part)
            pub_type = type_match.group(1).strip() if type_match else ""
            
            # Filter type if needed
            if type_filter == "Papers" and pub_type.lower() in ("book", "presentation", "poster"):
                continue
            if type_filter == "Books" and pub_type.lower() != "book":
                continue
                
            # 3. Parse Date/Year
            date_match = re.search(r'class="[^"]*nova-legacy-v-entity-item__meta-data-item[^"]*"[^>]*>\s*<span[^>]*>(.*?)</span>', part)
            if not date_match:
                date_match = re.search(r'<span[^>]*>\s*([A-Za-z]{3}\s+\d{4}|\d{4})\s*</span>', part)
                
            pub_date = date_match.group(1).strip() if date_match else "n.d."
            year = "n.d."
            year_match = re.search(r'\b(19\d{2}|20\d{2})\b', pub_date)
            if year_match:
                year = year_match.group(1)
                
            # Check for Full-text available
            is_oa = "Full-text available" in part or "Download" in part
            
            results.append({
                'title': title,
                'doi': pub_url,  # Pass direct ResearchGate publication link as 'doi'
                'authors': author_name,
                'year': year,
                'journal': f"ResearchGate ({pub_type})" if pub_type else "ResearchGate",
                'is_oa': is_oa,
                'source': 'researchgate'
            })
            
        print(f"[SUCCESS] Retrieved {len(results)} publications from ResearchGate profile.")
        return results
    except Exception as e:
        print(f"[WARNING] ResearchGate profile scraping failed: {e}")
        return []


def try_unpaywall(doi):
    """Strategy 1: Legal Open Access check via Unpaywall."""
    if not doi:
        print("\n--- [STRATEGY 1] Skipped (No DOI available) ---")
        return False
    if doi.startswith("http://") or doi.startswith("https://"):
        return False
    print("\n--- [STRATEGY 1] Querying Unpaywall Database ---")
    url = f"https://api.unpaywall.org/v2/{doi}?email={UNPAYWALL_EMAIL}"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            
        pdf_url = data.get('best_oa_location', {}).get('url_for_pdf')
        title = data.get('title', 'downloaded_paper')
        
        if pdf_url:
            print(f"[INFO] PDF Found via Unpaywall: {pdf_url}")
            register_discovered_url(pdf_url, "Unpaywall Open Access PDF")
            filename = f"{clean_filename(title)}.pdf"
            return download_file(pdf_url, filename)
        else:
            print("[INFO] Paper is legally paywalled on Unpaywall.")
    except Exception as e:
        print(f"[WARNING] Unpaywall lookup failed: {e}")
    return False


def try_scihub(doi):
    """Strategy 2: Repository scrape via Sci-Hub Mirrors."""
    if not doi:
        print("\n--- [STRATEGY 2] Skipped (No DOI available) ---")
        return False
    if doi.startswith("http://") or doi.startswith("https://"):
        return False
        
    print("\n--- [STRATEGY 2] Querying Sci-Hub Shadow Library Mirrors ---")
    for domain in SCIHUB_DOMAINS:
        if abort_requested:
            print("[INFO] Sci-Hub strategy aborted.")
            return False
        print(f"[INFO] Trying Sci-Hub mirror: {domain}")
        url = f"{domain}/{doi}"
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as response:
                html = response.read().decode('utf-8', errors='ignore')
            
            # Pull potential PDF URLs from scripts/embeds
            pdf_paths = re.findall(r'[\'"]([^\'"]+\.pdf[^\'"]*)[\'"]', html)
            pdf_paths += re.findall(r'src=([^ >]+\.pdf[^ >]*)', html)
            pdf_paths += re.findall(r'href=([^ >]+\.pdf[^ >]*)', html)
    
            pdf_url = None
            for path in pdf_paths:
                path = path.replace('\\', '')
                if ".pdf" in path:
                    pdf_url = path
                    break
    
            if pdf_url:
                if pdf_url.startswith('//'):
                    pdf_url = 'https:' + pdf_url
                elif pdf_url.startswith('/'):
                    pdf_url = domain + pdf_url
                elif not pdf_url.startswith('http'):
                    pdf_url = f"{domain}/{pdf_url}"
                    
                print(f"[INFO] Found Sci-Hub PDF Target: {pdf_url}")
                register_discovered_url(pdf_url, f"Sci-Hub PDF ({domain})")
                filename = doi.replace("/", "_") + ".pdf"
                if download_file(pdf_url, filename):
                    return True
            else:
                print(f"[INFO] Sci-Hub layout on {domain} hid or didn't contain this file.")
        except Exception as e:
            print(f"[WARNING] Mirror {domain} failed: {e}")
            
    return False


def resolve_doi_via_handle_api(doi):
    """Query handle API to get the resolved URL of a DOI."""
    if not doi:
        return None
    print(f"[INFO] Resolving DOI {doi} via hdl.handle.net API...")
    url = f"https://hdl.handle.net/api/handles/{doi}"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            
        values = data.get('values', [])
        for value in values:
            if value.get('type') == 'URL':
                resolved_url = value.get('data', {}).get('value')
                if resolved_url:
                    print(f"[INFO] Handle API resolved DOI to: {resolved_url}")
                    register_discovered_url(resolved_url, "Publisher Resource Page (Handle API)")
                    return resolved_url
    except Exception as e:
        print(f"[WARNING] Handle API resolution failed: {e}")
    return None


def resolve_doi_to_url(doi):
    """Query Crossref API to find the primary resource URL of a DOI."""
    if not doi:
        return None
    print(f"[INFO] Resolving DOI {doi} via Crossref API...")
    url = f"https://api.crossref.org/works/{doi}"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
        
        resource_url = data.get('message', {}).get('resource', {}).get('primary', {}).get('URL')
        if resource_url:
            register_discovered_url(resource_url, "Publisher Resource Page")
            return resource_url
            
        # Fallback to look in 'link' array if primary resource URL is missing
        links = data.get('message', {}).get('link', [])
        for link in links:
            intended_url = link.get('URL')
            if intended_url:
                register_discovered_url(intended_url, "Publisher Resource Page")
                return intended_url
    except Exception as e:
        print(f"[WARNING] Crossref DOI resolution failed: {e}")
        
    # Backup: Query Handle REST API (never blocked by Cloudflare)
    return resolve_doi_via_handle_api(doi)


def get_jpeg_size(filepath):
    """Parse JPEG SOF0-SOF3 markers to extract width and height in pure Python."""
    try:
        with open(filepath, 'rb') as f:
            data = f.read(4096)  # Read first 4KB
            if len(data) < 4 or data[0:2] != b'\xFF\xD8':
                return 800, 1000  # Default fallback if not valid JPEG
            
            i = 2
            while i < len(data) - 8:
                if data[i] == 0xFF:
                    marker = data[i+1]
                    if marker == 0xD9:  # EOI
                        break
                    is_sof = (0xC0 <= marker <= 0xC3) or (0xC5 <= marker <= 0xCB) or (0xCD <= marker <= 0xCF)
                    if is_sof and marker != 0xC4:
                        # SOF block layout: sample precision, height, width
                        height = int.from_bytes(data[i+5:i+7], byteorder='big')
                        width = int.from_bytes(data[i+7:i+9], byteorder='big')
                        if width > 0 and height > 0:
                            return width, height
                        break
                    else:
                        block_len = int.from_bytes(data[i+2:i+4], byteorder='big')
                        i += 2 + block_len
                else:
                    i += 1
    except Exception:
        pass
    return 800, 1000  # Default fallback


def compile_jpegs_to_pdf(jpeg_paths, pdf_path):
    """Compile JPEG images into a single PDF file using pure Python."""
    print(f"[INFO] Stitching {len(jpeg_paths)} page images into a single PDF...")
    
    offsets = {}
    out = bytearray()
    
    def write_line(line_bytes):
        out.extend(line_bytes + b'\n')
        
    write_line(b"%PDF-1.4")
    write_line(b"%\xFF\xFF\xFF\xFF")  # Binary marker
    
    num_pages = len(jpeg_paths)
    
    # 1. Catalog
    offsets[1] = len(out)
    write_line(b"1 0 obj")
    write_line(b"<< /Type /Catalog /Pages 2 0 R >>")
    write_line(b"endobj")
    
    # 2. Pages Parent
    kids_refs = [f"{3*p + 3} 0 R" for p in range(num_pages)]
    kids_str = " ".join(kids_refs)
    
    offsets[2] = len(out)
    write_line(b"2 0 obj")
    write_line(b"<< /Type /Pages /Kids [" + kids_str.encode() + b"] /Count " + str(num_pages).encode() + b" >>")
    write_line(b"endobj")
    
    # Write Page, Content, and Image stream objects
    for p, jpeg_path in enumerate(jpeg_paths):
        page_obj_id = 3 * p + 3
        content_obj_id = 3 * p + 4
        image_obj_id = 3 * p + 5
        
        width, height = get_jpeg_size(jpeg_path)
        
        # A. Page Object
        offsets[page_obj_id] = len(out)
        write_line(f"{page_obj_id} 0 obj".encode())
        write_line(f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {width} {height}] /Contents {content_obj_id} 0 R /Resources << /XObject << /Im0 {image_obj_id} 0 R >> >> >>".encode())
        write_line(b"endobj")
        
        # B. Content Stream Object (drawing the XObject at full size)
        content_stream = f"q\n{width} 0 0 {height} 0 0 cm\n/Im0 Do\nQ\n".encode()
        offsets[content_obj_id] = len(out)
        write_line(f"{content_obj_id} 0 obj".encode())
        write_line(f"<< /Length {len(content_stream)} >>".encode())
        write_line(b"stream")
        write_line(content_stream)
        write_line(b"endstream")
        write_line(b"endobj")
        
        # C. Image Object
        try:
            with open(jpeg_path, 'rb') as img_f:
                img_data = img_f.read()
        except Exception as err:
            img_data = b""
            print(f"[WARNING] Failed to read {jpeg_path}: {err}")
            
        offsets[image_obj_id] = len(out)
        write_line(f"{image_obj_id} 0 obj".encode())
        write_line(f"<< /Type /XObject /Subtype /Image /Width {width} /Height {height} /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length {len(img_data)} >>".encode())
        write_line(b"stream")
        out.extend(img_data)
        out.extend(b'\n')
        write_line(b"endstream")
        write_line(b"endobj")
        
    # Write xref table
    xref_offset = len(out)
    write_line(b"xref")
    total_objects = 3 * num_pages + 3
    write_line(f"0 {total_objects}".encode())
    write_line(b"0000000000 65535 f ")
    
    for obj_id in range(1, total_objects):
        offset = offsets.get(obj_id, 0)
        write_line(f"{offset:010d} 00000 n ".encode())
        
    # Write trailer
    write_line(b"trailer")
    write_line(f"<< /Size {total_objects} /Root 1 0 R >>".encode())
    write_line(b"startxref")
    write_line(str(xref_offset).encode())
    write_line(b"%%EOF")
    
    # Save PDF
    with open(pdf_path, 'wb') as pdf_f:
        pdf_f.write(out)
    print(f"[SUCCESS] Compiled PDF saved inside Downloads: '{os.path.basename(pdf_path)}'")


def get_book_pages_count(ia_id):
    """Retrieve total page count from Internet Archive metadata API."""
    url = f"https://archive.org/metadata/{ia_id}"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
        meta = data.get('metadata', {})
        count = meta.get('imagecount') or meta.get('item_pages') or meta.get('pages')
        if count:
            return int(count)
    except Exception as e:
        print(f"[WARNING] Could not resolve page count via metadata: {e}")
    return 350  # Dynamic default fallback


def deobfuscate_image(image_data, link, obf_header):
    """Decrypts the first 1024 bytes of image_data using AES-CTR and pycryptodome."""
    try:
        from Crypto.Cipher import AES
        from Crypto.Util import Counter
        import hashlib
        import base64
        import re
        
        version, counter_b64 = obf_header.split('|')
        if version != '1':
            raise ValueError("Unsupported obfuscation version: " + version)
            
        # Derive AES key: replace protocol/host in link with '/'
        aesKey = re.sub(r"^https?:\/\/.*?\/", "/", link)
        sha1_digest = hashlib.sha1(aesKey.encode('utf-8')).digest()
        key = sha1_digest[:16]
        
        # Decode the counter (should be 16 bytes)
        counter_bytes = base64.b64decode(counter_b64)
        if len(counter_bytes) != 16:
            raise ValueError(f"Expected counter to be 16 bytes, got {len(counter_bytes)}")
            
        prefix = counter_bytes[:8]
        initial_value = int.from_bytes(counter_bytes[8:], byteorder='big')
        
        # Create AES-CTR cipher with a 64-bit counter length
        ctr = Counter.new(64, prefix=prefix, initial_value=initial_value, little_endian=False)
        cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
        
        decrypted_part = cipher.decrypt(image_data[:1024])
        return decrypted_part + image_data[1024:]
    except Exception as e:
        print(f"[WARNING] Deobfuscation error: {e}")
        return image_data


def try_download_ia_pages(ia_id, pdf_path, title, status_label=None, root_widget=None):
    """Interactively prompts for authentication cookie, calls grant_access to searchInside.php,
    fetches high-resolution page URIs from BookReaderJSIA.php, downloads concurrently,
    deobfuscates pages, and compiles them into a single PDF using pure Python."""
    global abort_requested
    
    print("\n--- [BOOK PAGE COMPILER STRATEGY] Querying page count and CDL status ---")
    
    # 1. Prompt for Cookie securely on the main thread
    cookie = None
    if root_widget:
        cookie_res = []
        evt = threading.Event()
        
        def prompt():
            try:
                import tkinter.simpledialog
                val = tkinter.simpledialog.askstring(
                    "Archive.org Authentication Required",
                    f"This book ('{title if title else ia_id}') is locked under Controlled Digital Lending.\n\n"
                    "To download it page-by-page as a compiled PDF, please:\n"
                    "1. Log in and Borrow this book in your web browser.\n"
                    "2. Open DevTools (F12) -> Network -> Copy any request's 'Cookie' header.\n"
                    "3. Paste your Archive.org Cookie below:\n\n"
                    "Leave blank or click Cancel to skip and fallback to browser viewing.",
                    parent=root_widget
                )
                cookie_res.append(val)
            except Exception as err:
                print(f"[WARNING] Main thread dialog failed: {err}")
            finally:
                evt.set()
                
        root_widget.after(0, prompt)
        evt.wait()
        cookie = cookie_res[0] if cookie_res else None
        
    if not cookie:
        print("[INFO] No cookie credentials provided. Skipping CDL image compilation.")
        return False
        
    # 2. Establish requests Session and populate cookies
    import requests
    import time
    session = requests.Session()
    # Parse cookie string and set in session
    for part in cookie.split(";"):
        part = part.strip()
        if not part:
            continue
        if "=" in part:
            c_name, c_val = part.split("=", 1)
            session.cookies.set(c_name, c_val, domain=".archive.org")
            
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    })
    
    # 3. Perform grant_access handshake against searchInside.php
    print("[INFO] Performing grant_access handshake against searchInside.php...")
    if status_label:
        status_label.config(text="Performing access handshake...", fg="#00ADB5")
    try:
        handshake_url = "https://archive.org/services/loans/loan/searchInside.php"
        data = {
            "action": "grant_access",
            "identifier": ia_id
        }
        resp = session.post(handshake_url, data=data, timeout=15)
        if resp.status_code == 200:
            print("[SUCCESS] grant_access handshake succeeded.")
        else:
            print(f"[WARNING] Handshake returned status {resp.status_code}.")
    except Exception as e:
        print(f"[WARNING] Handshake failed: {e}")
        
    # 4. Fetch the details page to locate the BookReaderJSIA.php URL
    print("[INFO] Resolving BookReaderJSIA metadata URL...")
    if status_label:
        status_label.config(text="Resolving book metadata...", fg="#00ADB5")
    jsia_url = None
    try:
        details_url = f"https://archive.org/details/{ia_id}"
        resp_details = session.get(details_url, timeout=20)
        html = resp_details.text
        if '"url":"' in html:
            raw_jsia = html.split('"url":"')[1].split('"')[0]
            jsia_url = "https:" + raw_jsia.replace("\\u0026", "&").replace("\\/", "/")
            # Force JSON format instead of JSONP for clean parsing
            jsia_url = jsia_url.replace("format=jsonp", "format=json")
            print(f"[INFO] Discovered metadata URL: {jsia_url}")
    except Exception as e:
        print(f"[WARNING] Failed to extract BookReaderJSIA URL: {e}")
        
    if not jsia_url:
        print("[ERROR] Could not resolve BookReaderJSIA metadata page. Skipping.")
        return False
        
    # 5. Fetch and parse pages from JSIA JSON
    print("[INFO] Fetching page lists from BookReader...")
    try:
        resp_jsia = session.get(jsia_url, timeout=20)
        jsia_data = resp_jsia.json()
        br_options = jsia_data.get("data", {}).get("brOptions", {})
        pages_list = br_options.get("data", [])
        
        flat_links = []
        for item in pages_list:
            for page in item:
                flat_links.append(page.get("uri"))
    except Exception as e:
        print(f"[ERROR] Failed to fetch or parse book pages JSON: {e}")
        return False
        
    if not flat_links:
        print("[ERROR] Resolved page link list is empty.")
        return False
        
    # Check if we got restricted preview links or direct images
    is_preview = any("BookReaderPreview.php" in l for l in flat_links)
    if is_preview:
        print("\n==============================================")
        print("[WARNING] The server served restricted preview image links.")
        print("[TIP] You must first Borrow this book in your web browser using your account")
        print("      before running this tool to access the high-resolution pages.")
        print("==============================================\n")
        if status_label:
            status_label.config(text="CDL Loan Missing. Borrow book first!", fg="#F44336")
        return False
        
    total_pages = len(flat_links)
    print(f"[INFO] Total Pages resolved: {total_pages}")
    
    downloads_dir = os.path.dirname(pdf_path)
    temp_dir = os.path.join(downloads_dir, f"temp_{ia_id}")
    os.makedirs(temp_dir, exist_ok=True)
    
    # 6. Concurrently download pages using ThreadPoolExecutor
    print(f"[INFO] Pulling {total_pages} pages concurrently. Please wait...")
    if status_label:
        status_label.config(text=f"Pulling pages (0/{total_pages})...", fg="#A855F7")
        
    jpeg_paths = [None] * total_pages
    downloaded_count = [0]
    download_lock = threading.Lock()
    
    high_res_links = [f"{link}&rotate=0&scale=3" for link in flat_links]
    
    def download_worker(index, link):
        global abort_requested
        if abort_requested:
            return
            
        page_file = os.path.join(temp_dir, f"page_{index:04d}.jpg")
        success = False
        headers = {
            "Referer": "https://archive.org/",
            "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Dest": "image",
        }
        
        # Retry up to 3 times
        for attempt in range(3):
            if abort_requested:
                return
            try:
                resp = session.get(link, headers=headers, timeout=20)
                if resp.status_code == 200:
                    image_content = resp.content
                    obf_header = resp.headers.get("X-Obfuscate")
                    if obf_header:
                        image_content = deobfuscate_image(image_content, link, obf_header)
                        
                    with open(page_file, "wb") as f:
                        f.write(image_content)
                    
                    success = True
                    break
                elif resp.status_code == 403:
                    session.post("https://archive.org/services/loans/loan/searchInside.php", data={"action": "grant_access", "identifier": ia_id}, timeout=10)
            except Exception:
                time.sleep(1)
                
        if success:
            with download_lock:
                jpeg_paths[index] = page_file
                downloaded_count[0] += 1
                progress = downloaded_count[0]
                if progress % 5 == 0 or progress == total_pages:
                    print(f"[INFO] Pulled page {progress}/{total_pages}...")
                    if status_label:
                        status_label.config(text=f"Pulling page {progress}/{total_pages}...", fg="#A855F7")
                        
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=8) as executor:
        for idx, link in enumerate(high_res_links):
            executor.submit(download_worker, idx, link)
            
    success_compiled = False
    valid_jpegs = [path for path in jpeg_paths if path is not None]
    
    if len(valid_jpegs) == total_pages and not abort_requested:
        print("[INFO] All pages successfully fetched and decrypted.")
        if status_label:
            status_label.config(text="Stitching page images into PDF...", fg="#00ADB5")
        compile_jpegs_to_pdf(valid_jpegs, pdf_path)
        success_compiled = True
    elif abort_requested:
        print("[INFO] Download aborted by user.")
    else:
        print(f"[ERROR] Page pulling failed. Only {len(valid_jpegs)}/{total_pages} pages were retrieved.")
        if status_label:
            status_label.config(text="Download failed. Some pages missing.", fg="#F44336")
            
    # Clean up temporary images
    print("[INFO] Cleaning up temporary image cache...")
    for path in valid_jpegs:
        try:
            os.remove(path)
        except:
            pass
    try:
        os.rmdir(temp_dir)
    except:
        pass
        
    return success_compiled


# Known Taylor & Francis / CRC Press / Routledge DOI prefixes
_TF_DOI_PREFIXES = (
    "10.1201/",  # CRC Press / Taylor & Francis books
    "10.4324/",  # Routledge books
    "10.1080/",  # T&F journals
    "10.3109/",  # Informa Healthcare
    "10.3390/",  # MDPI (not T&F, but shares API pattern)
)


def try_download_taylorfrancis(doi, title):
    """Taylor & Francis / CRC Press book downloader via the T&F content API.
    
    The API URL:
        https://api.taylorfrancis.com/content/books/mono/download
        ?identifierName=doi&identifierValue={doi}&type=googlepdf
    
    This returns a 302 redirect to a time-limited signed AWS S3 URL.
    - GET works and follows redirects correctly.
    - HEAD returns 403 on S3 (STS token mismatch), so we use GET only.
    - No institutional login is required for preview PDFs.
    """
    if not doi:
        return False
    # Only attempt for recognised T&F DOI prefixes
    if not any(doi.startswith(p) for p in _TF_DOI_PREFIXES):
        return False
    
    print("\n--- [BOOK STRATEGY] Querying Taylor & Francis Content API ---")
    try:
        import requests as _req
    except ImportError:
        print("[WARNING] 'requests' library not installed. Skipping Taylor & Francis strategy.")
        return False
    
    api_url = (
        f"https://api.taylorfrancis.com/content/books/mono/download"
        f"?identifierName=doi&identifierValue={urllib.parse.quote(doi, safe=':/')}&type=googlepdf"
    )
    print(f"[INFO] T&F API URL: {api_url}")
    register_discovered_url(f"https://www.taylorfrancis.com/books/{urllib.parse.quote(doi, safe=':/.')}", "Taylor & Francis Book Page")
    
    tf_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Accept': 'application/pdf,text/html,application/xhtml+xml,*/*;q=0.8',
        'Referer': 'https://www.taylorfrancis.com/',
    }
    
    try:
        # Stream the response so we can inspect bytes before writing
        r = _req.get(api_url, headers=tf_headers, allow_redirects=True, timeout=30, stream=True)
        
        # Check final resolved URL for diagnostic purposes
        final_url = r.url
        content_type = r.headers.get('Content-Type', '')
        content_length = r.headers.get('Content-Length', 'unknown')
        print(f"[INFO] T&F API → Final URL: {final_url[:80]}...")
        print(f"[INFO] Content-Type: {content_type} | Size: {content_length} bytes")
        
        if r.status_code != 200:
            print(f"[WARNING] T&F API returned HTTP {r.status_code}. Skipping.")
            r.close()
            return False
        
        # Read first 16 bytes to verify it's a real PDF
        first_chunk = next(r.iter_content(16), b'')
        if not first_chunk.startswith(b'%PDF'):
            r.close()
            decoded = first_chunk.decode('utf-8', errors='replace')
            print(f"[WARNING] T&F response is not a PDF. Snippet: {decoded[:80]}")
            return False
        
        # It's a PDF! Stream the rest and save
        filename = f"{clean_filename(title if title else doi)}.pdf"
        downloads_dir = os.path.join(os.path.dirname(__file__), "Downloads")
        os.makedirs(downloads_dir, exist_ok=True)
        pdf_path = os.path.join(downloads_dir, filename)
        
        print(f"[INFO] Downloading T&F PDF to: {pdf_path}")
        byte_count = len(first_chunk)
        with open(pdf_path, 'wb') as f:
            f.write(first_chunk)
            for chunk in r.iter_content(65536):
                if abort_requested:
                    r.close()
                    print("[INFO] T&F download aborted by user.")
                    return False
                f.write(chunk)
                byte_count += len(chunk)
        
        r.close()
        print(f"[SUCCESS] T&F PDF saved: '{filename}' ({byte_count:,} bytes)")
        return True
    except _req.exceptions.Timeout:
        print("[WARNING] T&F API request timed out (30s).")
    except _req.exceptions.ConnectionError as e:
        print(f"[WARNING] T&F API connection error: {e}")
    except Exception as e:
        print(f"[WARNING] Taylor & Francis download failed: {e}")
    return False


def try_download_book(identifier, title, status_label=None, root_widget=None):
    """Strategy for downloading free public domain books from Open Library / Internet Archive and Project Gutenberg."""
    if not identifier and not title:
        print("\n--- [BOOK STRATEGY] Skipped (No ID or Title available) ---")
        return False
        
    print("\n--- [BOOK STRATEGY] Querying Free Book Repositories ---")
    
    # Extract prefix and key
    key = ""
    prefix = ""
    if identifier and ":" in identifier:
        prefix, key = identifier.split(":", 1)
        prefix = prefix.strip().lower()
        key = key.strip()
        
    success = False
    
    # 1. If prefix is 'ia' (Internet Archive ID), download from archive.org directly!
    if prefix == "ia" and key:
        print(f"[INFO] Found Internet Archive ID: {key}")
        ia_url = f"https://archive.org/download/{key}/{key}.pdf"
        filename = f"{clean_filename(title if title else key)}.pdf"
        register_discovered_url(f"https://archive.org/details/{key}", "Internet Archive Details / Borrow Page")
        print(f"[INFO] Downloading direct PDF from Internet Archive: {ia_url}")
        success = download_file(ia_url, filename)
        if success:
            return True
        else:
            print("[TIP] This book is copyrighted or locked under Controlled Digital Lending (CDL).")
            print("      Archive.org blocks direct PDF pulls and serves them as protected online reader images.")
            
            # Fallback: Interactively scrape and compile images!
            success = try_download_ia_pages(key, filename, title, status_label=status_label, root_widget=root_widget)
            if success:
                return True
            
    # 2. Try Project Gutenberg search via Gutendex API (Title search)
    if not success and title:
        print(f"[INFO] Querying Project Gutenberg (Gutendex) for '{title}'...")
        try:
            gutendex_url = f"https://gutendex.com/books/?search={urllib.parse.quote(title)}"
            req = urllib.request.Request(gutendex_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
                
            results = data.get('results', [])
            if results:
                best_match = results[0]
                guten_id = best_match.get('id')
                formats = best_match.get('formats', {})
                
                # Check for PDF or EPUB formats
                pdf_url = formats.get('application/pdf') or formats.get('application/x-mobipocket-ebook')
                epub_url = formats.get('application/epub+zip')
                html_url = formats.get('text/html')
                
                # Prefer PDF, fallback to EPUB
                target_url = pdf_url if pdf_url else epub_url
                if not target_url and html_url:
                    target_url = html_url
                    
                if target_url:
                    ext = ".pdf" if "pdf" in target_url else (".epub" if "epub" in target_url else ".html")
                    print(f"[INFO] Found Gutenberg Book: '{best_match.get('title')}' (ID: {guten_id})")
                    register_discovered_url(f"https://www.gutenberg.org/ebooks/{guten_id}", "Project Gutenberg Details Page")
                    register_discovered_url(target_url, "Project Gutenberg Book File")
                    print(f"[INFO] Downloading book file: {target_url}")
                    filename = f"Gutenberg_{clean_filename(title)}{ext}"
                    success = download_file(target_url, filename)
                    if success:
                        return True
        except Exception as e:
            print(f"[WARNING] Project Gutenberg query failed: {e}")
            
    # 3. If we only have ISBN or OL Key, query Open Library's Edition API to resolve Internet Archive ID
    if not success and (prefix in ("isbn", "ol") or key):
        print(f"[INFO] Querying Open Library API to resolve Internet Archive ID...")
        try:
            ol_url = ""
            if prefix == "isbn":
                ol_url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{key}&format=json&jscmd=data"
                register_discovered_url(f"https://openlibrary.org/isbn/{key}", "OpenLibrary Book Page")
            elif prefix == "ol":
                ol_url = f"https://openlibrary.org/works/{key}.json"
                register_discovered_url(f"https://openlibrary.org/works/{key}", "OpenLibrary Work Page")
                
            if ol_url:
                req = urllib.request.Request(ol_url, headers=HEADERS)
                with urllib.request.urlopen(req, timeout=10) as response:
                    res_data = json.loads(response.read().decode())
                    
                ia_id = None
                if prefix == "isbn":
                    book_data = res_data.get(f"ISBN:{key}", {})
                    ia_id = book_data.get('identifiers', {}).get('archive', [None])[0] or book_data.get('ocaid')
                
                if ia_id:
                    ia_url = f"https://archive.org/download/{ia_id}/{ia_id}.pdf"
                    filename = f"{clean_filename(title if title else ia_id)}.pdf"
                    register_discovered_url(f"https://archive.org/details/{ia_id}", "Internet Archive Details / Borrow Page")
                    print(f"[INFO] Resolved Internet Archive ID: {ia_id}")
                    print(f"[INFO] Downloading direct PDF from Internet Archive: {ia_url}")
                    success = download_file(ia_url, filename)
                    if success:
                        return True
                    else:
                        print("[TIP] This resolved book is copyrighted or locked under CDL on Archive.org.")
                        print("      Archive.org blocks direct PDF pulls and serves them as protected online reader images.")
                        
                        # Fallback: Interactively scrape and compile images!
                        success = try_download_ia_pages(ia_id, filename, title, status_label=status_label, root_widget=root_widget)
                        if success:
                            return True
        except Exception as e:
            print(f"[WARNING] Open Library resolving failed: {e}")
            
    # 4. Fallback: Search Open Library by Title to get another matching copy with Internet Archive ID
    if not success and title:
        print(f"[INFO] Searching Open Library by Title to find alternate open editions...")
        try:
            search_url = f"https://openlibrary.org/search.json?title={urllib.parse.quote(title)}&fields=ia&limit=3"
            req = urllib.request.Request(search_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
                
            docs = data.get('docs', [])
            for doc in docs:
                ia_list = doc.get('ia', [])
                if ia_list:
                    ia_id = ia_list[0]
                    ia_url = f"https://archive.org/download/{ia_id}/{ia_id}.pdf"
                    filename = f"{clean_filename(title)}.pdf"
                    register_discovered_url(f"https://archive.org/details/{ia_id}", "Internet Archive Details / Borrow Page")
                    print(f"[INFO] Found alternate edition Internet Archive ID: {ia_id}")
                    print(f"[INFO] Downloading direct PDF from Internet Archive: {ia_url}")
                    success = download_file(ia_url, filename)
                    if success:
                        return True
                    else:
                        print("[TIP] This alternate edition is copyrighted or locked under CDL on Archive.org.")
                        print("      Archive.org blocks direct PDF pulls and serves them as protected online reader images.")
                        
                        # Fallback: Interactively scrape and compile images!
                        success = try_download_ia_pages(ia_id, filename, title, status_label=status_label, root_widget=root_widget)
                        if success:
                            return True
        except Exception as e:
            print(f"[WARNING] Alternate Open Library search failed: {e}")
            
    return False


def try_arxiv(doi, title):
    """Strategy 4: Query arXiv Open Access Preprint Server."""
    if doi and (doi.startswith("http://") or doi.startswith("https://")):
        return False
        
    if not doi and not title:
        print("\n--- [STRATEGY 4] Skipped (No DOI or Title available) ---")
        return False
        
    print("\n--- [STRATEGY 4] Querying arXiv Open Access Preprint Server ---")
    url = None
    if doi:
        clean_doi = doi.strip()
        url = f"http://export.arxiv.org/api/query?search_query=doi:{urllib.parse.quote(clean_doi)}&max_results=1"
    elif title:
        clean_title = title.strip().strip('"').strip("'")
        url = f"http://export.arxiv.org/api/query?search_query=ti:%22{urllib.parse.quote(clean_title)}%22&max_results=1"
        
    if not url:
        return False
        
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as response:
            xml_data = response.read().decode('utf-8', errors='ignore')
            
        pdf_links = re.findall(r'<link[^>]*?href=["\'](https?://arxiv\.org/pdf/[^"\']+)["\']', xml_data)
        ids = re.findall(r'<id>https?://arxiv\.org/abs/([^<\s]+)</id>', xml_data)
        
        if not pdf_links and ids:
            pdf_links = [f"https://arxiv.org/pdf/{ids[0]}.pdf"]
            
        if pdf_links:
            pdf_url = pdf_links[0]
            if not pdf_url.endswith('.pdf'):
                pdf_url += '.pdf'
            print(f"[INFO] Found arXiv PDF Target: {pdf_url}")
            register_discovered_url(pdf_url, "arXiv Open Access PDF")
            
            paper_name = title if title else (ids[0] if ids else 'arxiv_paper')
            filename = f"arxiv_{clean_filename(paper_name)}.pdf"
            return download_file(pdf_url, filename)
        else:
            print("[INFO] No matching document found on arXiv.")
    except Exception as e:
        print(f"[WARNING] arXiv lookup failed: {e}")
    return False


def try_europe_pmc(doi, title):
    """Strategy 5: Query Europe PMC Open Access Repository."""
    if doi and (doi.startswith("http://") or doi.startswith("https://")):
        return False
        
    if not doi and not title:
        print("\n--- [STRATEGY 5] Skipped (No DOI or Title available) ---")
        return False
        
    print("\n--- [STRATEGY 5] Querying Europe PMC Open Access Repository ---")
    url = None
    if doi:
        url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:{urllib.parse.quote(doi)}&format=json"
    elif title:
        url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22{urllib.parse.quote(title)}%22&format=json"
        
    if not url:
        return False
        
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            
        results = data.get('resultList', {}).get('result', [])
        if results:
            best_match = results[0]
            pmcid = best_match.get('pmcid')
            is_oa = best_match.get('isOpenAccess') == 'Y'
            
            pdf_url = None
            url_list = best_match.get('fullTextUrlList', {}).get('fullTextUrl', [])
            for u in url_list:
                if u.get('documentStyle') == 'pdf' or u.get('availabilityCode') == 'OA':
                    test_url = u.get('url', '')
                    if 'pdf' in test_url.lower() or test_url.endswith('.pdf'):
                        pdf_url = test_url
                        break
                        
            if not pdf_url and is_oa and pmcid:
                pdf_url = f"https://europepmc.org/articles/{pmcid}?pdf=render"
                
            if pdf_url:
                print(f"[INFO] Found Europe PMC PDF Target: {pdf_url}")
                register_discovered_url(pdf_url, "Europe PMC Open Access PDF")
                paper_name = title if title else (pmcid if pmcid else 'europepmc_paper')
                filename = f"pmc_{clean_filename(paper_name)}.pdf"
                return download_file(pdf_url, filename)
            else:
                print("[INFO] Document found on Europe PMC, but no direct PDF link is available.")
        else:
            print("[INFO] No matching document found on Europe PMC.")
    except Exception as e:
        print(f"[WARNING] Europe PMC lookup failed: {e}")
    return False


def try_researchgate(doi, title):
    """Strategy 3: Automated extraction from ResearchGate."""
    if not doi and not title:
        print("\n--- [STRATEGY 3] Skipped (No DOI or Title available) ---")
        return False
    print("\n--- [STRATEGY 3] Scraping ResearchGate for Full-Text ---")
    
    rg_profile_url = None
    
    # 0. Check if DOI is already a direct ResearchGate publication URL
    if doi and "researchgate.net/publication/" in doi:
        rg_profile_url = doi
        print(f"[INFO] Using provided direct ResearchGate publication URL: {rg_profile_url}")
        
    # 1. If it is a ResearchGate specific DOI, attempt direct internal resolver link
    elif doi and doi.strip().startswith("10.13140/"):
        resolver_url = f"https://www.researchgate.net/doi/{doi.strip()}"
        print(f"[INFO] Detected ResearchGate DOI. Attempting direct internal resolver: {resolver_url}")
        try:
            req = urllib.request.Request(resolver_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as response:
                final_url = response.geturl()
                if "researchgate.net/publication/" in final_url:
                    rg_profile_url = final_url
                    print(f"[INFO] Direct internal resolver succeeded: {rg_profile_url}")
        except Exception as e:
            print(f"[WARNING] Direct internal resolver bypassed/failed (usually due to 403 Forbidden): {e}")
            
    # 2. Direct resolution using Crossref / Handle API as fallback
    if doi and not rg_profile_url:
        resolved_url = resolve_doi_to_url(doi)
        if resolved_url:
            print(f"[INFO] Resolving resolved DOI URL: {resolved_url}")
            try:
                req = urllib.request.Request(resolved_url, headers=HEADERS)
                with urllib.request.urlopen(req, timeout=10) as response:
                    final_url = response.geturl()
                    if "researchgate.net/publication/" in final_url:
                        rg_profile_url = final_url
                        print(f"[INFO] Direct DOI resolution succeeded: {rg_profile_url}")
            except Exception as e:
                print(f"[WARNING] Direct DOI URL resolution bypassed/failed: {e}")
            
    # 3. Direct resolution via doi.org redirect as a fallback
    if doi and not rg_profile_url:
        print(f"[INFO] Attempting direct DOI resolution via doi.org...")
        try:
            url = f"https://doi.org/{doi}"
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as response:
                final_url = response.geturl()
                if "researchgate.net/publication/" in final_url:
                    rg_profile_url = final_url
                    print(f"[INFO] Direct DOI resolution succeeded: {rg_profile_url}")
        except Exception as e:
            print(f"[WARNING] Direct DOI resolution bypassed/failed: {e}")
            
    # Step 1: Discover the paper link using an un-indexed engine search query targeting ResearchGate
    if not rg_profile_url:
        query = doi if doi else title
        search_url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query + ' site:researchgate.net/publication/')}"
        try:
            req = urllib.request.Request(search_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as response:
                html = response.read().decode('utf-8', errors='ignore')
                
            # Match ResearchGate publication URLs out of DuckDuckGo raw hrefs
            links = re.findall(r'href="([^"]*researchgate\.net/publication/[^"]*)"', html)
            if links:
                # Unquote the URL from search query routing
                rg_profile_url = urllib.parse.unquote(links[0])
                # Drop tracking arguments if appended by the search engine
                if "&" in rg_profile_url:
                    rg_profile_url = rg_profile_url.split("&")[0]
                print(f"[INFO] Target Profile Found: {rg_profile_url}")
        except Exception as e:
            print(f"[WARNING] Public index routing failed: {e}")
            
    if rg_profile_url:
        register_discovered_url(rg_profile_url, "ResearchGate Profile Page")
        
    if not rg_profile_url:
        print("[INFO] Could not map paper details to a definitive ResearchGate profile.")
        return False

    # Step 2: Scrape the actual profile page for open full-text assets
    try:
        req = urllib.request.Request(rg_profile_url, headers=HEADERS)
        with urllib.request.urlopen(req) as response:
            page_source = response.read().decode('utf-8', errors='ignore')
            final_profile_url = response.geturl()
            
        # Check for standard ResearchGate asset download links 
        # (Usually match: /publication/X_Title/file/Y.pdf or specific token structures)
        pdf_matches = re.findall(r'href="([^"]+\.pdf[^"]*)"', page_source)
        pdf_matches += re.findall(r'["\'](https://www\.researchgate\.net/profile/[^"\']+/publication/[^"\']+/file/[^"\']+ \.pdf)["\']', page_source)
        
        # Fallback to look for raw data-attributes or download endpoints
        pdf_matches += [f"https://www.researchgate.net/{m}" for m in re.findall(r'href="(/publication/[^"]+/file/[^"]+)"', page_source)]

        target_pdf = None
        
        # 1. Parse publication segment from profile URL path
        parsed_profile = urllib.parse.urlparse(final_profile_url)
        pub_segment = None
        path_parts = parsed_profile.path.strip('/').split('/')
        for i, part in enumerate(path_parts):
            if part == 'publication' and i + 1 < len(path_parts):
                pub_segment = path_parts[i + 1]
                break
                
        # 2. Parse linkId from profile URL query parameters if present
        link_id = None
        query_params = urllib.parse.parse_qs(parsed_profile.query)
        if 'linkId' in query_params:
            link_id = query_params['linkId'][0]
            
        # 3. Analyze matches to extract linkId and resolve absolute links
        for link in pdf_matches:
            # Extract link_id from the PDF path if not found in query parameters
            if not link_id:
                link_id_match = re.search(r'/links/([a-f0-9]+)', link)
                if link_id_match:
                    link_id = link_id_match.group(1)
            
            # Resolve relative links (relative to domain root instead of relative to publication dir)
            parsed_base = urllib.parse.urlparse(final_profile_url)
            base_domain = f"{parsed_base.scheme}://{parsed_base.netloc}"
            if link.startswith('/'):
                abs_link = base_domain + link
            elif link.startswith('profile/'):
                abs_link = base_domain + '/' + link
            else:
                abs_link = urllib.parse.urljoin(final_profile_url, link.strip())
                
            # Filter for direct asset download URLs
            if any(marker in abs_link for marker in ["/file/", "download", "/links/", "/publication/"]):
                if not target_pdf:
                    target_pdf = abs_link
                    
        # 4. Attempt downloads sequentially
        success = False
        filename = f"RG_{clean_filename(title if title else doi.replace('/', '_'))}.pdf"
        
        # Priority 1: Try direct PDF URL (which yields raw PDF bytes)
        if target_pdf:
            print(f"[INFO] Attempting download from direct PDF URL: {target_pdf}")
            register_discovered_url(target_pdf, "ResearchGate Direct PDF Link")
            success = download_file(target_pdf, filename, referer=final_profile_url)
            
        # Priority 2: Fallback to constructed official download endpoint
        if not success and pub_segment and link_id:
            official_download_url = f"https://www.researchgate.net/publication/{pub_segment}/link/{link_id}/download"
            print(f"[INFO] Direct download failed/not-valid. Attempting constructed official download link: {official_download_url}")
            register_discovered_url(official_download_url, "ResearchGate Constructed Download Link")
            success = download_file(official_download_url, filename, referer=final_profile_url)
            
        if success:
            return True
        else:
            print("\n[WARNING] ResearchGate's Cloudflare security walls are actively blocking automated scripts.")
            print("[INFO] Launching the direct PDF in your default web browser...")
            try:
                import webbrowser
                # Prioritize direct PDF URL, fallback to profile page
                open_url = target_pdf if target_pdf else final_profile_url
                webbrowser.open(open_url)
                print("[SUCCESS] Opened target PDF link in your web browser!")
                return True
            except Exception as browser_err:
                print(f"[ERROR] Failed to launch web browser: {browser_err}")
                return False
            
    except Exception as e:
        print(f"[WARNING] ResearchGate scraping routine failed: {e}")
        print("[TIP] ResearchGate may be prompting a Captcha verification wall against scripts.")
    return False


is_running = False
current_mode = "Direct"
research_query = ""
current_page = 1
has_more_results = True
card_buttons = []
prev_btn = None
next_btn = None
page_lbl = None
results_frame = None
results_container = None


def reset_gui_state(run_button, entry_widget):
    """Restore the GUI download button and entry box back to their idle states."""
    global is_running, current_mode, prev_btn, next_btn, card_buttons
    is_running = False
    
    # Restore main action button text based on mode
    if current_mode == "Direct":
        run_button.config(text="Download Document", bg="#8B5CF6", activebackground="#A78BFA", state='normal')
    else:
        run_button.config(text="Search Keywords", bg="#8B5CF6", activebackground="#A78BFA", state='normal')
        
    entry_widget.config(state='normal')
    
    # Re-enable pagination and cards
    if prev_btn and next_btn:
        update_pagination_states()
    for btn in card_buttons:
        try:
            btn.config(state='normal')
        except:
            pass


def update_pagination_states():
    """Helper to update the enabled/disabled states of pagination controls."""
    global current_page, prev_btn, next_btn, has_more_results
    if not prev_btn or not next_btn:
        return
        
    if current_page == 1:
        prev_btn.config(state='disabled')
    else:
        prev_btn.config(state='normal')
        
    if has_more_results:
        next_btn.config(state='normal')
    else:
        next_btn.config(state='disabled')


def run_pipeline_bg(identifier, status_label, log_widget, run_button, entry_widget, root_widget):
    """Run the download pipeline in a background thread and output logs to the GUI."""
    global abort_requested, discovered_urls
    discovered_urls = []
    
    # Resolve identifier (DOI or Title)
    target_doi = None
    target_title = None
    
    ident = identifier.strip()
    if ident.startswith("10."):
        target_doi = ident
    elif ident.startswith("http://") or ident.startswith("https://"):
        target_doi = ident
    elif any(ident.lower().startswith(prefix) for prefix in ("ia:", "isbn:", "ol:")):
        target_doi = ident
    else:
        target_title = ident
        
    class RedirectText:
        def __init__(self, text_widget):
            self.text_widget = text_widget
        def write(self, string):
            self.text_widget.insert('end', string)
            self.text_widget.see('end')
        def flush(self):
            pass
            
    old_stdout = sys.stdout
    sys.stdout = RedirectText(log_widget)
    
    try:
        if abort_requested:
            raise InterruptedError("Cancelled by user")

        if not target_doi and target_title:
            print(f"Beginning Processing Pipeline for Title: '{target_title}'...")
            status_label.config(text="Resolving Title DOI...", fg="#00ADB5")
            target_doi = resolve_title_to_doi(target_title)
        else:
            print(f"Beginning Processing Pipeline for DOI: {target_doi}...")
            
        if abort_requested:
            raise InterruptedError("Cancelled by user")

        success = False
        is_book_identifier = target_doi and any(target_doi.lower().startswith(prefix) for prefix in ("ia:", "isbn:", "ol:"))
        
        if is_book_identifier:
            status_label.config(text="Querying Book Repositories...", fg="#00ADB5")
            success = try_download_book(target_doi, target_title, status_label=status_label, root_widget=root_widget)
        else:
            if target_doi:
                # Try Taylor & Francis first for known T&F DOI prefixes
                if not success and any(target_doi.startswith(p) for p in _TF_DOI_PREFIXES):
                    status_label.config(text="Querying Taylor & Francis API...", fg="#00ADB5")
                    success = try_download_taylorfrancis(target_doi, target_title)

                if not success:
                    status_label.config(text="Querying Unpaywall Database...", fg="#00ADB5")
                    success = try_unpaywall(target_doi)
                
                if abort_requested:
                    raise InterruptedError("Cancelled by user")
                    
                if not success:
                    status_label.config(text="Querying Sci-Hub Shadows...", fg="#00ADB5")
                    success = try_scihub(target_doi)
                
            if abort_requested:
                raise InterruptedError("Cancelled by user")

            if not success:
                status_label.config(text="Querying arXiv...", fg="#00ADB5")
                success = try_arxiv(target_doi, target_title)
                
            if abort_requested:
                raise InterruptedError("Cancelled by user")

            if not success:
                status_label.config(text="Querying Europe PMC...", fg="#00ADB5")
                success = try_europe_pmc(target_doi, target_title)
                
            if abort_requested:
                raise InterruptedError("Cancelled by user")

            if not success:
                status_label.config(text="Querying ResearchGate...", fg="#00ADB5")
                success = try_researchgate(target_doi, target_title)
                
            if abort_requested:
                raise InterruptedError("Cancelled by user")

            # Final resort: check if it matches Gutenberg / OpenLibrary public domain books
            if not success:
                status_label.config(text="Querying Book Repositories...", fg="#00ADB5")
                success = try_download_book(target_doi, target_title, status_label=status_label, root_widget=root_widget)
                
            if abort_requested:
                raise InterruptedError("Cancelled by user")

        if success:
            status_label.config(text="Document Pulled Successfully!", fg="#4CAF50")
            print("\n==============================================")
            print("[PROCESS FINISHED] Document pulled successfully.")
            print("==============================================")
        else:
            # Fallback to browser launching if any URLs were discovered
            valid_fallbacks = sorted(discovered_urls, key=lambda x: x[1])
            if valid_fallbacks:
                best_url, rank, label = valid_fallbacks[0]
                print(f"\n[WARNING] Programmatic binary download failed (likely due to Cloudflare protection).")
                print(f"[INFO] Launching the best discovered URL in your default web browser ({label}):")
                print(f"       {best_url}")
                try:
                    import webbrowser
                    webbrowser.open(best_url)
                    status_label.config(text=f"Opened in Browser: {label}", fg="#4CAF50")
                    print("\n==============================================")
                    print("[PROCESS FINISHED] Document opened in web browser.")
                    print("==============================================")
                except Exception as browser_err:
                    print(f"[ERROR] Failed to launch web browser: {browser_err}")
                    status_label.config(text="Pull Failed. Check active channels.", fg="#F44336")
                    print("\n==============================================")
                    print("[PROCESS FAILED] File could not be retrieved from active channels.")
                    print("==============================================")
            else:
                status_label.config(text="Pull Failed. Check active channels.", fg="#F44336")
                print("\n==============================================")
                print("[PROCESS FAILED] File could not be retrieved from active channels.")
                print("==============================================")
            
    except InterruptedError:
        status_label.config(text="Research Stopped.", fg="#FF9800")
        print("\n==============================================")
        print("[PROCESS CANCELLED] Stopped by user request.")
        print("==============================================")
    except Exception as ex:
        status_label.config(text="An error occurred during download.", fg="#F44336")
        print(f"\n[ERROR] Thread failed: {ex}")
    finally:
        sys.stdout = old_stdout
        reset_gui_state(run_button, entry_widget)


def launch_gui():
    """Launch the modern dark-themed desktop GUI for Paper Downloader."""
    global prev_btn, next_btn, page_lbl, results_frame, results_container, card_buttons
    
    root = tk.Tk()
    root.title("Premium Paper Downloader v2.1 by Yazid YOUCEF")
    root.configure(bg="#0D0B14")
    
    # Custom styled scrollbar matching Deep Purple palette
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Vertical.TScrollbar", gripcount=0,
                    background="#2E2543", darkcolor="#1A1625", lightcolor="#1A1625",
                    troughcolor="#1A1625", bordercolor="#1A1625", arrowcolor="#8B5CF6")
    style.map("Vertical.TScrollbar",
              background=[('active', '#8B5CF6'), ('!disabled', '#2E2543')])
    
    # Load and set personalized application icon gracefully
    icon_path = os.path.join(os.path.dirname(__file__), "app_icon.png")
    _icon_ref = None  # keep a reference to prevent GC
    if os.path.exists(icon_path):
        # Try PIL/Pillow first (handles all PNG types reliably)
        try:
            from PIL import Image, ImageTk
            pil_img = Image.open(icon_path).resize((64, 64), Image.LANCZOS)
            _icon_ref = ImageTk.PhotoImage(pil_img)
            root.iconphoto(True, _icon_ref)
        except ImportError:
            # PIL not installed — fall back to native Tkinter PNG loader
            try:
                _icon_ref = tk.PhotoImage(file=icon_path)
                root.iconphoto(True, _icon_ref)
            except Exception as e:
                print(f"[WARNING] Could not load icon (install Pillow for best results): {e}")
        except Exception as e:
            print(f"[WARNING] Failed to load custom window icon via PIL: {e}")
    
    # Center window on screen (taller to fit permanently visible logs and keyword results)
    w, h = 650, 750
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(True, True)
    
    # Header Section (Centered)
    header_frame = tk.Frame(root, bg="#0D0B14", pady=12)
    header_frame.pack(fill='x', padx=25)
    
    header_lbl = tk.Label(header_frame, text="PAPER DOWNLOADER v2.1", bg="#0D0B14", fg="#A855F7", font=('Segoe UI Semibold', 16))
    header_lbl.pack(anchor='center')
    
    sub_lbl = tk.Label(header_frame, text="Search and retrieve academic documents by DOI or Title dynamically.", bg="#0D0B14", fg="#A78BFA", font=('Segoe UI', 9))
    sub_lbl.pack(anchor='center', pady=(2, 0))
    
    author_lbl = tk.Label(header_frame, text="Designed & Developed by Yazid YOUCEF", bg="#0D0B14", fg="#8B5CF6", font=('Segoe UI', 8, 'italic'))
    author_lbl.pack(anchor='center', pady=(3, 0))
    
    # Main Input Card (Centered Elements)
    card_frame = tk.Frame(root, bg="#1A1625", bd=1, relief='flat', padx=20, pady=15)
    card_frame.pack(fill='x', padx=25, pady=(5, 5))
    
    # Segmented Mode Selector
    mode_frame = tk.Frame(card_frame, bg="#1A1625")
    mode_frame.pack(anchor='center', pady=(0, 10))
    
    mode_var = tk.StringVar(value="Direct")
    
    def on_mode_change():
        global current_mode, is_running
        if is_running:
            mode_var.set(current_mode)
            return
            
        current_mode = mode_var.get()
        if current_mode == "Direct":
            run_button.config(text="Download Document")
            input_lbl.config(text="Enter DOI or Title:")
            clear_research_results()
            type_frame.pack_forget()
        elif current_mode == "Research":
            run_button.config(text="Search Keywords")
            input_lbl.config(text="Enter Keywords:")
            type_frame.pack(anchor='center', pady=(4, 2))
        else:  # Author
            run_button.config(text="Search by Author")
            input_lbl.config(text="Enter Author Name:")
            type_frame.pack(anchor='center', pady=(4, 2))
            
    direct_rb = tk.Radiobutton(mode_frame, text="Direct", variable=mode_var, value="Direct", bg="#1A1625", fg="#EEEEEE", activebackground="#1A1625", activeforeground="#A855F7", selectcolor="#0D0B14", font=('Segoe UI', 9), command=on_mode_change, cursor="hand2")
    direct_rb.pack(side='left', padx=8)
    
    research_rb = tk.Radiobutton(mode_frame, text="By Keywords", variable=mode_var, value="Research", bg="#1A1625", fg="#EEEEEE", activebackground="#1A1625", activeforeground="#A855F7", selectcolor="#0D0B14", font=('Segoe UI', 9), command=on_mode_change, cursor="hand2")
    research_rb.pack(side='left', padx=8)
    
    author_mode_rb = tk.Radiobutton(mode_frame, text="By Author", variable=mode_var, value="Author", bg="#1A1625", fg="#EEEEEE", activebackground="#1A1625", activeforeground="#A855F7", selectcolor="#0D0B14", font=('Segoe UI', 9), command=on_mode_change, cursor="hand2")
    author_mode_rb.pack(side='left', padx=8)
    
    input_lbl = tk.Label(card_frame, text="Enter DOI or Title:", bg="#1A1625", fg="#EEEEEE", font=('Segoe UI Semibold', 10))
    input_lbl.pack(anchor='center', pady=(8, 5))
    
    # Modern rounded entry emulation
    entry_container = tk.Frame(card_frame, bg="#2E2543", bd=0, padx=8, pady=6)
    entry_container.pack(fill='x', pady=5)
    
    entry = tk.Entry(entry_container, bg="#2E2543", fg="#FFFFFF", insertbackground="#FFFFFF", bd=0, font=('Segoe UI', 11), relief='flat', justify='center')
    entry.pack(fill='x')
    entry.focus_set()
    
    # Filter row (All / Papers / Books) — visible in Research and Author modes, hidden in Direct
    type_frame = tk.Frame(card_frame, bg="#1A1625")
    # NOTE: not packed here; shown via on_mode_change()
    
    type_var = tk.StringVar(value="All")
    
    type_lbl = tk.Label(type_frame, text="Filter:", bg="#1A1625", fg="#9CA3AF", font=('Segoe UI Semibold', 9))
    type_lbl.pack(side='left', padx=(0, 10))
    
    all_rb = tk.Radiobutton(type_frame, text="All", variable=type_var, value="All", bg="#1A1625", fg="#EEEEEE", activebackground="#1A1625", activeforeground="#A855F7", selectcolor="#0D0B14", font=('Segoe UI', 9), cursor="hand2")
    all_rb.pack(side='left', padx=10)
    
    papers_rb = tk.Radiobutton(type_frame, text="Papers", variable=type_var, value="Papers", bg="#1A1625", fg="#EEEEEE", activebackground="#1A1625", activeforeground="#A855F7", selectcolor="#0D0B14", font=('Segoe UI', 9), cursor="hand2")
    papers_rb.pack(side='left', padx=10)
    
    books_rb = tk.Radiobutton(type_frame, text="Books", variable=type_var, value="Books", bg="#1A1625", fg="#EEEEEE", activebackground="#1A1625", activeforeground="#A855F7", selectcolor="#0D0B14", font=('Segoe UI', 9), cursor="hand2")
    books_rb.pack(side='left', padx=10)
    
    # Status label — always visible
    status_label = tk.Label(card_frame, text="Ready for input.", bg="#1A1625", fg="#A78BFA", font=('Segoe UI', 10, 'italic'))
    status_label.pack(pady=5, anchor='center')
    
    # --- Interactive Research Mode Results Frame ---
    results_frame = tk.Frame(root, bg="#0D0B14", padx=25)
    
    results_container = tk.Frame(results_frame, bg="#0D0B14")
    results_container.pack(fill='both', expand=True)
    
    def on_container_resize(event):
        new_width = event.width
        new_wrap = max(300, new_width - 180)
        for card in results_container.winfo_children():
            try:
                details_f = card.winfo_children()[0]
                children = details_f.winfo_children()
                if len(children) >= 1:
                    title_lbl = children[0]
                    title_lbl.config(wraplength=new_wrap)
                if len(children) >= 3:
                    meta_lbl = children[2]
                    meta_lbl.config(wraplength=new_wrap)
            except Exception:
                pass
                
    results_container.bind('<Configure>', on_container_resize)
    
    # Navigation bar for pagination
    nav_frame = tk.Frame(results_frame, bg="#0D0B14", pady=5)
    nav_frame.pack(fill='x')
    
    def on_prev_click():
        global current_page, research_query
        if current_page > 1:
            load_research_page(research_query, current_page - 1)
            
    def on_next_click():
        global current_page, research_query
        load_research_page(research_query, current_page + 1)
        
    prev_btn = tk.Button(nav_frame, text="◀ Previous", bg="#2E2543", fg="#EEEEEE", activebackground="#3F335C", activeforeground="#FFFFFF", disabledforeground="#8E8A9F", bd=0, font=('Segoe UI', 9), padx=12, pady=4, cursor="hand2", command=on_prev_click, state='disabled')
    prev_btn.pack(side='left', padx=15)
    
    page_lbl = tk.Label(nav_frame, text="Page 1", bg="#0D0B14", fg="#A855F7", font=('Segoe UI Semibold', 10))
    page_lbl.pack(side='left', fill='x', expand=True)
    
    next_btn = tk.Button(nav_frame, text="Next ▶", bg="#2E2543", fg="#EEEEEE", activebackground="#3F335C", activeforeground="#FFFFFF", disabledforeground="#8E8A9F", bd=0, font=('Segoe UI', 9), padx=12, pady=4, cursor="hand2", command=on_next_click)
    next_btn.pack(side='right', padx=15)
    
    # Details text area container (Always visible)
    logs_frame = tk.Frame(root, bg="#0D0B14", padx=25)
    logs_frame.pack(fill='both', expand=True, pady=(0, 15))
    
    # Sleek console header with a "Clear Logs" button
    logs_header = tk.Frame(logs_frame, bg="#0D0B14")
    logs_header.pack(fill='x', pady=(0, 6))
    
    console_lbl = tk.Label(logs_header, text="📜  Pipeline Console Logs", bg="#0D0B14", fg="#A78BFA", font=('Segoe UI Semibold', 9))
    console_lbl.pack(side='left')
    
    def clear_logs():
        log_area.delete('1.0', 'end')
        
    clear_btn = tk.Button(
        logs_header,
        text="🧹 Clear Logs",
        bg="#2E2543",
        fg="#EEEEEE",
        activebackground="#3F335C",
        activeforeground="#FFFFFF",
        disabledforeground="#8E8A9F",
        bd=0,
        font=('Segoe UI Semibold', 8),
        padx=10,
        pady=2,
        cursor="hand2",
        command=clear_logs
    )
    clear_btn.pack(side='right')
    
    log_area = tk.Text(logs_frame, bg="#1A1625", fg="#F3E8FF", insertbackground="#FFFFFF", bd=0, font=('Consolas', 9), relief='flat', height=10)
    scrollbar = ttk.Scrollbar(logs_frame, orient="vertical", command=log_area.yview, style="Vertical.TScrollbar")
    log_area.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    log_area.pack(side="left", fill="both", expand=True)
    
    # Setup thread synchronization events
    running_event = threading.Event()
    
    def animate_loading(label, run_event, count=0):
        if not run_event.is_set():
            return
        dots = "." * ((count % 3) + 1)
        spaces = " " * (3 - len(dots))
        label.config(text=f"Processing Pipeline {dots}{spaces}")
        root.after(400, lambda: animate_loading(label, run_event, count + 1))
        
    def clear_research_results():
        """Clear all loaded paper cards from the research view."""
        global card_buttons
        for widget in results_container.winfo_children():
            widget.destroy()
        card_buttons = []
        results_frame.pack_forget()
        
    def reset_inputs():
        """Re-enable all input fields (called after any operation completes)."""
        entry.config(state='normal')
        
    def start_individual_download(doi, paper_title):
        """Trigger threaded background downloader for a specific result card's DOI."""
        global is_running, abort_requested
        
        # Disable all UI controls to prevent multiple actions
        is_running = True
        abort_requested = False
        
        entry.config(state='disabled')
        run_button.config(state='disabled')
        prev_btn.config(state='disabled')
        next_btn.config(state='disabled')
        for btn in card_buttons:
            btn.config(state='disabled')
            
        status_label.config(text="Downloading paper...", fg="#A855F7")
        running_event.set()
        animate_loading(status_label, running_event)
        
        # Clear log area
        log_area.delete('1.0', 'end')
        
        def dl_thread():
            try:
                # Use DOI if present, fallback to exact Title
                target = doi if doi else paper_title
                run_pipeline_bg(target, status_label, log_area, run_button, entry, root)
            finally:
                running_event.clear()
                
        t = threading.Thread(target=dl_thread)
        t.daemon = True
        t.start()
        
    def display_research_results(results, query, page):
        """Render the 5 results cards dynamically into the results frame."""
        global current_page, research_query, card_buttons, has_more_results
        
        if not results:
            if page > 1:
                status_label.config(text="No more results available.", fg="#FBBF24")
                current_page = page - 1
                page_lbl.config(text=f"Page {current_page}")
                has_more_results = False
                update_pagination_states()
                reset_gui_state(run_button, entry)
                return
            else:
                status_label.config(text="No matching documents found.", fg="#F44336")
                clear_research_results()
                reset_gui_state(run_button, entry)
                reset_inputs()
                return
                
        current_page = page
        research_query = query
        card_buttons = []
        has_more_results = (len(results) == 5)
        
        clear_research_results()
            
        results_frame.pack(fill='x', padx=25, pady=(5, 5), before=logs_frame)
        page_lbl.config(text=f"Page {page}")
        
        # Determine initial dynamic wraplength
        current_wrap = max(380, results_container.winfo_width() - 180)
        
        # Build 5 dynamic results cards
        for idx, result in enumerate(results):
            card = tk.Frame(results_container, bg="#1A1625", pady=6, padx=12, bd=0)
            card.pack(fill='x', pady=3)
            
            # Left panel - Paper details
            details_f = tk.Frame(card, bg="#1A1625")
            details_f.pack(side='left', fill='both', expand=True)
            
            title_lbl = tk.Label(details_f, text=f"{idx+1}. {result['title']}", bg="#1A1625", fg="#FFFFFF", font=('Segoe UI Semibold', 9), anchor='w', wraplength=current_wrap, justify='left')
            title_lbl.pack(anchor='w')
            
            # Format identifier label dynamically based on book/paper prefixes (ISBN instead of DOI for books)
            raw_id = result['doi']
            is_book = (type_var.get() == "Books") or (result.get('source') == 'openlibrary') or (raw_id and any(raw_id.lower().startswith(prefix) for prefix in ("ia:", "isbn:", "ol:")))
            
            if raw_id:
                if raw_id.lower().startswith("ia:"):
                    id_label = "Internet Archive ID"
                    id_val = raw_id.split(":", 1)[1]
                elif raw_id.lower().startswith("isbn:"):
                    id_label = "ISBN"
                    id_val = raw_id.split(":", 1)[1]
                elif raw_id.lower().startswith("ol:"):
                    id_label = "OpenLibrary Key"
                    id_val = raw_id.split(":", 1)[1]
                else:
                    id_label = "DOI"
                    id_val = raw_id
                doi_str = f"{id_label}: {id_val}"
            else:
                doi_str = "ISBN/ID: N/A" if is_book else "DOI: N/A"
                
            if is_book:
                badge_text = "  [Free eBook Available]"
                badge_fg = "#10B981"
            else:
                badge_text = "  [Direct PDF Available]" if result.get('is_oa') else "  [Sci-Hub / ResearchGate Fallback]"
                badge_fg = "#10B981" if result.get('is_oa') else "#8B5CF6"
            
            doi_frame = tk.Frame(details_f, bg="#1A1625")
            doi_frame.pack(anchor='w', pady=(1, 0))
            
            doi_lbl = tk.Label(doi_frame, text=doi_str, bg="#1A1625", fg="#A78BFA", font=('Segoe UI', 8, 'italic'), anchor='w')
            doi_lbl.pack(side='left')
            
            badge_lbl = tk.Label(doi_frame, text=badge_text, bg="#1A1625", fg=badge_fg, font=('Segoe UI Semibold', 8), anchor='w')
            badge_lbl.pack(side='left')
            
            meta_str = f"Authors: {result['authors']} | {result['journal']} ({result['year']})"
            meta_lbl = tk.Label(details_f, text=meta_str, bg="#1A1625", fg="#9CA3AF", font=('Segoe UI', 8), anchor='w', wraplength=current_wrap, justify='left')
            meta_lbl.pack(anchor='w', pady=(1, 0))
            
            # Right panel - Action Buttons
            btn_container = tk.Frame(card, bg="#1A1625")
            btn_container.pack(side='right', padx=(10, 0))
            
            # Use DOI closure variable
            target_doi = result['doi']
            target_title = result['title']
            
            # View Button
            view_btn = tk.Button(
                btn_container, 
                text="View", 
                bg="#8B5CF6", 
                fg="#FFFFFF", 
                activebackground="#A78BFA", 
                activeforeground="#FFFFFF", 
                disabledforeground="#8E8A9F", 
                bd=0, 
                font=('Segoe UI Semibold', 9), 
                padx=12, 
                pady=4, 
                cursor="hand2", 
                command=lambda d=target_doi, t=target_title, ib=is_book: view_document_in_browser(d, t, is_book=ib)
            )
            view_btn.pack(side='left', padx=(0, 6))
            card_buttons.append(view_btn)
            
            # Download Button
            dl_btn = tk.Button(
                btn_container, 
                text="Download", 
                bg="#10B981", 
                fg="#FFFFFF", 
                activebackground="#059669", 
                activeforeground="#FFFFFF", 
                disabledforeground="#8E8A9F", 
                bd=0, 
                font=('Segoe UI Semibold', 9), 
                padx=12, 
                pady=4, 
                cursor="hand2", 
                command=lambda d=target_doi, t=target_title: start_individual_download(d, t)
            )
            dl_btn.pack(side='left')
            card_buttons.append(dl_btn)
            
        # Update navigation buttons state
        update_pagination_states()
        
        # Re-enable search button
        status_label.config(text="Research matches loaded successfully.", fg="#4CAF50")
        reset_gui_state(run_button, entry)
        reset_inputs()
        
    def load_research_page(query, page):
        """Fetch results dynamically for a page offset in a background thread."""
        global is_running, abort_requested
        
        is_running = True
        abort_requested = False
        
        # Disable inputs
        entry.config(state='disabled')
        run_button.config(text="Stop Research", bg="#D32F2F", activebackground="#EF5350")
        prev_btn.config(state='disabled')
        next_btn.config(state='disabled')
        for btn in card_buttons:
            btn.config(state='disabled')
            
        # Read filter value safely on the main thread before starting background thread
        type_val = type_var.get()
        # In Author mode, the main entry IS the author query; title is empty
        if current_mode == "Author":
            title_val = ""
            author_val = query  # query param holds the author name
        else:
            title_val = query
            author_val = ""
        
        if type_val == "Books":
            status_label.config(text="Querying OpenLibrary Database...", fg="#A855F7")
        elif current_mode == "Author":
            status_label.config(text="Searching by Author...", fg="#A855F7")
        else:
            status_label.config(text="Querying Crossref Database...", fg="#A855F7")
        running_event.set()
        animate_loading(status_label, running_event)
        
        offset = (page - 1) * 5

        def fetch_thread(type_filter_val, title_q, author_q):
            try:
                if author_q and not title_q:
                    # By Author mode: search OpenAlex AND ResearchGate, combine & deduplicate
                    results_oa = []
                    try:
                        results_oa = search_openalex_by_author(author_q, offset=0, rows=100, type_filter=type_filter_val)
                    except Exception as e_oa:
                        print(f"[WARNING] OpenAlex author search failed: {e_oa}")
                        
                    results_rg = []
                    try:
                        results_rg = search_researchgate_by_author(author_q, offset=0, rows=100, type_filter=type_filter_val)
                    except Exception as e_rg:
                        print(f"[WARNING] ResearchGate author search failed: {e_rg}")
                        
                    # Merge and deduplicate by title or URL/DOI
                    seen_titles = set()
                    seen_dois = set()
                    merged = []
                    
                    for item in results_rg + results_oa:
                        title_norm = re.sub(r'[^a-z0-9]', '', item['title'].lower())
                        doi_val = item.get('doi', '')
                        
                        if title_norm in seen_titles:
                            continue
                        if doi_val and doi_val in seen_dois:
                            continue
                            
                        seen_titles.add(title_norm)
                        if doi_val:
                            seen_dois.add(doi_val)
                        merged.append(item)
                        
                    results = merged[offset : offset + 5]
                elif type_filter_val == "Books":
                    results = search_openlibrary(title_q, author=author_q, offset=offset, rows=5)
                else:
                    results = search_crossref(title_q, offset=offset, rows=5, type_filter=type_filter_val, author=author_q)
                
                if abort_requested:
                    root.after(0, lambda: reset_gui_state(run_button, entry))
                    root.after(0, reset_inputs)
                    return
                    
                root.after(0, lambda: display_research_results(results, query, page))
            except Exception as e:
                root.after(0, lambda err=e: log_area.insert('end', f"\n[ERROR] Research fetch failed: {err}\n"))
                root.after(0, lambda: log_area.see('end'))
                root.after(0, lambda: status_label.config(text="Failed to fetch research results.", fg="#F44336"))
                root.after(0, lambda: reset_gui_state(run_button, entry))
                root.after(0, reset_inputs)
            finally:
                running_event.clear()
                
        t = threading.Thread(target=fetch_thread, args=(type_val, title_val, author_val))
        t.daemon = True
        t.start()
        
    def run_thread(identifier):
        try:
            run_pipeline_bg(identifier, status_label, log_area, run_button, entry, root)
        finally:
            running_event.clear()
            
    def handle_button_click():
        global is_running, abort_requested, current_mode
        
        if not is_running:
            # START ACTION
            identifier = entry.get().strip()
            if not identifier:
                status_label.config(text="Please enter a search query first!", fg="#F44336")
                return
                
            if current_mode in ("Research", "Author"):
                load_research_page(identifier, 1)
                return
            else:
                # Direct Download Mode
                is_running = True
                abort_requested = False
                
                # Disable input entry box
                entry.config(state='disabled')
                
                # Update button to "Stop Research" with warning/red styles
                run_button.config(text="Stop Research", bg="#D32F2F", activebackground="#EF5350")
                status_label.config(text="Initializing...", fg="#A855F7")
                
                running_event.set()
                animate_loading(status_label, running_event)
                
                # Clear log area
                log_area.delete('1.0', 'end')
                
                t = threading.Thread(target=run_thread, args=(identifier,))
                t.daemon = True
                t.start()
        else:
            # STOP ACTION
            abort_requested = True
            status_label.config(text="Stopping...", fg="#FF9800")
            run_button.config(state='disabled')
        
    # Center Download/Stop Button
    btn_frame = tk.Frame(card_frame, bg="#1A1625")
    btn_frame.pack(anchor='center', pady=(10, 0))
    
    run_button = tk.Button(btn_frame, text="Download Document", bg="#8B5CF6", fg="#FFFFFF", activebackground="#A78BFA", activeforeground="#FFFFFF", disabledforeground="#8E8A9F", bd=0, font=('Segoe UI Semibold', 10), padx=25, pady=8, cursor="hand2", command=handle_button_click)
    run_button.pack(anchor='center')
    
    # Style button hover bindings
    def on_btn_enter(e):
        global is_running
        if run_button['state'] != 'disabled':
            if is_running:
                run_button['bg'] = '#EF5350' # Hover state for Stop button (brighter red)
            else:
                run_button['bg'] = '#A78BFA' # Hover state for Download button (brighter purple)
                
    def on_btn_leave(e):
        global is_running
        if run_button['state'] != 'disabled':
            if is_running:
                run_button['bg'] = '#D32F2F' # Idle state for Stop button
            else:
                run_button['bg'] = '#8B5CF6' # Idle state for Download button
            
    run_button.bind("<Enter>", on_btn_enter)
    run_button.bind("<Leave>", on_btn_leave)
    
    # Handle enter key press (only trigger search if not running)
    def on_enter_key(e):
        global is_running
        if not is_running:
            handle_button_click()
    entry.bind("<Return>", on_enter_key)
    
    # ── Algeria-only Support Panel ────────────────────────────────────────────
    # Built but hidden; revealed if country detection confirms Algeria (DZ)
    support_frame = tk.Frame(root, bg="#120F1E", pady=0)
    
    # Thin accent separator
    sep = tk.Frame(support_frame, bg="#8B5CF6", height=1)
    sep.pack(fill='x')
    
    inner = tk.Frame(support_frame, bg="#120F1E", padx=30, pady=12)
    inner.pack(fill='x')
    
    # Left: Services offered (with premium, highly attractive freelance copywriting)
    services_frame = tk.Frame(inner, bg="#120F1E")
    services_frame.pack(side='left', fill='both', expand=True, padx=(0, 20))
    
    services_title = tk.Label(services_frame, text="🚀  Besoin d'un Expert Tech ?",
                               bg="#120F1E", fg="#A855F7", font=('Segoe UI Semibold', 9))
    services_title.pack(anchor='w', pady=(0, 6))
    
    services = [
        ("🌐", "Applications Web Modernes"),
        ("🛒", "E-Commerce & Vitrines Pro"),
        ("📡", "Projets IoT & Domotique"),
    ]
    for icon, label in services:
        row = tk.Frame(services_frame, bg="#120F1E")
        row.pack(anchor='w', pady=1)
        tk.Label(row, text=icon, bg="#120F1E", fg="#C084FC", font=('Segoe UI', 8), width=3, anchor='w').pack(side='left')
        tk.Label(row, text=label, bg="#120F1E", fg="#D1D5DB",
                 font=('Segoe UI', 8)).pack(side='left')
                 
    # Center: Contact & Collaboration (Clean 2nd column)
    contact_frame = tk.Frame(inner, bg="#120F1E")
    contact_frame.pack(side='left', fill='both', expand=True, padx=(20, 20))
    
    contact_title = tk.Label(contact_frame, text="📬  Collaborons Ensemble !",
                             bg="#120F1E", fg="#A855F7", font=('Segoe UI Semibold', 9))
    contact_title.pack(anchor='w', pady=(0, 6))
    
    contacts = [
        ("💬", "WhatsApp : 0661342180"),
        ("📧", "yazid.youcef@gmail.com"),
        ("📍", "Batna, Algérie")
    ]
    for icon, label in contacts:
        row = tk.Frame(contact_frame, bg="#120F1E")
        row.pack(anchor='w', pady=1)
        tk.Label(row, text=icon, bg="#120F1E", fg="#C084FC", font=('Segoe UI', 8), width=3, anchor='w').pack(side='left')
        tk.Label(row, text=label, bg="#120F1E", fg="#D1D5DB",
                 font=('Segoe UI', 8), wraplength=220, justify='left').pack(side='left')
                 
    # Right: Buy Me a Coffee button (Supportive & Inspiring copy)
    bmc_frame = tk.Frame(inner, bg="#120F1E")
    bmc_frame.pack(side='left', fill='both', expand=True, padx=(20, 0))
    
    def open_bmc():
        import webbrowser
        webbrowser.open("https://buymeacoffee.com/yazidyoucef")
        
    # Title for coffee column
    coffee_title = tk.Label(bmc_frame, text="☕  Soutenir mon Travail",
                            bg="#120F1E", fg="#A855F7", font=('Segoe UI Semibold', 9))
    coffee_title.pack(anchor='center', pady=(0, 6))
    
    bmc_btn = tk.Button(
        bmc_frame,
        text="☕  Buy Me a Coffee",
        bg="#FBBF24",
        fg="#1C1410",
        activebackground="#F59E0B",
        activeforeground="#1C1410",
        bd=0,
        font=('Segoe UI Semibold', 9),
        padx=14,
        pady=6,
        cursor="hand2",
        command=open_bmc
    )
    bmc_btn.pack(anchor='center')
    
    tk.Label(bmc_frame, text="Encourager l'innovation locale 🇩🇿",
             bg="#120F1E", fg="#6B7280", font=('Segoe UI', 7, 'italic')).pack(pady=(4, 0))
    
    def check_country_bg():
        """Background thread: reveal support panel only for Algerian users."""
        country = get_user_country()
        if country == 'DZ':
            root.after(0, lambda: support_frame.pack(fill='x', side='bottom'))
    
    t_geo = threading.Thread(target=check_country_bg)
    t_geo.daemon = True
    t_geo.start()
    # ─────────────────────────────────────────────────────────────────────────
    
    root.mainloop()


# --- Main Orchestration Entry Point ---
if __name__ == "__main__":
    # If arguments are passed, run in headless CLI mode. Otherwise, launch GUI.
    if len(sys.argv) > 1:
        discovered_urls.clear()
        target_doi = None
        target_title = None

        first_arg = sys.argv[1].strip()
        # Heuristic: DOIs typically start with "10."
        if first_arg.startswith("10."):
            target_doi = first_arg
            target_title = sys.argv[2] if len(sys.argv) > 2 else None
        else:
            target_title = first_arg

        if not target_doi and target_title:
            print(f"Beginning Processing Pipeline for Target Document (Title: '{target_title}')...")
            # Attempt to resolve the title to a DOI via Crossref
            target_doi = resolve_title_to_doi(target_title)
        else:
            print(f"Beginning Processing Pipeline for Target Document (DOI: {target_doi})...")

        # Run through pipeline until one layer successfully finishes downloading
        success = try_unpaywall(target_doi)
        
        if not success:
            success = try_scihub(target_doi)
            
        if not success:
            success = try_researchgate(target_doi, target_title)
            
        if success:
            print("\n==============================================")
            print("[PROCESS FINISHED] Document pulled successfully.")
            print("==============================================")
        else:
            # Fallback to browser launching in CLI mode if any URLs were discovered
            valid_fallbacks = sorted(discovered_urls, key=lambda x: x[1])
            if valid_fallbacks:
                best_url, rank, label = valid_fallbacks[0]
                print(f"\n[WARNING] Programmatic binary download failed (likely due to Cloudflare protection).")
                print(f"[INFO] Launching the best discovered URL in your default web browser ({label}):")
                print(f"       {best_url}")
                try:
                    import webbrowser
                    webbrowser.open(best_url)
                    print("\n==============================================")
                    print("[PROCESS FINISHED] Document opened in web browser.")
                    print("==============================================")
                except Exception as browser_err:
                    print(f"[ERROR] Failed to launch web browser: {browser_err}")
                    print("\n==============================================")
                    print("[PROCESS FAILED] File could not be retrieved from active channels.")
                    print("==============================================")
            else:
                print("\n==============================================")
                print("[PROCESS FAILED] File could not be retrieved from active channels.")
                print("==============================================")
    else:
        # Launch beautiful GUI
        launch_gui()