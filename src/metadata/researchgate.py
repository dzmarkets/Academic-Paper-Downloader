import re
import urllib.parse
from src.core import state
from src.core.config import HEADERS
from src.network.client import fetch_html_resilient

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


def validate_researchgate_page(html, target_title, target_doi, target_year):
    """Validate if the ResearchGate page HTML matches the target paper metadata."""
    if not html:
        return False
        
    # If it is a Cloudflare block page, bypass validation to allow browser/direct PDF attempts
    if "Security check required" in html or "Temporarily Unavailable" in html:
        print("[INFO] ResearchGate page is blocked by Cloudflare challenge page, validation bypassed.")
        return True

    # 1. Check DOI if available
    if target_doi:
        doi_match = re.search(r'meta\s+[^>]*name=["\']citation_doi["\']\s+content=["\']([^"\']+)["\']', html, re.IGNORECASE)
        if not doi_match:
            doi_match = re.search(r'meta\s+[^>]*content=["\']([^"\']+)["\']\s+name=["\']citation_doi["\']', html, re.IGNORECASE)
        if not doi_match:
            doi_match = re.search(r'meta\s+[^>]*property=["\']citation_doi["\']\s+content=["\']([^"\']+)["\']', html, re.IGNORECASE)
            
        if doi_match:
            page_doi = doi_match.group(1).strip().lower()
            if page_doi == target_doi.strip().lower():
                print(f"[INFO] ResearchGate page validated via matching DOI: {page_doi}")
                return True
            else:
                print(f"[WARNING] ResearchGate page DOI mismatch: '{page_doi}' vs target '{target_doi}'")
                return False

    # 2. Check title similarity
    page_title = None
    title_match = re.search(r'meta\s+[^>]*name=["\']citation_title["\']\s+content=["\']([^"\']+)["\']', html, re.IGNORECASE)
    if not title_match:
        title_match = re.search(r'meta\s+[^>]*property=["\']og:title["\']\s+content=["\']([^"\']+)["\']', html, re.IGNORECASE)
    if not title_match:
        title_match = re.search(r'<title>([^<]+)</title>', html, re.IGNORECASE)
        
    if title_match:
        page_title = title_match.group(1).strip()
        if " - ResearchGate" in page_title:
            page_title = page_title.split(" - ResearchGate")[0].strip()
        if "(PDF)" in page_title:
            page_title = page_title.replace("(PDF)", "").strip()
            
    if target_title and page_title:
        target_words = set(w.lower() for w in re.split(r'\W+', target_title) if len(w) > 2)
        page_words = set(w.lower() for w in re.split(r'\W+', page_title) if len(w) > 2)
        
        if target_words and page_words:
            shared = target_words.intersection(page_words)
            overlap = len(shared) / min(len(target_words), len(page_words))
            if overlap < 0.8:
                print(f"[WARNING] ResearchGate page title mismatch: '{page_title}' vs target '{target_title}'")
                return False

    # 3. Check publication year/date if available (allowing 1 year difference)
    if target_year:
        date_match = re.search(r'meta\s+[^>]*name=["\']citation_publication_date["\']\s+content=["\']([^"\']+)["\']', html, re.IGNORECASE)
        if not date_match:
            date_match = re.search(r'publicationDate["\']:\s*["\'](\d{4})', html)
            
        page_year = None
        if date_match:
            date_str = date_match.group(1)
            year_match = re.search(r'\b(\d{4})\b', date_str)
            if year_match:
                page_year = year_match.group(1)
                
        if page_year:
            try:
                diff = abs(int(page_year) - int(target_year))
                if diff > 1:
                    print(f"[WARNING] ResearchGate page year mismatch: {page_year} vs target {target_year}")
                    return False
            except:
                pass

    return True


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

