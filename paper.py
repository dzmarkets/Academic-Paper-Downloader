import urllib.request
import urllib.parse
import urllib.error
import json
import re
import os
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import threading

GUI_MODE = False

def open_in_explorer(filepath):
    """Open the directory containing the file in Windows Explorer and select the file."""
    try:
        import subprocess
        abs_path = os.path.abspath(filepath).replace('/', '\\')
        if os.path.exists(abs_path):
            print(f"[INFO] Opening explorer to highlight file: {abs_path}")
            def run_explorer():
                extra_kwargs = {'creationflags': 0x08000000} if os.name == 'nt' else {}
                subprocess.run(f'explorer /select,"{abs_path}"', shell=True, **extra_kwargs)
            t = threading.Thread(target=run_explorer)
            t.daemon = True
            t.start()
    except Exception as e:
        print(f"[WARNING] Failed to open explorer: {e}")


# ---------------------------------------------------------------------------
# PyInstaller-aware path resolution
# ---------------------------------------------------------------------------
def get_app_dir():
    """Return the directory that contains the running script / executable.

    When packaged with PyInstaller (sys.frozen is set) the interpreter lives
    inside a temporary _MEI... folder, so we must use sys.executable instead
    of __file__ to locate the real application directory.
    """
    if getattr(sys, 'frozen', False):
        # Running as a PyInstaller bundle — use the .exe location
        return os.path.dirname(os.path.abspath(sys.executable))
    # Running as a plain Python script
    return os.path.dirname(os.path.abspath(__file__))


def get_documents_dir():
    """Locate the user's Windows Documents directory dynamically."""
    try:
        import ctypes
        from ctypes import wintypes
        buf = ctypes.create_unicode_buffer(wintypes.MAX_PATH)
        # CSIDL_PERSONAL = 5 is the CSIDL for "My Documents" (handles OneDrive redirects cleanly!)
        ctypes.windll.shell32.SHGetFolderPathW(None, 5, None, 0, buf)
        if buf.value:
            return buf.value
    except Exception:
        pass
    # Fallback to standard home directory Documents folder
    return os.path.join(os.path.expanduser('~'), 'Documents')


# Mapping from document category → descriptive folder name
_FOLDER_FOR_CATEGORY = {
    "book":   "Books",
    "thesis": "Theses",
    "paper":  "Papers",
    "others": "Others",
}


def get_download_dir(category="paper"):
    """Return (and create if necessary) the Downloads subfolder inside user's Documents.

    Parameters
    ----------
    category : str
        One of ``"paper"``, ``"book"``, ``"thesis"``, or ``"others"``.
        Anything else falls back to ``"Others"``.

    Returns
    -------
    str
        Absolute path to the category subfolder inside Documents, guaranteed to exist.
    """
    folder_name = _FOLDER_FOR_CATEGORY.get(category.lower(), "Others")
    base_dir = os.path.join(get_documents_dir(), "Academic Paper Downloader")
    path = os.path.join(base_dir, folder_name)
    os.makedirs(path, exist_ok=True)
    return path


# ---------------------------------------------------------------------------
# Define target paper metadata
# ---------------------------------------------------------------------------
VERSION = "2.4.1.0"
DOI = "10.1145/3375633"
TITLE = "Certifying compilation with de Bruijn indices"  # Used if DOI fails or for ResearchGate search
abort_requested = False
discovered_urls = []
dl_link_lbl = None


# Configuration
UNPAYWALL_EMAIL = "researcher@domain.com"
SCIHUB_DOMAINS = [
    "https://sci-hub.se",
    "https://sci-hub.st",
    "https://sci-hub.ru",
    "https://sci-hub.africa",
    "https://sci-net.xyz",
    "https://sci-hubse.com",
    "https://www.sci-hub.pub"
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


def check_for_updates():
    """Check GitHub for the latest release version of Academic Paper Downloader."""
    url = "https://api.github.com/repos/dzmarkets/Academic-Paper-Downloader/releases/latest"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            latest_version = data.get("tag_name", "").strip().lstrip("v")
            changelog = data.get("body", "")
            # Find direct download link for exe if available, else standard HTML release url
            html_url = data.get("html_url", "https://github.com/dzmarkets/Academic-Paper-Downloader/releases/latest")
            download_url = html_url
            if "assets" in data:
                setup_asset = None
                for asset in data["assets"]:
                    name = asset.get("name", "")
                    if name.endswith("_Setup.exe") or "setup" in name.lower():
                        setup_asset = asset.get("browser_download_url")
                        break
                
                if setup_asset:
                    download_url = setup_asset
                else:
                    for asset in data["assets"]:
                        if asset.get("name", "").endswith(".exe"):
                            download_url = asset.get("browser_download_url", html_url)
                            break
            return latest_version, changelog, download_url
    except urllib.error.HTTPError as e:
        if e.code == 404:
            # 404 means no releases are published yet!
            print("[INFO] No releases found on GitHub. Assuming up-to-date.")
            return VERSION, "No releases published yet on GitHub.", "https://github.com/dzmarkets/Academic-Paper-Downloader"
        print(f"[WARNING] Update check HTTP error: {e}")
        return None, None, None
    except Exception as e:
        print(f"[WARNING] Update check failed: {e}")
        return None, None, None


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
        download_matches += re.findall(r'href="([^"]*?publication/\d+_[^"]+/links/[a-f0-9]+/[^"]+)"', page_source)
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


def download_file(url, filename, referer=None, cookie=None, category="paper"):
    """Helper to perform standard binary file downloads with PDF validation.

    Parameters
    ----------
    url : str
        Direct download URL.
    filename : str
        Destination filename (basename only) or absolute path.
    referer : str, optional
        Referer header value.
    cookie : str, optional
        Cookie header value.
    category : str, optional
        Document category used to select the output subfolder.
        One of ``"paper"`` (default), ``"book"``, or ``"thesis"``.
    """
    global abort_requested
    if abort_requested:
        print("[INFO] Download aborted by user.")
        return False

    # Route downloads to the correct named subfolder next to the .exe / script
    downloads_dir = get_download_dir(category)
    if not os.path.isabs(filename):
        filename = os.path.join(downloads_dir, filename)

    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
    except Exception as e:
        print(f"[WARNING] Failed to create parent directory: {e}. Falling back to app root.")
        filename = os.path.join(get_app_dir(), os.path.basename(filename))

    is_pdf = filename.lower().endswith('.pdf')
    content = None
    
    # Build progressive header sets to try (some publishers require specific Accept/Referer combos)
    header_attempts = [
        # Attempt 1: Standard browser headers
        {
            'User-Agent': HEADERS['User-Agent'],
            'Accept': 'application/pdf,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            **(({'Referer': referer}) if referer else {}),
            **(({'Cookie': cookie}) if cookie else {}),
        },
        # Attempt 2: Academic publisher-friendly headers (OUP, Springer, Elsevier)
        {
            'User-Agent': HEADERS['User-Agent'],
            'Accept': 'application/pdf,application/x-pdf,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            **(({'Referer': referer}) if referer else {}),
            **(({'Cookie': cookie}) if cookie else {}),
        },
    ]
    
    for attempt_num, hdrs in enumerate(header_attempts, 1):
        try:
            req = urllib.request.Request(url, headers=hdrs)
            with urllib.request.urlopen(req, timeout=25) as response:
                chunks = []
                while True:
                    if abort_requested:
                        print("[INFO] Download aborted by user.")
                        return False
                    chunk = response.read(65536)
                    if not chunk:
                        break
                    chunks.append(chunk)
                content = b"".join(chunks)
            # Validate immediately
            if is_pdf and content and not content.startswith(b'%PDF'):
                content = None  # not a real PDF, try next
                continue
            break  # success
        except Exception as e:
            if attempt_num == 1:
                print(f"[WARNING] urllib download failed: {e}. Trying system curl fallback...")
            content = None

    # Fallback to system curl command if urllib failed
    if not content or (is_pdf and not content.startswith(b'%PDF')):
        try:
            import subprocess
            print(f"[INFO] Bypassing via native system curl...")
            cmd = ["curl", "-s", "-L",
                   "-H", f"User-Agent: {HEADERS['User-Agent']}",
                   "-H", "Accept: application/pdf,*/*;q=0.8"]
            if referer:
                cmd += ["-H", f"Referer: {referer}"]
            if cookie:
                cmd += ["-H", f"Cookie: {cookie}"]
            cmd += ["-o", filename, url]
            extra_kwargs = {'creationflags': 0x08000000} if os.name == 'nt' else {}
            res = subprocess.run(cmd, capture_output=True, **extra_kwargs)
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
    if GUI_MODE:
        open_in_explorer(filename)
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
    global abort_requested
    if abort_requested:
        return []
    if not query:
        return []
    # Detect exact match phrase in quotes (Google-like intelligent search)
    stripped = query.strip()
    is_exact = (stripped.startswith('"') and stripped.endswith('"')) or (stripped.startswith("'") and stripped.endswith("'"))
    exact_phrase = stripped.strip('"').strip("'").strip() if is_exact else None
    
    clean_query = stripped
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
        url += "&filter=type:journal-article,type:proceedings-article,type:posted-content"
    elif type_filter == "Books":
        url += "&filter=type:book"
    try:
        if abort_requested:
            return []
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as response:
            if abort_requested:
                return []
            data = json.loads(response.read().decode())
        
        items = data.get('message', {}).get('items', [])
        filtered_items = []
        for item in items:
            # If type_filter is Papers, only keep journal-article, proceedings-article, and posted-content (preprints)
            if type_filter == "Papers":
                allowed = ("journal-article", "proceedings-article", "posted-content")
                if item.get('type') not in allowed:
                    continue

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
            
            # Exact phrase check (Google-like intelligent search)
            if exact_phrase:
                phrase = exact_phrase.lower()
                if (phrase not in title.lower()) and (phrase not in authors_str.lower()):
                    continue
            
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


def search_google_scholar(query, offset=0, rows=5):
    """Query Google Scholar index via a robust, CAPTCHA-free DuckDuckGo fallback scraper.
    
    This retrieves high-quality academic titles, PDF links, authors, and journal names.
    """
    global abort_requested
    if abort_requested:
        return []
    if not query:
        return []
    
    # Check exact phrase match in quotes (Google-like intelligent search)
    stripped = query.strip()
    is_exact = (stripped.startswith('"') and stripped.endswith('"')) or (stripped.startswith("'") and stripped.endswith("'"))
    exact_phrase = stripped.strip('"').strip("'").strip() if is_exact else None
    
    clean_query = stripped
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(clean_query)}"
    print(f"[INFO] Querying Google Scholar (via DuckDuckGo proxy): {url}")
    
    try:
        html = fetch_html_resilient(url)
        if not html:
            return []
            
        blocks = re.split(r'<div class="[^"]*result__body[^"]*">', html)
        results = []
        
        for block in blocks[1:]:
            # Extract link and title
            a_match = re.search(r'<a[^>]*class="[^"]*result__a[^"]*"[^>]*>(.*?)</a>', block, re.DOTALL)
            if not a_match:
                continue
                
            title = re.sub('<[^<]+?>', '', a_match.group(1)).strip()
            
            href_match = re.search(r'href="([^"]+)"', a_match.group(0))
            if not href_match:
                continue
                
            raw_url = href_match.group(1)
            url_match = re.search(r'uddg=(https?%3A%2F%2F[^&"]*)', raw_url)
            actual_url = urllib.parse.unquote(url_match.group(1)) if url_match else raw_url
            if actual_url.startswith('//'):
                actual_url = 'https:' + actual_url
                
            # Skip profile pages, university directories, members lists, department lists, and search catalog result pages
            url_lower = actual_url.lower()
            title_lower = title.lower()
            
            is_profile = (
                "/profile/" in url_lower or
                "/institution/" in url_lower or
                "/members" in url_lower or
                "members" in title_lower or
                "dpartement" in title_lower or
                "département" in title_lower or
                "department" in title_lower or
                "faculty" in url_lower or
                "faculty" in title_lower or
                "central library" in title_lower or
                "catalogue en ligne" in title_lower or
                "index.php?lvl=more_results" in url_lower or
                ("search" in url_lower and "catalog" in url_lower) or
                "univ-" in url_lower or
                ("university" in title_lower and ("members" in title_lower or "profile" in title_lower))
            )
            if is_profile:
                continue
                
            # Skip non-academic / software / documentation / social domains —
            # only papers from academic repositories should appear in search results
            _NON_ACADEMIC_DOMAINS = (
                "github.com",
                "github.io",
                "readthedocs.io",
                "readthedocs.org",
                "pypi.org",
                "stackoverflow.com",
                "stackexchange.com",
                "reddit.com",
                "twitter.com",
                "x.com",
                "linkedin.com",
                "facebook.com",
                "youtube.com",
                "medium.com",
                "substack.com",
                "wikipedia.org",
                "conda-forge.org",
                "anaconda.org",
                "bioconductor.org",
                "npmjs.com",
                "cran.r-project.org",
                "sourceforge.net",
                "gitlab.com",
                "bitbucket.org",
                "docs.python.org",
                "docs.scipy.org",
                "galaxyproject.org",
                "snakemake.readthedocs.io",
            )
            if any(nd in url_lower for nd in _NON_ACADEMIC_DOMAINS):
                print(f"[INFO] Skipping non-academic URL: {actual_url}")
                continue
                
            # Snippet
            snippet_match = re.search(r'<a[^>]*class="[^"]*result__snippet[^"]*"[^>]*>(.*?)</a>', block, re.DOTALL)
            snippet = re.sub('<[^<]+?>', '', snippet_match.group(1)).strip() if snippet_match else ""
            
            # Exact phrase check (Google-like intelligent search)
            if exact_phrase:
                phrase = exact_phrase.lower()
                if (phrase not in title.lower()) and (phrase not in snippet.lower()):
                    continue
            
            authors = "Unknown Authors"
            journal = "Web Resource"
            year = "n.d."
            
            is_pdf = actual_url.lower().split('?')[0].endswith('.pdf') or 'pdf' in actual_url.lower()
            
            if "researchgate.net" in actual_url:
                journal = "ResearchGate Profile"
                if " | " in title:
                    authors = title.split(" | ")[0]
                elif " -" in title:
                    authors = title.split(" -")[0]
            elif "scholar.google.com" in actual_url:
                journal = "Google Scholar Citations"
            else:
                parsed = urllib.parse.urlparse(actual_url)
                journal = parsed.netloc.replace("www.", "")
                
            year_match = re.search(r'\b(19\d{2}|20\d{2})\b', snippet + " " + title)
            if year_match:
                year = year_match.group(1)
                
            if "Abstract" in snippet:
                before_abstract = snippet.split("Abstract")[0].strip()
                before_abstract = re.sub(r'[\.\-\s,]+$', '', before_abstract)
                if len(before_abstract) > 3 and len(before_abstract) < 150:
                    authors = before_abstract
            elif "Authors:" in snippet:
                authors_part = snippet.split("Authors:")[1].strip()
                authors_part = re.split(r'\b(download|published|abstract|index)\b', authors_part, flags=re.IGNORECASE)[0].strip()
                authors_part = re.sub(r'[\.\-\s,]+$', '', authors_part)
                if len(authors_part) > 3 and len(authors_part) < 150:
                    authors = authors_part
            
            if authors == "Unknown Authors" and exact_phrase:
                authors = exact_phrase
            
            # Skip results that still have unknown authors after all extraction
            if authors == "Unknown Authors":
                continue
                
            results.append({
                'title': title,
                'doi': actual_url,  # Direct download will resolve URL
                'authors': authors,
                'year': year,
                'journal': journal,
                'is_oa': is_pdf
            })
            
        return results[offset : offset + rows]
    except Exception as e:
        print(f"[WARNING] Google Scholar search failed: {e}")
        return []


def search_openlibrary(query, author="", offset=0, rows=5):
    """Query OpenLibrary API for books — much more accurate than Crossref for book searches.
    
    Returns books with a `can_download` field: True only when we have a viable
    programmatic download path (Internet Archive ID → direct PDF or CDL image scrape,
    or a known Taylor & Francis DOI prefix → T&F API). Books with only isbn:/ol:
    identifiers cannot be downloaded automatically and are excluded from results.
    """
    if not query:
        return []
    clean_query = query.strip().strip('"').strip("'").strip('[').strip(']').strip()
    clean_author = author.strip().strip('"').strip("'") if author else ""
    
    params = f"title={urllib.parse.quote(clean_query)}"
    if clean_author:
        params += f"&author={urllib.parse.quote(clean_author)}"
    params += "&fields=title,author_name,first_publish_year,isbn,publisher,key,ia&limit=100"
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
            can_download = False
            if ia_ids:
                doi = f"ia:{ia_ids[0]}"
                can_download = True   # Internet Archive: direct PDF or CDL image scrape
            elif isbns:
                doi = f"isbn:{isbns[0]}"
                can_download = False  # No direct programmatic download path
            elif ol_key:
                doi = f"ol:{ol_key.replace('/works/', '')}"
                can_download = False  # No direct programmatic download path
            
            # Skip entries with no identifier at all
            if not doi:
                continue
                
            # Only include books we can actually download
            if not can_download:
                continue
                
            filtered.append({
                'title': title,
                'doi': doi,
                'ol_key': ol_key,
                'authors': authors_str,
                'year': year,
                'journal': publisher_str,
                'is_oa': can_download,
                'can_download': can_download,
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
                filter_parts.append("type:article|preprint|review")
            elif type_filter == "Books":
                filter_parts.append("type:book|book-chapter")
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


def search_openalex_keyword(query, offset=0, rows=5, type_filter="All"):
    """Search OpenAlex for works matching a keyword query."""
    if not query:
        return []
    
    page = (offset // rows) + 1
    oa_headers = {**HEADERS, 'User-Agent': f'PaperDownloader/2.1 (mailto:{UNPAYWALL_EMAIL})'}
    
    filter_parts = []
    if type_filter == "Papers":
        filter_parts.append("type:article|preprint|review")
    elif type_filter == "Books":
        filter_parts.append("type:book|book-chapter")
        
    filter_str = ""
    if filter_parts:
        filter_str = f"&filter={urllib.parse.quote(','.join(filter_parts))}"
        
    url = (f"https://api.openalex.org/works"
           f"?search={urllib.parse.quote(query)}"
           f"&page={page}&per_page={rows}"
           f"{filter_str}")
           
    results = []
    try:
        req = urllib.request.Request(url, headers=oa_headers)
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode())
        works = data.get('results', [])
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
        print(f"[WARNING] OpenAlex keyword search failed: {e}")
        
    return results


def fetch_html_resilient(url):
    """Fetch HTML content from a URL using urllib first, falling back to native system curl on block/failure."""
    global abort_requested
    if abort_requested:
        return ""
    try:
        if abort_requested:
            return ""
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=12) as response:
            if abort_requested:
                return ""
            return response.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"[WARNING] urllib fetch failed: {e}. Trying native system curl fallback...")
        try:
            import subprocess
            cmd = ["curl", "-s", "-L", "-H", f"User-Agent: {HEADERS['User-Agent']}", "-H", f"Accept: {HEADERS['Accept']}", url]
            extra_kwargs = {'creationflags': 0x08000000} if os.name == 'nt' else {}
            res = subprocess.run(cmd, capture_output=True, **extra_kwargs)
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
        if GUI_MODE:
            open_in_explorer(pdf_path)
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
        downloads_dir = get_download_dir("book")
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
        if GUI_MODE:
            open_in_explorer(pdf_path)
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
        success = download_file(ia_url, filename, category="book")
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
                    success = download_file(target_url, filename, category="book")
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
                    success = download_file(ia_url, filename, category="book")
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
                    success = download_file(ia_url, filename, category="book")
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


def try_ssrn(doi, title):
    """Strategy: Download papers from SSRN (Social Science Research Network).
    
    SSRN DOIs follow the pattern: 10.2139/ssrn.{abstract_id}
    Direct PDF download URL: https://download.ssrn.com/sol3/papers.cfm?abstract_id={id}&download=yes
    Fallback: scrape the abstract page for the embedded PDF link.
    """
    if not doi:
        return False
    
    abstract_id = None
    if doi.startswith("10.2139/ssrn."):
        abstract_id = doi.split("10.2139/ssrn.", 1)[1].strip()
    elif "ssrn.com" in doi:
        # Handle direct SSRN URL passed as DOI
        m = re.search(r'abstract[_=]id[=_](\d+)', doi)
        if m:
            abstract_id = m.group(1)
    
    if not abstract_id:
        return False
    
    print("\n--- [STRATEGY] Querying SSRN (Social Science Research Network) ---")
    print(f"[INFO] SSRN Abstract ID: {abstract_id}")
    
    abstract_page = f"https://papers.ssrn.com/sol3/papers.cfm?abstract_id={abstract_id}"
    register_discovered_url(abstract_page, "SSRN Abstract Page")
    
    # Strategy 1: Direct download endpoint
    direct_url = f"https://download.ssrn.com/sol3/papers.cfm?abstract_id={abstract_id}&download=yes"
    filename = f"SSRN_{abstract_id}_{clean_filename(title) if title else abstract_id}.pdf"
    print(f"[INFO] Trying SSRN direct download: {direct_url}")
    register_discovered_url(direct_url, "SSRN Direct PDF Download")
    if download_file(direct_url, filename, referer=abstract_page):
        return True
    
    # Strategy 2: Scrape abstract page for embedded PDF URL
    print(f"[INFO] Scraping SSRN abstract page for PDF link: {abstract_page}")
    try:
        html = fetch_html_resilient(abstract_page)
        if html:
            # SSRN embeds links like: href="/sol3/Delivery.cfm/.../...pdf?..."
            pdf_links = re.findall(r'href=["\']([^"\']*\.pdf[^"\']*)["\']', html, re.IGNORECASE)
            pdf_links += re.findall(r'href=["\']([^"\']*delivery\.cfm[^"\']*)["\']', html, re.IGNORECASE)
            for link in pdf_links:
                if link.startswith('/'):
                    link = 'https://papers.ssrn.com' + link
                elif not link.startswith('http'):
                    link = 'https://papers.ssrn.com/' + link
                link = link.replace('&amp;', '&')
                print(f"[INFO] SSRN PDF candidate: {link}")
                register_discovered_url(link, "SSRN PDF Link")
                if download_file(link, filename, referer=abstract_page):
                    return True
    except Exception as e:
        print(f"[WARNING] SSRN page scraping failed: {e}")
    
    return False


def try_astesj(doi, title):
    """Strategy: Download papers from ASTESJ (open-access engineering journal).
    
    ASTESJ DOIs: 10.25046/aj{volume}{issue}{sequence}
    Article page: https://doi.org/{doi}  →  redirects to astesj.com article page
    The article page contains a direct PDF download link.
    """
    if not doi:
        return False
    if not doi.startswith("10.25046/"):
        return False
    
    print("\n--- [STRATEGY] Querying ASTESJ (Advances in Science, Technology and Engineering Systems) ---")
    
    # Resolve DOI to get article page URL
    article_url = f"https://doi.org/{doi}"
    print(f"[INFO] Resolving ASTESJ DOI: {article_url}")
    register_discovered_url(f"https://www.astesj.com/", "ASTESJ Journal")
    
    try:
        req = urllib.request.Request(article_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            final_url = resp.geturl()
            html = resp.read().decode('utf-8', errors='ignore')
        
        print(f"[INFO] ASTESJ article page: {final_url}")
        register_discovered_url(final_url, "ASTESJ Article Page")
        
        # Extract direct PDF link from article page
        # Pattern: href=".../ASTESJ_XXXX/XX.pdf" or similar
        pdf_links = re.findall(r'href=["\']([^"\']*\.pdf[^"\']*)["\']', html, re.IGNORECASE)
        
        for link in pdf_links:
            if not link.startswith('http'):
                if link.startswith('/'):
                    base = 'https://www.astesj.com'
                    link = base + link
                else:
                    link = urllib.parse.urljoin(final_url, link)
            link = link.replace('&amp;', '&')
            print(f"[INFO] ASTESJ PDF candidate: {link}")
            register_discovered_url(link, "ASTESJ PDF")
            filename = f"ASTESJ_{clean_filename(title if title else doi.replace('/', '_'))}.pdf"
            if download_file(link, filename, referer=final_url):
                return True
                
    except Exception as e:
        print(f"[WARNING] ASTESJ resolution failed: {e}")
    
    return False


def try_core(doi, title):
    """Strategy: Download open access papers from CORE (core.ac.uk).
    
    We query the login-free CORE search engine for the DOI:
        https://core.ac.uk/search?q=doi:{doi}
    And parse the search page HTML for the article output ID:
        e.g. href="/outputs/{id}"
    Once resolved, the direct login-free PDF download link is:
        https://core.ac.uk/download/{id}.pdf
    """
    if not doi:
        return False
    if doi.startswith("http://") or doi.startswith("https://"):
        return False
        
    print("\n--- [STRATEGY] Querying CORE (core.ac.uk) Open Access ---")
    search_page_url = f"https://core.ac.uk/search?q=doi:{urllib.parse.quote(doi)}"
    register_discovered_url(search_page_url, "CORE Search Page")
    
    try:
        html = fetch_html_resilient(search_page_url)
        if not html:
            print("[INFO] CORE returned empty search results.")
            return False
            
        # Look for article output paths like /outputs/82976757 or similar
        output_ids = re.findall(r'/outputs/(\d+)', html)
        if not output_ids:
            # Fallback search for any numbers inside outputs paths in text
            output_ids = re.findall(r'outputs/(\d+)', html)
            
        if output_ids:
            # Take the first/best match
            core_id = output_ids[0]
            download_url = f"https://core.ac.uk/download/{core_id}.pdf"
            print(f"[INFO] Discovered CORE Article ID: {core_id} → {download_url}")
            register_discovered_url(download_url, "CORE PDF Download")
            filename = f"CORE_{clean_filename(title if title else doi.replace('/', '_'))}.pdf"
            if download_file(download_url, filename, referer=search_page_url):
                return True
        else:
            print("[INFO] CORE indexes do not contain an open-access copy of this paper.")
    except Exception as e:
        print(f"[WARNING] CORE lookup failed: {e}")
        
    return False


def try_libgen(doi, title):
    """Strategy: Download documents from Library Genesis (libgen.la).
    
    We query the login-free search engine:
        https://libgen.la/index.php?req={doi}
    And parse the search results HTML to extract MD5 hashes.
    Once resolved, we query the download page:
        https://libgen.la/get.php?md5={md5}
    And parse its HTML to extract the direct PDF/EPUB attachment download link.
    """
    if not doi:
        return False
    if doi.startswith("http://") or doi.startswith("https://"):
        return False
        
    print("\n--- [STRATEGY] Querying Library Genesis (libgen.la) ---")
    search_url = f"https://libgen.la/index.php?req={urllib.parse.quote(doi)}"
    register_discovered_url(search_url, "LibGen Search Page")
    
    try:
        html = fetch_html_resilient(search_url)
        if not html:
            print("[INFO] LibGen search returned empty content.")
            return False
            
        # Parse MD5 values from links like get.php?md5=... or ads.php?md5=...
        md5_list = re.findall(r'md5=([a-fA-F0-9]{32})', html)
        md5_list = list(set(md5_list)) # deduplicate
        
        if md5_list:
            md5 = md5_list[0]
            download_landing_page = f"https://libgen.la/get.php?md5={md5}"
            print(f"[INFO] Discovered LibGen MD5: {md5} → Resolving download link...")
            register_discovered_url(download_landing_page, "LibGen Direct File Landing Page")
            
            # Fetch the get.php landing page
            landing_html = fetch_html_resilient(download_landing_page)
            if landing_html:
                # Find direct links pointing to attachments or keys, like: href="key=..." or href=".../attachments/..."
                direct_links = re.findall(r'href=["\']([^"\']*(?:key=|attachments/)[^"\']*)["\']', landing_html, re.IGNORECASE)
                direct_links += re.findall(r'href=["\'](get\.php\?[^"\']+)["\']', landing_html, re.IGNORECASE)
                
                # Filter / resolve links
                target_url = None
                for link in direct_links:
                    link = link.replace('&amp;', '&')
                    if not link.startswith('http'):
                        if link.startswith('/'):
                            target_url = 'https://libgen.la' + link
                        else:
                            target_url = 'https://libgen.la/' + link
                    else:
                        target_url = link
                    break # take first match
                    
                if target_url:
                    print(f"[INFO] Discovered direct LibGen attachment link: {target_url}")
                    register_discovered_url(target_url, "LibGen Direct File Download")
                    filename = f"LibGen_{clean_filename(title if title else doi.replace('/', '_'))}.pdf"
                    if download_file(target_url, filename, referer=download_landing_page):
                        return True
        else:
            print("[INFO] Library Genesis mirrors do not index this document.")
    except Exception as e:
        print(f"[WARNING] LibGen lookup failed: {e}")
        
    return False


def try_plos(doi, title):
    """Strategy: Construct direct download link for PLOS (Public Library of Science) journals."""
    if not doi:
        return False
    if doi.startswith("http://") or doi.startswith("https://"):
        return False
        
    # PLOS DOIs always start with 10.1371/
    if not doi.lower().startswith("10.1371/"):
        return False
        
    print("\n--- [STRATEGY] Querying PLOS Journal Direct Link ---")
    download_url = f"https://journals.plos.org/plosone/article/file?id={urllib.parse.quote(doi)}&type=printable"
    register_discovered_url(download_url, "PLOS Printable PDF")
    
    filename = f"PLOS_{clean_filename(title if title else doi.replace('/', '_'))}.pdf"
    print(f"[INFO] Constructing PLOS direct URL: {download_url}")
    if download_file(download_url, filename):
        return True
    return False


def try_biorxiv(doi, title):
    """Strategy: Retrieve preprints from BioRxiv / MedRxiv API and download the PDF."""
    if not doi:
        return False
    if doi.startswith("http://") or doi.startswith("https://"):
        return False
        
    # BioRxiv/MedRxiv DOIs start with 10.1101/
    if not doi.lower().startswith("10.1101/"):
        return False
        
    print("\n--- [STRATEGY] Querying BioRxiv API ---")
    suffix = doi.split("10.1101/", 1)[1].strip()
    
    # Try biorxiv details API first, fall back to medrxiv details API
    collection = []
    for endpoint in ("biorxiv", "medrxiv"):
        query_url = f"https://api.biorxiv.org/details/{endpoint}/{urllib.parse.quote(doi)}"
        try:
            res_text = fetch_html_resilient(query_url)
            if res_text:
                data = json.loads(res_text)
                collection = data.get('collection', [])
                if collection:
                    print(f"[INFO] Found metadata collection via {endpoint} endpoint.")
                    break
        except Exception as e:
            print(f"[WARNING] BioRxiv {endpoint} API query failed: {e}")
            
    register_discovered_url(f"https://www.biorxiv.org/content/{doi}", "BioRxiv Page")
    filename = f"BioRxiv_{clean_filename(title if title else doi.replace('/', '_'))}.pdf"
    
    try:
        if collection:
            # Retrieve version number from latest entry
            latest = collection[-1]
            version = latest.get('version', '1')
            download_url = f"https://www.biorxiv.org/content/10.1101/{suffix}v{version}.full.pdf"
            print(f"[INFO] Discovered BioRxiv PDF URL (v{version}): {download_url}")
            register_discovered_url(download_url, "BioRxiv PDF")
            if download_file(download_url, filename):
                return True
            
            # Fallback to v1 if the guessed version fails
            if version != '1':
                fallback_url = f"https://www.biorxiv.org/content/10.1101/{suffix}v1.full.pdf"
                print(f"[INFO] Trying BioRxiv fallback PDF (v1): {fallback_url}")
                register_discovered_url(fallback_url, "BioRxiv v1 PDF")
                if download_file(fallback_url, filename):
                    return True
        else:
            # Direct construction fallback if API collection is empty
            fallback_url = f"https://www.biorxiv.org/content/10.1101/{suffix}v1.full.pdf"
            print(f"[INFO] No API collection; trying default path: {fallback_url}")
            register_discovered_url(fallback_url, "BioRxiv v1 PDF")
            if download_file(fallback_url, filename):
                return True
    except Exception as e:
        print(f"[WARNING] BioRxiv lookup failed: {e}")
        # Try direct construct fallback on exception
        try:
            fallback_url = f"https://www.biorxiv.org/content/10.1101/{suffix}v1.full.pdf"
            if download_file(fallback_url, filename):
                return True
        except:
            pass
            
    return False


def try_publisher_direct(doi, title, status_label=None):
    """Strategy: Construct direct download link for known open-access publisher DOI prefixes."""
    if not doi:
        return False
    if doi.startswith("http://") or doi.startswith("https://"):
        return False

    doi_lower = doi.lower()
    
    # Define publisher rules mapping DOI prefixes to their direct URL structures
    # and readable names
    rules = [
        # (Prefixes/Keywords, Name, URL Template, Filename Prefix)
        (["10.1007", "10.1186", "10.1134", "10.1057"], "Springer Open / BMC / Pleiades / Palgrave", "https://link.springer.com/content/pdf/{doi}.pdf", "Springer_"),
        (["10.3390"], "MDPI", "https://www.mdpi.com/article/{doi}/pdf", "MDPI_"),
        (["10.3389"], "Frontiers", "https://www.frontiersin.org/articles/{doi}/pdf", "Frontiers_"),
        (["10.1002", "10.1111", "10.22541"], "Wiley (OA)", "https://onlinelibrary.wiley.com/doi/pdf/{doi}", "Wiley_"),
        (["10.1080"], "Taylor & Francis", "https://www.tandfonline.com/doi/pdf/{doi}", "TF_"),
        (["10.1088", "10.3847"], "IOP Science / AAS", "https://iopscience.iop.org/article/{doi}/pdf", "IOP_"),
        (["10.1021"], "ACS (OA)", "https://pubs.acs.org/doi/pdf/{doi}", "ACS_"),
        (["10.1093"], "Oxford Academic", "https://academic.oup.com/doi/pdf/{doi}", "OUP_"),
        (["10.1177"], "Sage (OA)", "https://journals.sagepub.com/doi/pdf/{doi}", "Sage_"),
        (["10.1146"], "Annual Reviews", "https://www.annualreviews.org/doi/pdf/{doi}", "AR_"),
        (["10.1103"], "APS", "https://journals.aps.org/prl/pdf/{doi}", "APS_"),
        (["10.1086"], "University of Chicago Press", "https://www.journals.uchicago.edu/doi/pdf/{doi}", "Chicago_"),
        (["10.1098"], "Royal Society", "https://royalsocietypublishing.org/doi/pdf/{doi}", "Royal_"),
        (["10.1061"], "ASCE", "https://ascelibrary.org/doi/pdf/{doi}", "ASCE_"),
        (["10.1108"], "Emerald", "https://www.emerald.com/insight/content/doi/{doi}/pdf", "Emerald_"),
        (["10.1137"], "SIAM", "https://epubs.siam.org/doi/pdf/{doi}", "SIAM_"),
        (["10.1515"], "De Gruyter", "https://www.degruyter.com/document/doi/{doi}/pdf", "DeGruyter_"),
        (["10.1142"], "World Scientific", "https://www.worldscientific.com/doi/pdf/{doi}", "WorldScientific_"),
        (["10.1089"], "Mary Ann Liebert", "https://www.liebertpub.com/doi/pdf/{doi}", "Liebert_"),
        (["10.1055"], "Georg Thieme", "https://www.thieme-connect.com/products/ejournals/pdf/{doi}.pdf", "Thieme_"),
        (["10.1145"], "ACM", "https://dl.acm.org/doi/pdf/{doi}", "ACM_"),
        (["10.1071"], "CSIRO", "https://www.publish.csiro.au/pdf/{doi}", "CSIRO_"),
        (["10.1152"], "American Physiological Society", "https://journals.physiology.org/doi/pdf/{doi}", "APSPhysio_"),
        (["10.1128"], "American Society for Microbiology", "https://journals.asm.org/doi/pdf/{doi}", "ASM_"),
        (["10.3366"], "Edinburgh University Press", "https://www.euppublishing.com/doi/pdf/{doi}", "EUP_"),
        (["10.1287"], "INFORMS", "https://pubsonline.informs.org/doi/pdf/{doi}", "INFORMS_"),
        (["10.2514"], "AIAA", "https://arc.aiaa.org/doi/pdf/{doi}", "AIAA_"),
    ]
    
    # Handle Nature Nature-based suffixes differently since they use suffix after 10.1038/
    if doi_lower.startswith("10.1038/"):
        suffix = doi.split("10.1038/", 1)[1].strip()
        url = f"https://www.nature.com/articles/{suffix}.pdf"
        name = "Nature"
        filename_prefix = "Nature_"
        
        print(f"\n--- [STRATEGY] Querying {name} Direct Link ---")
        if status_label:
            status_label.config(text=f"Querying {name} Direct...", fg="#00ADB5")
            
        register_discovered_url(url, f"{name} Direct PDF")
        filename = f"{filename_prefix}{clean_filename(title if title else suffix)}.pdf"
        print(f"[INFO] Constructing {name} direct URL: {url}")
        if download_file(url, filename):
            return True
        return False
        
    # Standard prefix rules
    for prefixes, name, url_template, filename_prefix in rules:
        if any(doi_lower.startswith(p + "/") for p in prefixes):
            print(f"\n--- [STRATEGY] Querying {name} Direct Link ---")
            if status_label:
                status_label.config(text=f"Querying {name} Direct...", fg="#00ADB5")
                
            url = url_template.replace("{doi}", doi)
            
            register_discovered_url(url, f"{name} Direct PDF")
            filename = f"{filename_prefix}{clean_filename(title if title else doi.replace('/', '_'))}.pdf"
            print(f"[INFO] Constructing {name} direct URL: {url}")
            if download_file(url, filename):
                return True
            break
            
    return False


def try_zenodo(doi, title):
    """Strategy: Download open access records directly from Zenodo API."""
    if not doi:
        return False
    if doi.startswith("http://") or doi.startswith("https://"):
        return False
        
    print("\n--- [STRATEGY] Querying Zenodo API ---")
    
    # Extract Zenodo Record ID if it's a Zenodo DOI
    record_id = None
    if "zenodo." in doi.lower():
        parts = doi.lower().split("zenodo.", 1)
        if len(parts) > 1:
            m = re.match(r'^(\d+)', parts[1].strip())
            if m:
                record_id = m.group(1)
                
    files = []
    
    # If it is a Zenodo DOI, query the direct record API. Otherwise, query the search API.
    if record_id:
        query_url = f"https://zenodo.org/api/records/{record_id}"
        record_page = f"https://zenodo.org/records/{record_id}"
        register_discovered_url(record_page, "Zenodo Record Page")
        print(f"[INFO] Querying Zenodo Record API: {query_url}")
        try:
            res_text = fetch_html_resilient(query_url)
            if res_text:
                data = json.loads(res_text)
                files = data.get('files', [])
        except Exception as e:
            print(f"[WARNING] Zenodo record lookup failed: {e}")
    else:
        query_url = f"https://zenodo.org/api/records?q=doi:\"{urllib.parse.quote(doi)}\""
        register_discovered_url(query_url, "Zenodo Search Query")
        print(f"[INFO] Querying Zenodo Search API: {query_url}")
        try:
            res_text = fetch_html_resilient(query_url)
            if res_text:
                data = json.loads(res_text)
                hits = data.get('hits', {}).get('hits', [])
                if hits:
                    files = hits[0].get('files', [])
        except Exception as e:
            print(f"[WARNING] Zenodo search query failed: {e}")
            
    if files:
        for f in files:
            # Look for pdf files
            key = f.get('key', '').lower()
            if key.endswith('.pdf') or f.get('type', '') == 'pdf':
                download_url = f.get('links', {}).get('self')
                if download_url:
                    print(f"[INFO] Discovered Zenodo PDF URL: {download_url}")
                    register_discovered_url(download_url, "Zenodo PDF")
                    filename = f"Zenodo_{clean_filename(title if title else doi.replace('/', '_'))}.pdf"
                    if download_file(download_url, filename):
                        return True
        print("[INFO] Zenodo record contains no PDF files.")
    else:
        print("[INFO] Zenodo API returned no record data.")
        
    return False


def try_doaj(doi, title):
    """Strategy: Query DOAJ API for article metadata containing direct fulltext links."""
    if not doi:
        return False
    if doi.startswith("http://") or doi.startswith("https://"):
        return False
        
    print("\n--- [STRATEGY] Querying DOAJ API ---")
    query_url = f"https://doaj.org/api/v2/search/articles/doi:{urllib.parse.quote(doi)}"
    register_discovered_url(query_url, "DOAJ API Query")
    
    try:
        res_text = fetch_html_resilient(query_url)
        if res_text:
            data = json.loads(res_text)
            results = data.get('results', [])
            if results:
                article = results[0]
                bibjson = article.get('bibjson', {})
                links = bibjson.get('link', [])
                
                # Sort links to prioritize direct PDFs first
                sorted_links = []
                for l in links:
                    url = l.get('url', '')
                    content_type = l.get('content_type', '').lower()
                    
                    # Direct PDF check
                    if content_type == 'application/pdf' or url.lower().endswith('.pdf'):
                        sorted_links.insert(0, l)
                    else:
                        sorted_links.append(l)
                        
                for l in sorted_links:
                    download_url = l.get('url')
                    if not download_url:
                        continue
                        
                    content_type = l.get('content_type', '').lower()
                    is_pdf = content_type == 'application/pdf' or download_url.lower().endswith('.pdf')
                    
                    # If it's an MDPI landing page, construct the PDF URL directly
                    if not is_pdf and "mdpi.com" in download_url.lower() and not download_url.lower().endswith('/pdf'):
                        download_url = download_url.rstrip('/') + '/pdf'
                        is_pdf = True
                        
                    print(f"[INFO] DOAJ link candidate: {download_url} (is_pdf={is_pdf})")
                    register_discovered_url(download_url, "DOAJ Link")
                    
                    filename = f"DOAJ_{clean_filename(title if title else doi.replace('/', '_'))}.pdf"
                    if download_file(download_url, filename):
                        return True
            else:
                print("[INFO] DOAJ API returned no results for this DOI.")
    except Exception as e:
        print(f"[WARNING] DOAJ lookup failed: {e}")
        
    return False


def try_semantic_scholar(doi, title):
    """Strategy: Query Semantic Scholar API for open access PDF links."""
    if not doi:
        return False
    if doi.startswith("http://") or doi.startswith("https://"):
        return False
        
    print("\n--- [STRATEGY] Querying Semantic Scholar API ---")
    query_url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{urllib.parse.quote(doi)}?fields=isOpenAccess,openAccessPdf"
    register_discovered_url(f"https://www.semanticscholar.org/paper/{urllib.parse.quote(doi)}", "Semantic Scholar Page")
    
    try:
        res_text = fetch_html_resilient(query_url)
        if res_text:
            data = json.loads(res_text)
            if data.get('isOpenAccess') and data.get('openAccessPdf'):
                download_url = data['openAccessPdf'].get('url')
                if download_url:
                    print(f"[INFO] Discovered Semantic Scholar PDF URL: {download_url}")
                    register_discovered_url(download_url, "Semantic Scholar PDF")
                    filename = f"SemanticScholar_{clean_filename(title if title else doi.replace('/', '_'))}.pdf"
                    if download_file(download_url, filename):
                        return True
            else:
                print("[INFO] Semantic Scholar records indicate paper is not Open Access.")
    except Exception as e:
        # Avoid print-spamming if it's just a 404 (not found in Semantic Scholar)
        if "HTTP Error 404" in str(e):
            print("[INFO] Paper not found in Semantic Scholar index.")
        else:
            print(f"[WARNING] Semantic Scholar lookup failed: {e}")
            
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
            if target_pdf:
                print(f"[INFO] Blocked PDF URL (for manual access): {target_pdf}")
                print("[INFO] Automatically launching web browser to open the ResearchGate direct PDF...")
                try:
                    import webbrowser
                    webbrowser.open(target_pdf)
                except Exception as browser_err:
                    print(f"[WARNING] Failed to launch web browser: {browser_err}")
            return False
            
    except Exception as e:
        print(f"[WARNING] ResearchGate scraping routine failed: {e}")
        print("[TIP] ResearchGate may be prompting a Captcha verification wall against scripts.")
    return False


is_running = False
research_query = ""
current_page = 1
has_more_results = True
card_buttons = []
prev_btn = None
next_btn = None
page_lbl = None
results_frame = None
results_visible = False
pagination_start_page = 1
max_available_page = None

# Caching and prefetching variables
cached_research_results = {}
prefetched_pages = set()
active_search_query = ""
page_buttons = []
page_num_frame = None
results_container = None


def reset_gui_state(run_button, entry_widget):
    """Restore the GUI button and entry box back to their idle states."""
    global is_running, prev_btn, next_btn, card_buttons
    is_running = False
    run_button.config(text="Search / Download", bg="#8B5CF6", activebackground="#A78BFA", fg="#FFFFFF", activeforeground="#FFFFFF", state='normal')
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
    global current_page, prev_btn, next_btn, cached_research_results
    if not prev_btn or not next_btn:
        return
        
    if current_page == 1:
        prev_btn.config(state='disabled')
    else:
        prev_btn.config(state='normal')
        
    if (current_page + 1) in cached_research_results:
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
            
        if target_doi:
            # Register manual fallback URLs in case programmatic downloads fail
            if target_doi.startswith("http://") or target_doi.startswith("https://"):
                register_discovered_url(target_doi, "Direct URL Fallback")
            elif any(target_doi.lower().startswith(prefix) for prefix in ("ia:", "isbn:", "ol:")):
                register_discovered_url(f"https://annas-archive.li/search?q={urllib.parse.quote(target_doi)}", "Anna's Archive Book Search (.li)")
                register_discovered_url(f"https://annas-archive.pk/search?q={urllib.parse.quote(target_doi)}", "Anna's Archive Book Search (.pk)")
            else:
                register_discovered_url(f"https://annas-archive.li/scidb/{urllib.parse.quote(target_doi)}", "Anna's Archive SciDB (.li)")
                register_discovered_url(f"https://annas-archive.pk/scidb/{urllib.parse.quote(target_doi)}", "Anna's Archive SciDB (.pk)")
            
        if abort_requested:
            raise InterruptedError("Cancelled by user")

        success = False
        is_book_identifier = target_doi and any(target_doi.lower().startswith(prefix) for prefix in ("ia:", "isbn:", "ol:"))
        
        if is_book_identifier:
            status_label.config(text="Querying Book Repositories...", fg="#00ADB5")
            success = try_download_book(target_doi, target_title, status_label=status_label, root_widget=root_widget)
        else:
            if target_doi:
                # Try fast-path pattern matching (PLOS, BioRxiv) before requesting APIs
                if not success and target_doi.lower().startswith("10.1371/"):
                    status_label.config(text="Querying PLOS Database...", fg="#00ADB5")
                    success = try_plos(target_doi, target_title)
                    
                if not success and target_doi.lower().startswith("10.1101/"):
                    status_label.config(text="Querying BioRxiv/MedRxiv API...", fg="#00ADB5")
                    success = try_biorxiv(target_doi, target_title)

                if not success:
                    success = try_publisher_direct(target_doi, target_title, status_label=status_label)

                # Try direct URL download first if target_doi is a direct URL (and not a ResearchGate publication url)
                if not success and (target_doi.startswith("http://") or target_doi.startswith("https://")) and ("researchgate.net" not in target_doi or "/links/" in target_doi):
                    status_label.config(text="Directly Downloading URL...", fg="#00ADB5")
                    success = download_file(target_doi, clean_filename(target_title or "Downloaded_Paper") + ".pdf")
                    if success:
                        print(f"[SUCCESS] Directly downloaded PDF from URL: {target_doi}")

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
                    status_label.config(text="Querying Semantic Scholar...", fg="#00ADB5")
                    success = try_semantic_scholar(target_doi, target_title)

                if abort_requested:
                    raise InterruptedError("Cancelled by user")

                if not success:
                    status_label.config(text="Querying Zenodo...", fg="#00ADB5")
                    success = try_zenodo(target_doi, target_title)

                if abort_requested:
                    raise InterruptedError("Cancelled by user")

                if not success:
                    status_label.config(text="Querying DOAJ...", fg="#00ADB5")
                    success = try_doaj(target_doi, target_title)

                if abort_requested:
                    raise InterruptedError("Cancelled by user")

                if not success:
                    status_label.config(text="Querying CORE...", fg="#00ADB5")
                    success = try_core(target_doi, target_title)
                
                if abort_requested:
                    raise InterruptedError("Cancelled by user")
                    
                if not success:
                    status_label.config(text="Querying SSRN...", fg="#00ADB5")
                    success = try_ssrn(target_doi, target_title)

                if abort_requested:
                    raise InterruptedError("Cancelled by user")

                if not success:
                    status_label.config(text="Querying Sci-Hub Shadows...", fg="#00ADB5")
                    success = try_scihub(target_doi)

                if abort_requested:
                    raise InterruptedError("Cancelled by user")

                if not success:
                    status_label.config(text="Querying Library Genesis...", fg="#00ADB5")
                    success = try_libgen(target_doi, target_title)
                
            if abort_requested:
                raise InterruptedError("Cancelled by user")

            if not success:
                status_label.config(text="Querying arXiv...", fg="#00ADB5")
                success = try_arxiv(target_doi, target_title)
                
            if abort_requested:
                raise InterruptedError("Cancelled by user")

            if not success:
                status_label.config(text="Querying ASTESJ...", fg="#00ADB5")
                success = try_astesj(target_doi, target_title)

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
            print("==============================================" )
        else:
            # All strategies failed — report failure clearly, no browser popup
            valid_fallbacks = sorted(discovered_urls, key=lambda x: x[1])
            status_label.config(text="Download Failed. Publisher blocked all channels.", fg="#F44336")
            print("\n==============================================")
            print("[PROCESS FAILED] Could not retrieve a downloadable PDF.")
            if valid_fallbacks:
                print("[INFO] Discovered URLs (copy-paste to access manually):")
                for fu, rank, label in valid_fallbacks:
                    print(f"  -> [{label}] {fu}")
            print("==============================================" )
            
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


def fetch_yazid_rg_publications():
    """Retrieve Yazid Youcef's publications, attempting live scraping with a guaranteed local fallback."""
    profile_url = "https://www.researchgate.net/profile/Yazid-Youcef"
    
    # 1. Guaranteed robust fallback list of Yazid Youcef's high-quality publications
    local_works = [
        {
            'title': "Intelligent and Secure Homes: IoT Solutions for Advanced Monitoring and Communication",
            'doi': "https://www.researchgate.net/profile/Yazid-Youcef",
            'authors': "Yazid Youcef",
            'year': "2025",
            'journal': "University of Batna 2 (Thesis)",
            'is_oa': True,
            'source': 'yazid_profile'
        },
        {
            'title': "Design and Build IoT Smart Home System with Blocks Based App Inventor Programming",
            'doi': "https://www.researchgate.net/profile/Yazid-Youcef",
            'authors': "Yazid Youcef",
            'year': "2025",
            'journal': "ResearchGate (Technical Report)",
            'is_oa': True,
            'source': 'yazid_profile'
        }
    ]
    
    # 2. Attempt live parse from his ResearchGate profile
    try:
        page_html = fetch_html_resilient(profile_url)
        if page_html and "gtm-research-item" in page_html:
            parts = page_html.split('gtm-research-item')
            parsed_results = []
            for part in parts[1:]:
                link_match = re.search(r'href="([^"]*researchgate\.net/publication/[^"]*)"[^>]*>(.*?)</a>', part)
                if not link_match:
                    link_match = re.search(r'href="(/publication/[^"]+)"[^>]*>(.*?)</a>', part)
                if not link_match:
                    continue
                    
                pub_url = link_match.group(1)
                if pub_url.startswith('/'):
                    pub_url = "https://www.researchgate.net" + pub_url
                title = re.sub('<[^<]+?>', '', link_match.group(2)).strip()
                
                type_match = re.search(r'class="[^"]*nova-legacy-v-entity-item__badge[^"]*"[^>]*>(.*?)</span>', part)
                pub_type = type_match.group(1).strip() if type_match else ""
                
                date_match = re.search(r'class="[^"]*nova-legacy-v-entity-item__meta-data-item[^"]*"[^>]*>\s*<span[^>]*>(.*?)</span>', part)
                if not date_match:
                    date_match = re.search(r'<span[^>]*>\s*([A-Za-z]{3}\s+\d{4}|\d{4})\s*</span>', part)
                pub_date = date_match.group(1).strip() if date_match else "n.d."
                year = "n.d."
                year_match = re.search(r'\b(19\d{2}|20\d{2})\b', pub_date)
                if year_match:
                    year = year_match.group(1)
                    
                is_oa = "Full-text available" in part or "Download" in part
                
                parsed_results.append({
                    'title': title,
                    'doi': pub_url,
                    'authors': "Yazid Youcef",
                    'year': year,
                    'journal': f"ResearchGate ({pub_type})" if pub_type else "ResearchGate",
                    'is_oa': is_oa,
                    'source': 'yazid_profile'
                })
            if parsed_results:
                seen_titles = set()
                deduped = []
                for p in parsed_results:
                    t_low = p['title'].lower().strip()
                    if t_low not in seen_titles:
                        seen_titles.add(t_low)
                        deduped.append(p)
                print(f"[INFO] Successfully retrieved {len(deduped)} publications dynamically from Yazid Youcef's profile.")
                return deduped
    except Exception as e:
        print(f"[WARNING] Live ResearchGate profile query bypassed/failed: {e}")
        
    print("[INFO] Utilizing guaranteed local profile publications fallback.")
    return local_works


def fetch_assma_publications():
    """Retrieve Assma Derdoukh's publications using a guaranteed local fallback."""
    local_works = [
        {
            'title': "On the Robust Stability of Positive Delay Systems Under Time-varying Perturbations",
            'doi': "http://bmathaa.org/repository/docs/BMAA17-1-7.pdf",
            'authors': "Assma Derdoukh, Maissa Kada",
            'year': "2025",
            'journal': "Bulletin of Mathematical Analysis and Applications",
            'is_oa': True,
            'source': 'assma_profile'
        },
        {
            'title': "Sur la méthode de Fourier pour l'étude d'une classe d'équations opératorielles",
            'doi': "https://bu.umc.edu.dz/md/index.php?lvl=more_results&mode=keyword&user_query=Indices+de+d%C3%A9faut&tags=ok",
            'authors': "Assma Derdoukh",
            'year': "2023",
            'journal': "Université Constantine 1 (Thesis)",
            'is_oa': False,
            'source': 'assma_profile'
        }
    ]
    return local_works





def start_update_download(parent, latest_version, download_url):
    """Downloads the installer in the background and updates the header label progress."""
    global dl_link_lbl
    
    # Disable further clicks by unbinding event
    dl_link_lbl.unbind("<Button-1>")
    dl_link_lbl.unbind("<Enter>")
    dl_link_lbl.unbind("<Leave>")
    dl_link_lbl.config(text="📥 Initializing download...", fg="#A78BFA", cursor="")
    
    def do_download():
        try:
            import urllib.request
            import tempfile
            import subprocess
            import sys
            
            # Extract filename from the URL or default to setup exe name
            filename = download_url.split('/')[-1]
            if not filename.endswith('.exe'):
                filename = "AcademicPaperDownloader_Setup.exe"
                
            temp_path = os.path.join(tempfile.gettempdir(), filename)
            
            req = urllib.request.Request(download_url, headers=HEADERS)
            with urllib.request.urlopen(req) as response:
                total_size = int(response.info().get('Content-Length', 0))
                downloaded = 0
                
                with open(temp_path, 'wb') as f:
                    block_size = 65536
                    while True:
                        buffer = response.read(block_size)
                        if not buffer:
                            break
                        downloaded += len(buffer)
                        f.write(buffer)
                        
                        if total_size > 0:
                            pct = int(downloaded * 100 / total_size)
                            parent.after(0, lambda p=pct: dl_link_lbl.config(text=f"📥 Downloading update: {p}%"))
                        else:
                            parent.after(0, lambda: dl_link_lbl.config(text="📥 Downloading update..."))
                            
            # Verify the downloaded file is a valid Windows executable (magic bytes 'MZ')
            if os.path.exists(temp_path):
                with open(temp_path, 'rb') as f:
                    magic = f.read(2)
                if magic != b'MZ':
                    raise ValueError("Downloaded file does not have a valid Windows executable signature.")
                            
            # Launch installer and exit app immediately so the file is not locked
            parent.after(0, lambda: dl_link_lbl.config(text="⚡ Launching Installer..."))
            cmd_str = f'cmd.exe /c timeout /t 2 & start "" "{temp_path}" /SILENT /SP- /SUPPRESSMSGBOXES /NORESTART'
            subprocess.Popen(cmd_str, creationflags=0x08000000)
            parent.after(100, lambda: os._exit(0))
            
        except Exception as e:
            print(f"[ERROR] Failed to download update: {e}")
            # Fallback on failure
            parent.after(0, lambda: reset_failed_update(parent, latest_version, download_url))

    def reset_failed_update(parent, latest_version, download_url):
        dl_link_lbl.config(
            text="❌ Update Failed. Click to try again.", 
            fg="#EF4444", 
            cursor="hand2"
        )
        # Re-bind click and hover events
        dl_link_lbl.bind("<Button-1>", lambda e: start_update_download(parent, latest_version, download_url))
        dl_link_lbl.bind("<Enter>", lambda e: dl_link_lbl.config(fg="#FCA5A5"))
        dl_link_lbl.bind("<Leave>", lambda e: dl_link_lbl.config(fg="#EF4444"))

    t = threading.Thread(target=do_download)
    t.daemon = True
    t.start()


def trigger_update_available_ui(parent, latest_version, download_url):
    """Replaces the releases label in the header with an update notification."""
    global dl_link_lbl
    
    # Change the link label to update action
    dl_link_lbl.config(
        text=f"🚀 Update to v{latest_version} available! (Click to Install)", 
        fg="#F59E0B", 
        font=('Segoe UI Semibold', 9, 'underline')
    )
    
    # Bind the click action to start the update process
    dl_link_lbl.bind("<Button-1>", lambda e: start_update_download(parent, latest_version, download_url))
    
    # Configure hover states for the update notification
    dl_link_lbl.bind("<Enter>", lambda e: dl_link_lbl.config(fg="#FBBF24"))
    dl_link_lbl.bind("<Leave>", lambda e: dl_link_lbl.config(fg="#F59E0B"))



def check_updates_gui(parent, manual=True):
    """Trigger a background thread to check for updates and present the result beautifully."""
    progress_win = None
    if manual:
        progress_win = tk.Toplevel(parent)
        progress_win.title("Checking for Updates")
        progress_win.configure(bg="#0D0B14")
        progress_win.transient(parent)
        progress_win.grab_set()
        
        w, h = 300, 120
        ws = progress_win.winfo_screenwidth()
        hs = progress_win.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        progress_win.geometry(f"{w}x{h}+{int(x)}+{int(y)}")
        progress_win.resizable(False, False)
        
        lbl = tk.Label(progress_win, text="Checking GitHub for updates...", bg="#0D0B14", fg="#A78BFA", font=('Segoe UI', 10), pady=20)
        lbl.pack()
        progress_win.update()
        
    def thread_proc():
        latest_ver, changelog, dl_url = check_for_updates()
        
        if progress_win:
            try:
                progress_win.destroy()
            except Exception:
                pass
                
        if not latest_ver:
            if manual:
                parent.after(0, lambda: status_label.config(text="Update check bypassed (offline/no releases found).", fg="#A78BFA"))
            return
            
        def parse_version(v_str):
            parts = []
            for p in re.findall(r'\d+', v_str):
                try:
                    parts.append(int(p))
                except ValueError:
                    pass
            return parts
            
        current_parsed = parse_version(VERSION)
        latest_parsed = parse_version(latest_ver)
        
        is_newer = False
        for c, l in zip(current_parsed, latest_parsed):
            if l > c:
                is_newer = True
                break
            elif c > l:
                break
        else:
            if len(latest_parsed) > len(current_parsed):
                is_newer = True
                
        if is_newer:
            parent.after(0, lambda: trigger_update_available_ui(parent, latest_ver, dl_url))
            if manual:
                parent.after(0, lambda: status_label.config(text=f"New version v{latest_ver} available! Click the link at the top to install.", fg="#F59E0B"))
        else:
            if manual:
                parent.after(0, lambda: status_label.config(text=f"Academic Paper Downloader is up to date (v{VERSION}).", fg="#10B981"))
                
    t = threading.Thread(target=thread_proc)
    t.daemon = True
    t.start()


_app_mutex = None

def create_app_mutex():
    global _app_mutex
    try:
        import ctypes
        _app_mutex = ctypes.windll.kernel32.CreateMutexW(None, False, "AcademicPaperDownloaderMutex")
    except Exception:
        pass


def launch_gui():
    """Launch the modern dark-themed desktop GUI for Paper Downloader."""
    global GUI_MODE
    GUI_MODE = True
    global prev_btn, next_btn, page_lbl, results_frame, results_container, card_buttons, clear_res_btn, status_label, dl_link_lbl, results_visible, main_container, toggle_console_btn
    
    create_app_mutex()
    
    root = tk.Tk()
    root.title(f"Premium Paper Downloader v{VERSION} by Yazid YOUCEF")
    root.configure(bg="#0D0B14")
    
    # Silent update check on startup after 1.5 seconds
    root.after(1500, lambda: check_updates_gui(root, manual=False))
    
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
    try:
        root.state('zoomed')
    except Exception:
        pass
    
    # Header Section (Centered)
    header_frame = tk.Frame(root, bg="#0D0B14", pady=12)
    header_frame.pack(fill='x', padx=25)
    
    # Title & Update symbols container centered beautifully
    title_container = tk.Frame(header_frame, bg="#0D0B14")
    title_container.pack(anchor='center')
    
    header_lbl = tk.Label(title_container, text=f"PAPER DOWNLOADER v{VERSION}", bg="#0D0B14", fg="#A855F7", font=('Segoe UI Semibold', 16))
    header_lbl.pack(side='left')
    
    # Flat spacer label
    tk.Label(title_container, text="  ", bg="#0D0B14").pack(side='left')
    
    # Update interactive label/symbol (🔄)
    update_sym = tk.Label(title_container, text="🔄", bg="#0D0B14", fg="#A78BFA", font=('Segoe UI', 11), cursor="hand2")
    update_sym.pack(side='left', padx=3)
    update_sym.bind("<Button-1>", lambda e: check_updates_gui(root, manual=True))
    
    # Hover states to make elements feel alive
    def on_sym_enter(lbl):
        lbl.config(fg="#C084FC")
        
    def on_sym_leave(lbl):
        lbl.config(fg="#A78BFA")
        
    update_sym.bind("<Enter>", lambda e: on_sym_enter(update_sym))
    update_sym.bind("<Leave>", lambda e: on_sym_leave(update_sym))
    
    sub_lbl = tk.Label(header_frame, text="Enter a DOI to download directly · Enter keywords to search and browse results.", bg="#0D0B14", fg="#A78BFA", font=('Segoe UI', 9))
    sub_lbl.pack(anchor='center', pady=(2, 0))
    
    author_lbl = tk.Label(header_frame, text="Designed & Developed by Yazid YOUCEF", bg="#0D0B14", fg="#8B5CF6", font=('Segoe UI', 8, 'italic'))
    author_lbl.pack(anchor='center', pady=(3, 0))
    
    # Clickable download releases link
    def open_releases(e=None):
        import webbrowser
        webbrowser.open("https://github.com/dzmarkets/Academic-Paper-Downloader/releases")
        
    dl_link_lbl = tk.Label(header_frame, text="🌐 Get Latest Releases & Updates", bg="#0D0B14", fg="#10B981", font=('Segoe UI Semibold', 9, 'underline'), cursor="hand2")
    dl_link_lbl.pack(anchor='center', pady=(4, 0))
    dl_link_lbl.bind("<Button-1>", open_releases)
    
    # Hover states to make elements feel alive
    def on_link_enter(e):
        dl_link_lbl.config(fg="#34D399")
        
    def on_link_leave(e):
        dl_link_lbl.config(fg="#10B981")
        
    dl_link_lbl.bind("<Enter>", on_link_enter)
    dl_link_lbl.bind("<Leave>", on_link_leave)
    
    # Main Input Card (Centered Elements)
    card_frame = tk.Frame(root, bg="#1A1625", bd=1, relief='flat', padx=20, pady=15)
    card_frame.pack(fill='x', padx=25, pady=(5, 5))
    
    # Side-by-side main container
    global main_container
    main_container = tk.Frame(root, bg="#0D0B14")
    main_container.pack(fill='both', expand=True, pady=(0, 10))
    main_container.grid_columnconfigure(0, weight=2)
    main_container.grid_columnconfigure(1, weight=1)
    main_container.grid_rowconfigure(0, weight=1)
    
    input_lbl = tk.Label(card_frame, text="Enter DOI or Keywords:", bg="#1A1625", fg="#EEEEEE", font=('Segoe UI Semibold', 10))
    input_lbl.pack(anchor='center', pady=(8, 5))
    
    # Modern rounded entry emulation
    entry_container = tk.Frame(card_frame, bg="#2E2543", bd=0, padx=8, pady=6)
    entry_container.pack(fill='x', pady=5)
    
    entry = tk.Entry(entry_container, bg="#2E2543", fg="#FFFFFF", insertbackground="#FFFFFF", bd=0, font=('Segoe UI', 11), relief='flat', justify='center')
    entry.pack(fill='x')
    entry.focus_set()
    
    # Status label — always visible
    status_label = tk.Label(card_frame, text="Ready for input.", bg="#1A1625", fg="#A78BFA", font=('Segoe UI', 10, 'italic'))
    status_label.pack(pady=5, anchor='center')
    
    # --- Interactive Research Mode Results Frame ---
    results_frame = tk.Frame(main_container, bg="#0D0B14", padx=25)

    # Sub-frame for canvas + scrollbar to separate from pagination and prevent packing squeeze
    canvas_frame = tk.Frame(results_frame, bg="#0D0B14")
    canvas_frame.pack(side='top', fill='both', expand=True)

    # Scrollable canvas wrapper for results
    _results_canvas = tk.Canvas(canvas_frame, bg="#0D0B14", highlightthickness=0)
    _results_scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=_results_canvas.yview, style="Vertical.TScrollbar")
    _results_canvas.configure(yscrollcommand=_results_scrollbar.set)
    _results_scrollbar.pack(side="right", fill="y")
    _results_canvas.pack(side="left", fill="both", expand=True)

    results_container = tk.Frame(_results_canvas, bg="#0D0B14")
    _results_canvas_window = _results_canvas.create_window((0, 0), window=results_container, anchor="nw")

    def _on_results_frame_configure(event):
        _results_canvas.configure(scrollregion=_results_canvas.bbox("all"))
        # Decide canvas height: fit content up to 300px, then scroll
        content_h = results_container.winfo_reqheight()
        canvas_h = min(content_h, 300)
        _results_canvas.configure(height=canvas_h)
        # Also update wraplength on all visible cards
        new_width = _results_canvas.winfo_width()
        new_wrap = max(300, new_width - 180)
        for card in results_container.winfo_children():
            try:
                details_f = card.winfo_children()[0]
                children = details_f.winfo_children()
                if len(children) >= 1:
                    children[0].config(wraplength=new_wrap)
                if len(children) >= 3:
                    children[2].config(wraplength=new_wrap)
            except Exception:
                pass

    def _on_canvas_width_change(event):
        _results_canvas.itemconfig(_results_canvas_window, width=event.width)

    results_container.bind("<Configure>", _on_results_frame_configure)
    _results_canvas.bind("<Configure>", _on_canvas_width_change)

    # Mouse-wheel scrolling (Windows)
    def _on_mousewheel(event):
        _results_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    _results_canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
    # (wraplength + scroll region handled in _on_results_frame_configure above)

    def clear_research_results(clear_cache=True):
        """Clear all loaded paper cards from the research view."""
        global card_buttons, cached_research_results, prefetched_pages, active_search_query, max_available_page
        for widget in results_container.winfo_children():
            widget.destroy()
        card_buttons = []
        _results_canvas.yview_moveto(0)  # Reset scroll to top
        
        if clear_cache:
            nav_frame.pack_forget()          # Hide nav bar together with results
            global results_visible
            results_visible = False
            _update_grid_layout()
            entry.delete(0, tk.END)
            status_label.config(text="Ready for input.", fg="#A78BFA")
            
            # Clear search cache and reset page numbers UI
            cached_research_results.clear()
            prefetched_pages.clear()
            active_search_query = ""
            max_available_page = None
            reset_page_buttons_ui()

    # Navigation bar — placed AFTER the canvas so it appears at the bottom of results
    nav_frame = tk.Frame(results_frame, bg="#0D0B14", pady=5)
    # nav_frame packs AFTER the canvas widget — Tkinter pack order = top-to-bottom
    # It is shown/hidden together with results_frame; packed explicitly in display_research_results

    def on_prev_click():
        global current_page, research_query
        if current_page > 1:
            load_research_page(research_query, current_page - 1)

    def on_next_click():
        global current_page, research_query
        load_research_page(research_query, current_page + 1)

    prev_btn = tk.Button(nav_frame, text="\u25c4 Previous", bg="#2E2543", fg="#EEEEEE", activebackground="#3F335C", activeforeground="#FFFFFF", disabledforeground="#8E8A9F", bd=0, font=('Segoe UI', 9), padx=12, pady=4, cursor="hand2", command=on_prev_click, state='disabled')
    prev_btn.pack(side='left', padx=15)

    global page_buttons, page_num_frame, page_lbl
    page_buttons = []
    page_num_frame = tk.Frame(nav_frame, bg="#0D0B14")
    page_num_frame.pack(side='left', fill='x', expand=True)

    page_subframe = tk.Frame(page_num_frame, bg="#0D0B14")
    page_subframe.pack(anchor='center')

    page_lbl = tk.Label(page_subframe, text="Page", bg="#0D0B14", fg="#8E8A9F", font=('Segoe UI Semibold', 9))
    page_lbl.pack(side='left', padx=(0, 6))

    for p in range(1, 11):
        btn = tk.Button(
            page_subframe,
            text=str(p),
            bg="#1E1A2B",
            fg="#6B7280",
            activebackground="#3F335C",
            activeforeground="#FFFFFF",
            disabledforeground="#4B5563",
            bd=0,
            font=('Segoe UI Semibold', 9),
            padx=8,
            pady=3,
            cursor="hand2",
            state='disabled',
            command=lambda p_idx=p: load_cached_page(p_idx)
        )
        btn.pack(side='left', padx=3)
        page_buttons.append(btn)

    clear_res_btn = tk.Button(nav_frame, text="Clear Results", bg="#2E2543", fg="#EEEEEE", activebackground="#D32F2F", activeforeground="#FFFFFF", disabledforeground="#8E8A9F", bd=0, font=('Segoe UI Semibold', 9), padx=12, pady=4, cursor="hand2", command=clear_research_results)
    clear_res_btn.pack(side='right', padx=(0, 15))

    next_btn = tk.Button(nav_frame, text="Next \u25ba", bg="#2E2543", fg="#EEEEEE", activebackground="#3F335C", activeforeground="#FFFFFF", disabledforeground="#8E8A9F", bd=0, font=('Segoe UI', 9), padx=12, pady=4, cursor="hand2", command=on_next_click)
    next_btn.pack(side='right', padx=15)

    # ── Console / Logs area ────────────────────────────────────────────────────
    # The header is always visible; the body (log_area) can be toggled.
    logs_frame = tk.Frame(main_container, bg="#0D0B14", padx=25)

    logs_header = tk.Frame(logs_frame, bg="#0D0B14")
    logs_header.pack(fill='x', pady=(0, 4))

    console_lbl = tk.Label(logs_header, text="\U0001f4dc  Pipeline Console Logs",
                           bg="#0D0B14", fg="#A78BFA", font=('Segoe UI Semibold', 9))
    console_lbl.pack(side='left')

    # Collapsible body frame that holds log_area + its scrollbar
    _console_body = tk.Frame(logs_frame, bg="#0D0B14")
    _console_body.pack(fill='both', expand=True)
    _console_visible = [True]   # mutable flag

    def _update_grid_layout():
        try:
            results_frame.grid_forget()
            logs_frame.grid_forget()
            
            is_results_visible = results_visible
            is_logs_visible = _console_visible[0]
            
            if is_results_visible and is_logs_visible:
                main_container.grid_columnconfigure(0, weight=2)
                main_container.grid_columnconfigure(1, weight=1)
                results_frame.grid(row=0, column=0, sticky='nsew', padx=(25, 10))
                logs_frame.grid(row=0, column=1, sticky='nsew', padx=(10, 25))
            elif is_results_visible and not is_logs_visible:
                main_container.grid_columnconfigure(0, weight=1)
                results_frame.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=25)
            elif not is_results_visible and is_logs_visible:
                main_container.grid_columnconfigure(0, weight=1)
                logs_frame.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=25)
        except Exception as e:
            print(f"[ERROR] Grid update failed: {e}")

    def _toggle_console():
        if _console_visible[0]:
            _console_visible[0] = False
            toggle_console_btn.config(text="Show Console [+]")
        else:
            _console_visible[0] = True
            toggle_console_btn.config(text="Hide Console [-]")
        _update_grid_layout()

    def _force_show_console():
        if not _console_visible[0]:
            _console_visible[0] = True
            toggle_console_btn.config(text="Hide Console [-]")
            _update_grid_layout()

    def clear_logs():
        log_area.delete('1.0', 'end')

    clear_btn = tk.Button(
        logs_header,
        text="Clear Logs",
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

    log_area = tk.Text(_console_body, bg="#1A1625", fg="#F3E8FF", insertbackground="#FFFFFF",
                       bd=0, font=('Consolas', 9), relief='flat', height=10)
    scrollbar = ttk.Scrollbar(_console_body, orient="vertical", command=log_area.yview,
                               style="Vertical.TScrollbar")
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
        
    def reset_inputs():
        """Re-enable all input fields (called after any operation completes)."""
        entry.config(state='normal')
        clear_res_btn.config(state='normal')
        
    def start_individual_download(doi, paper_title):
        """Trigger threaded background downloader for a specific result card's DOI."""
        global is_running, abort_requested
        
        # Disable all UI controls to prevent multiple actions
        is_running = True
        abort_requested = False
        
        entry.config(state='disabled')
        run_button.config(text="Stop Downloading", bg="#D32F2F", activebackground="#EF5350", fg="#FFFFFF", activeforeground="#FFFFFF", state='normal')
        prev_btn.config(state='disabled')
        next_btn.config(state='disabled')
        clear_res_btn.config(state='disabled')
        for btn in card_buttons:
            btn.config(state='disabled')
            
        status_label.config(text="Downloading paper...", fg="#A855F7")
        _force_show_console()
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
        
    def update_pagination_buttons_ui():
        global page_buttons, pagination_start_page, current_page, cached_research_results, max_available_page
        if not page_buttons:
            return
            
        # Unpack all buttons first to maintain correct sequence
        for btn in page_buttons:
            btn.pack_forget()
            
        # Pack and style visible buttons based on cache / active page
        for i in range(10):
            p = pagination_start_page + i
            btn = page_buttons[i]
            
            # Rebind button configuration dynamically
            btn.config(text=str(p), command=lambda p_idx=p: load_cached_page(p_idx))
            
            # Determine visibility:
            # We show a button if:
            # - p is <= max_available_page (if max_available_page is set)
            # - OR max_available_page is None (we show all 10 buttons of the current block)
            show_btn = False
            if max_available_page is None:
                show_btn = True
            else:
                if p <= max_available_page:
                    show_btn = True
                    
            if show_btn:
                btn.pack(side='left', padx=3)
                if p in cached_research_results:
                    if p == current_page:
                        btn.config(state='normal', bg="#8B5CF6", fg="#FFFFFF")
                    else:
                        btn.config(state='normal', bg="#2E2543", fg="#EEEEEE")
                else:
                    # Not cached yet
                    if p == current_page:
                        btn.config(state='normal', bg="#8B5CF6", fg="#FFFFFF")
                    else:
                        btn.config(state='disabled', bg="#1E1A2B", fg="#6B7280")

    def reset_page_buttons_ui():
        global pagination_start_page, current_page, max_available_page
        pagination_start_page = 1
        current_page = 1
        max_available_page = None
        update_pagination_buttons_ui()

    def enable_page_button(page_idx):
        update_pagination_buttons_ui()
        update_pagination_states()

    def update_page_buttons_style(active_page):
        update_pagination_buttons_ui()

    def load_cached_page(page_idx):
        global current_page, research_query, cached_research_results
        if page_idx in cached_research_results:
            display_research_results(cached_research_results[page_idx], research_query, page_idx)

    def on_prefetch_complete(query):
        global active_search_query, abort_requested
        if active_search_query == query:
            if abort_requested:
                status_label.config(text="Search stopped by user.", fg="#F44336")
            else:
                pages_found = len(cached_research_results)
                if pages_found > 0:
                    status_label.config(text=f"Search complete. Found {pages_found} pages of results.", fg="#4CAF50")
                else:
                    status_label.config(text="No matching documents found.", fg="#F44336")
            reset_gui_state(run_button, entry)
            reset_inputs()
            # Final update to ensure buttons visibility aligns with search completeness
            update_pagination_buttons_ui()

    def start_background_prefetch(query, clear_cache=True):
        global active_search_query, cached_research_results, prefetched_pages, pagination_start_page, max_available_page
        active_search_query = query
        if clear_cache:
            cached_research_results.clear()
            prefetched_pages.clear()
            pagination_start_page = 1
            max_available_page = None
            reset_page_buttons_ui()
        else:
            max_available_page = None
            update_pagination_buttons_ui()
        
        def prefetch_loop():
            global abort_requested, active_search_query, max_available_page
            
            start_p = pagination_start_page
            end_p = pagination_start_page + 9
            
            for p in range(start_p, end_p + 1):
                if abort_requested:
                    break
                if active_search_query != query:
                    break
                    
                # Skip already cached pages (e.g. page 10 when shifting to 10-19 range)
                if p in cached_research_results and cached_research_results[p]:
                    continue
                    
                try:
                    # 1. Fetch priority works
                    yazid_works = fetch_yazid_rg_publications()
                    assma_works = fetch_assma_publications()
                    priority_works = yazid_works + assma_works
                    
                    # Deduplicate priority works by title to prevent duplicates
                    seen_priority = set()
                    unique_priority = []
                    for w in priority_works:
                        t_low = w['title'].lower().strip()
                        if t_low not in seen_priority:
                            seen_priority.add(t_low)
                            unique_priority.append(w)
                    priority_works = unique_priority
                    
                    # 2. Check for matches against keywords
                    stripped = query.strip()
                    is_exact = (stripped.startswith('"') and stripped.endswith('"')) or (stripped.startswith("'") and stripped.endswith("'"))
                    exact_phrase = stripped.strip('"').strip("'").strip() if is_exact else None
                    
                    matching_priority = []
                    query_words = [w.lower() for w in re.split(r'\W+', query) if len(w) > 2]
                    
                    for work in priority_works:
                        title_lower = work['title'].lower()
                        authors_lower = work['authors'].lower()
                        is_match = False
                        
                        if not query_words:
                            is_match = True
                        elif "yazid" in query.lower() or "youcef" in query.lower():
                            if "yazid" in authors_lower or "youcef" in authors_lower:
                                is_match = True
                        elif "assma" in query.lower() or "derdoukh" in query.lower():
                            if "assma" in authors_lower or "derdoukh" in authors_lower:
                                is_match = True
                        elif exact_phrase:
                            phrase = exact_phrase.lower()
                            if (phrase in title_lower) or (phrase in authors_lower):
                                is_match = True
                        else:
                            for word in query_words:
                                if word in title_lower or word in authors_lower:
                                    is_match = True
                                    break
                                    
                        if is_match:
                            matching_priority.append(work)
                    
                    effective_priority = min(5, len(matching_priority))
                    if p == 1:
                        adjusted_offset = 0
                    else:
                        adjusted_offset = (p - 1) * 5 - effective_priority
                        
                    # Fetch results from Crossref, OpenAlex, and Scholar
                    crossref_results = search_crossref(query, offset=adjusted_offset, rows=5, type_filter="Papers", author="")
                    openalex_results = search_openalex_keyword(query, offset=adjusted_offset, rows=5, type_filter="Papers")
                    scholar_results = search_google_scholar(query, offset=adjusted_offset, rows=5)
                    
                    results = []
                    results.extend(crossref_results)
                    for r in openalex_results:
                        if not any(r['title'].lower() in x['title'].lower() or x['title'].lower() in r['title'].lower() or (r['doi'] and r['doi'] == x['doi']) for x in results):
                            results.append(r)
                    for r in scholar_results:
                        if not any(r['title'].lower() in x['title'].lower() or x['title'].lower() in r['title'].lower() or (r['doi'] and r['doi'] == x['doi']) for x in results):
                            results.append(r)
                            
                    if p == 1 and matching_priority:
                        cleaned_results = []
                        for r in results:
                            if not any(y['title'].lower() in r['title'].lower() or r['title'].lower() in y['title'].lower() for y in matching_priority):
                                cleaned_results.append(r)
                        results = matching_priority + cleaned_results
                        
                    results = results[:5]
                    
                    if abort_requested or active_search_query != query:
                        break
                        
                    cached_research_results[p] = results
                    prefetched_pages.add(p)
                    
                    if p == 1:
                        running_event.clear()  # Stop loading animation
                        if results:
                            root.after(0, lambda r=results: display_research_results(r, query, 1))
                            root.after(0, lambda: status_label.config(text="Page 1 loaded. Fetching subsequent pages in background...", fg="#10B981"))
                        else:
                            max_available_page = 1
                            root.after(0, lambda: display_research_results([], query, 1))
                            break
                    else:
                        if results:
                            root.after(0, lambda p_idx=p: enable_page_button(p_idx))
                        else:
                            max_available_page = p - 1
                            root.after(0, update_pagination_buttons_ui)
                            break
                            
                except Exception as e:
                    print(f"[WARNING] Prefetch page {p} failed: {e}")
                    if p == 1:
                        running_event.clear()
                        root.after(0, lambda: status_label.config(text="Failed to fetch search results.", fg="#F44336"))
                        root.after(0, lambda: reset_gui_state(run_button, entry))
                        root.after(0, reset_inputs)
                        break
                        
                import time
                time.sleep(0.5)
                
            running_event.clear()
            root.after(0, lambda: on_prefetch_complete(query))
            
        t_prefetch = threading.Thread(target=prefetch_loop)
        t_prefetch.daemon = True
        t_prefetch.start()

    def display_research_results(results, query, page):
        """Render the 5 results cards dynamically into the results frame."""
        global current_page, research_query, card_buttons, has_more_results, pagination_start_page
        
        if not results:
            if page > 1:
                status_label.config(text="No more results available.", fg="#FBBF24")
                current_page = page - 1
                update_page_buttons_style(current_page)
                update_pagination_states()
                reset_gui_state(run_button, entry)
                return
            else:
                status_label.config(text="No matching documents found.", fg="#F44336")
                clear_research_results()
                reset_gui_state(run_button, entry)
                reset_inputs()
                return
                
        # Shift pagination range if necessary
        if page == pagination_start_page + 9:
            pagination_start_page = page
            # Prefetch the next window of pages (e.g. from page + 1 to page + 9)
            start_background_prefetch(query, clear_cache=False)
        elif page < pagination_start_page:
            pagination_start_page = max(1, page - 8)
            start_background_prefetch(query, clear_cache=False)
            
        current_page = page
        research_query = query
        card_buttons = []
        has_more_results = (len(results) == 5)
        
        clear_research_results(clear_cache=False)

        global results_visible
        results_visible = True
        _update_grid_layout()
        nav_frame.pack(side='bottom', fill='x', pady=5)          # nav at the bottom of results_frame
        _results_canvas.yview_moveto(0)   # Always scroll back to top on new results
        update_page_buttons_style(page)
        update_pagination_states()
        
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
            
            # Format identifier label (DOI for papers)
            raw_id = result['doi']
            is_book = (result.get('source') == 'openlibrary') or (raw_id and any(raw_id.lower().startswith(prefix) for prefix in ("ia:", "isbn:", "ol:")))
            
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
                    if raw_id.startswith("http://") or raw_id.startswith("https://"):
                        if "researchgate.net" in raw_id:
                            id_label = "DOI"
                            id_val = "N/A"
                        else:
                            id_label = "URL"
                            id_val = raw_id
                    else:
                        id_label = "DOI"
                        id_val = raw_id
                doi_str = f"{id_label}: {id_val}"
            else:
                doi_str = "ISBN/ID: N/A" if is_book else "DOI: N/A"
                
            if is_book:
                can_dl = result.get('can_download', True)  # default True for ia: items
                # Also check T&F DOI prefix (doi like 10.1201/ etc.)
                raw_doi = result.get('doi', '')
                if not can_dl and raw_doi and any(raw_doi.startswith(p) for p in _TF_DOI_PREFIXES):
                    can_dl = True
                if can_dl:
                    badge_text = "  [PDF Download Available]"
                    badge_fg = "#10B981"
                else:
                    badge_text = "  [No Direct PDF Available]"
                    badge_fg = "#6B7280"
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
        
    def load_research_page(query, page):
        """Fetch keyword search results for a page offset.
        Uses cached results if query matches the current active query;
        otherwise triggers background prefetching for pages 1-10.
        """
        global is_running, abort_requested, active_search_query, cached_research_results
        
        # If this page is already cached for the active query, display it instantly!
        if active_search_query == query and page in cached_research_results:
            load_cached_page(page)
            return
            
        # Otherwise, this is a new query. Start background prefetching!
        is_running = True
        abort_requested = False
        
        # Disable entry and change search button to stop
        entry.config(state='disabled')
        run_button.config(text="Stop Search", bg="#D32F2F", activebackground="#EF5350", fg="#FFFFFF", activeforeground="#FFFFFF")
        prev_btn.config(state='disabled')
        next_btn.config(state='disabled')
        clear_res_btn.config(state='disabled')
        for btn in card_buttons:
            btn.config(state='disabled')
            
        status_label.config(text="Searching Crossref & OpenAlex...", fg="#A855F7")
        running_event.set()
        animate_loading(status_label, running_event)
        
        start_background_prefetch(query)
        
    def run_thread(identifier):
        try:
            run_pipeline_bg(identifier, status_label, log_area, run_button, entry, root)
        finally:
            running_event.clear()
            
    def handle_button_click():
        global is_running, abort_requested
        
        if not is_running:
            # START ACTION
            identifier = entry.get().strip()
            if not identifier:
                status_label.config(text="Please enter a DOI or keywords first!", fg="#F44336")
                return
            
            # Auto-detect: is this a DOI / identifier, or a keyword query?
            is_doi = (
                identifier.startswith("10.")               # Standard DOI
                or identifier.startswith("http://")        # URL DOI
                or identifier.startswith("https://")
                or any(identifier.lower().startswith(p) for p in ("ia:", "isbn:", "ol:"))  # Book IDs
                or re.match(r'^10\.\d{4,}/\S+$', identifier)  # Strict DOI pattern
            )

            if is_doi:
                # --- DIRECT DOWNLOAD MODE ---
                clear_research_results()
                is_running = True
                abort_requested = False
                entry.config(state='disabled')
                run_button.config(text="Stop Downloading", bg="#D32F2F", activebackground="#EF5350", fg="#FFFFFF", activeforeground="#FFFFFF")
                status_label.config(text="Initializing pipeline...", fg="#A855F7")
                _force_show_console()
                running_event.set()
                animate_loading(status_label, running_event)
                log_area.delete('1.0', 'end')
                t = threading.Thread(target=run_thread, args=(identifier,))
                t.daemon = True
                t.start()
            else:
                # --- KEYWORD SEARCH MODE ---
                load_research_page(identifier, 1)
        else:
            # STOP ACTION
            abort_requested = True
            status_label.config(text="Stopping...", fg="#FF9800")
            run_button.config(state='disabled')
        
    # Center Search / Download Button
    btn_frame = tk.Frame(card_frame, bg="#1A1625")
    btn_frame.pack(anchor='center', pady=(10, 0))
    
    run_button = tk.Button(btn_frame, text="Search / Download", bg="#8B5CF6", fg="#FFFFFF", activebackground="#A78BFA", activeforeground="#FFFFFF", disabledforeground="#8E8A9F", bd=0, font=('Segoe UI Semibold', 10), padx=25, pady=8, cursor="hand2", command=handle_button_click)
    run_button.pack(side='left', padx=10)
    
    toggle_console_btn = tk.Button(btn_frame, text="Hide Console [-]", bg="#2E2543", fg="#EEEEEE", activebackground="#3F335C", activeforeground="#FFFFFF", bd=0, font=('Segoe UI Semibold', 10), padx=20, pady=8, cursor="hand2", command=_toggle_console)
    toggle_console_btn.pack(side='left', padx=10)
    
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
        import re
        import os

        # ── Enable ANSI in Windows terminal ───────────────────────────────────
        if os.name == 'nt':
            try:
                os.system('')
            except Exception:
                pass

        # ── ANSI colours for terminal ──────────────────────────────────────────
        GOLD       = "\033[1;33m"
        PURPLE     = "\033[1;35m"
        CYAN       = "\033[1;36m"
        GREEN      = "\033[1;32m"
        WHITE_BOLD = "\033[1;37m"
        RESET      = "\033[0m"

        terminal_width = 80

        # Plain text lines (stripped of ANSI) for in-app console
        # Each entry: (plain_text, tag_name)  tag_name=None means default colour
        styled_lines = [
            ("", None),
            ("* ------------------------------------------------------------- *", "gold"),
            ("  Soutenir l'Innovation Locale / Support Local Innovation [DZ]  ", "purple"),
            ("* ------------------------------------------------------------- *", "gold"),
            ("", None),
            ("Buy Me a Coffee ne fonctionne pas directement en Algerie.", "white_bold"),
            ("Encouragez ce travail par transfert local (Baridimob / CCP).", None),
            ("", None),
            ("Cette application reduit considerablement votre temps de recherche", "cyan"),
            ("en interrogeant simultanement plus de 11 sources academiques majeures", "cyan"),
            ("et en resolvant jusqu'a 50 000 journaux scientifiques en 1 seul clic !", "green"),
            ("", None),
            ("Votre contribution permet de perenniser le developpement de cet outil gratuit.", None),
            ("", None),
            ("Informations de Transfert / Donation Details :", "white_bold"),
            ("-------------------------------------------------------------", None),
            ("Nom Complet :   Yazid Youcef", "cyan"),
            ("RIP CCP :       00799999000605964735", "green"),
            ("-------------------------------------------------------------", None),
            ("", None),
            ("Merci infiniment pour votre generosite et votre soutien ! <3", "gold"),
            ("* ------------------------------------------------------------- *", "gold"),
            ("", None),
        ]

        # ── Print to terminal (with ANSI) ──────────────────────────────────────
        ansi_map = {
            "gold":       GOLD,
            "purple":     PURPLE,
            "cyan":       CYAN,
            "green":      GREEN,
            "white_bold": WHITE_BOLD,
            None:         "",
        }
        for plain, tag in styled_lines:
            colour = ansi_map.get(tag, "")
            raw_line = f"{colour}{plain}{RESET}" if colour else plain
            try:
                padding = max(0, (terminal_width - len(plain)) // 2)
                print(" " * padding + raw_line)
            except Exception:
                try:
                    print(plain)
                except Exception:
                    pass

        # ── Write into the in-app Pipeline Console log_area ───────────────────
        try:
            # Force the console visible first
            _force_show_console()
            # Colour tag definitions (Tkinter colours)
            tag_colours = {
                "gold":       "#F59E0B",
                "purple":     "#A855F7",
                "cyan":       "#22D3EE",
                "green":      "#10B981",
                "white_bold": "#FFFFFF",
            }
            # Configure tags once (safe to call multiple times)
            for tag_name, hex_colour in tag_colours.items():
                log_area.tag_configure(
                    f"bmc_{tag_name}",
                    foreground=hex_colour,
                    font=('Consolas', 9, 'bold')
                )
            log_area.tag_configure("bmc_normal", foreground="#F3E8FF", font=('Consolas', 9))

            log_area.config(state='normal')
            log_area.delete('1.0', 'end')   # Clear logs first for a clean donation display

            for plain, tag in styled_lines:
                padding = max(0, (terminal_width - len(plain)) // 2)
                centered = " " * padding + plain
                tk_tag = f"bmc_{tag}" if tag else "bmc_normal"
                log_area.insert('end', centered + "\n", tk_tag)

            log_area.see('end')
        except Exception:
            pass


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
        pady=4,
        cursor="hand2",
        command=open_bmc
    )
    bmc_btn.pack(anchor='center')
    
    rip_lbl = tk.Label(bmc_frame, text="RIP CCP : 00799999000605964735",
                       bg="#120F1E", fg="#10B981", font=('Segoe UI Semibold', 8))
    rip_lbl.pack(pady=(4, 0), anchor='center')
    
    tk.Label(bmc_frame, text="Encourager l'innovation locale 🇩🇿",
             bg="#120F1E", fg="#6B7280", font=('Segoe UI', 7, 'italic')).pack(pady=(2, 0))
    
    def check_country_bg():
        """Background thread: reveal support panel only for Algerian users."""
        country = get_user_country()
        if country == 'DZ':
            root.after(0, lambda: support_frame.pack(fill='x', side='bottom'))
    
    t_geo = threading.Thread(target=check_country_bg)
    t_geo.daemon = True
    t_geo.start()
    # ─────────────────────────────────────────────────────────────────────────
    
    _update_grid_layout()
    root.mainloop()


# --- Main Orchestration Entry Point ---
if __name__ == "__main__":
    # If arguments are passed, run in headless CLI mode. Otherwise, launch GUI.
    if len(sys.argv) > 1:
        discovered_urls.clear()
        target_doi = None
        target_title = None

        first_arg = sys.argv[1].strip()
        if first_arg.startswith("10."):
            target_doi = first_arg
            target_title = sys.argv[2] if len(sys.argv) > 2 else None
        elif first_arg.startswith("http://") or first_arg.startswith("https://"):
            target_doi = first_arg
            target_title = sys.argv[2] if len(sys.argv) > 2 else None
        elif any(first_arg.lower().startswith(prefix) for prefix in ("ia:", "isbn:", "ol:")):
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

        if target_doi:
            # Register manual fallback URLs in case programmatic downloads fail
            if target_doi.startswith("http://") or target_doi.startswith("https://"):
                register_discovered_url(target_doi, "Direct URL Fallback")
            elif any(target_doi.lower().startswith(prefix) for prefix in ("ia:", "isbn:", "ol:")):
                register_discovered_url(f"https://annas-archive.li/search?q={urllib.parse.quote(target_doi)}", "Anna's Archive Book Search (.li)")
                register_discovered_url(f"https://annas-archive.pk/search?q={urllib.parse.quote(target_doi)}", "Anna's Archive Book Search (.pk)")
            else:
                register_discovered_url(f"https://annas-archive.li/scidb/{urllib.parse.quote(target_doi)}", "Anna's Archive SciDB (.li)")
                register_discovered_url(f"https://annas-archive.pk/scidb/{urllib.parse.quote(target_doi)}", "Anna's Archive SciDB (.pk)")

        # Run through pipeline until one layer successfully finishes downloading
        success = False
        is_book_identifier = target_doi and any(target_doi.lower().startswith(prefix) for prefix in ("ia:", "isbn:", "ol:"))
        
        if is_book_identifier:
            success = try_download_book(target_doi, target_title)
        else:
            if target_doi:
                # Try fast-path pattern matching (PLOS, BioRxiv) before requesting APIs
                if not success and target_doi.lower().startswith("10.1371/"):
                    success = try_plos(target_doi, target_title)
                if not success and target_doi.lower().startswith("10.1101/"):
                    success = try_biorxiv(target_doi, target_title)

                # Try direct URL download first if target_doi is a direct URL (and not a ResearchGate publication url)
                if not success and (target_doi.startswith("http://") or target_doi.startswith("https://")) and ("researchgate.net" not in target_doi or "/links/" in target_doi):
                    success = download_file(target_doi, clean_filename(target_title or "Downloaded_Paper") + ".pdf")
                    if success:
                        print(f"[SUCCESS] Directly downloaded PDF from URL: {target_doi}")

                # Try Taylor & Francis first for known T&F DOI prefixes
                if not success and any(target_doi.startswith(p) for p in _TF_DOI_PREFIXES):
                    success = try_download_taylorfrancis(target_doi, target_title)
                if not success:
                    success = try_unpaywall(target_doi)
                if not success:
                    success = try_semantic_scholar(target_doi, target_title)
                if not success:
                    success = try_zenodo(target_doi, target_title)
                if not success:
                    success = try_doaj(target_doi, target_title)
                if not success:
                    success = try_core(target_doi, target_title)
                if not success:
                    success = try_ssrn(target_doi, target_title)
                if not success:
                    success = try_scihub(target_doi)
                if not success:
                    success = try_libgen(target_doi, target_title)
            if not success:
                success = try_arxiv(target_doi, target_title)
            if not success:
                success = try_astesj(target_doi, target_title)
            if not success:
                success = try_europe_pmc(target_doi, target_title)
            if not success:
                success = try_researchgate(target_doi, target_title)
            if not success:
                success = try_download_book(target_doi, target_title)
            
        if success:
            print("\n==============================================")
            print("[PROCESS FINISHED] Document pulled successfully.")
            print("==============================================")
        else:
            # CLI mode failed to download programmatically. Report failure cleanly without browser popups.
            valid_fallbacks = sorted(discovered_urls, key=lambda x: x[1])
            print("\n==============================================")
            print("[PROCESS FAILED] Programmatic binary download failed.")
            if valid_fallbacks:
                print("[INFO] Discovered URLs (copy-paste to access manually):")
                for fu, rank, label in valid_fallbacks:
                    print(f"  -> [{label}] {fu}")
            print("==============================================")
    else:
        # Launch beautiful GUI
        launch_gui()