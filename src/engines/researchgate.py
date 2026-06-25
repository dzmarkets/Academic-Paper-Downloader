import re
import urllib.parse
from src.core.config import HEADERS
from src.core.utils import clean_filename, register_discovered_url, check_title_similarity
from src.metadata.doi_resolvers import resolve_doi_metadata, resolve_doi_to_url
from src.metadata.researchgate import search_researchgate_by_author, validate_researchgate_page
from src.network.client import fetch_html_resilient
from src.network.downloader import download_file


def _collect_yahoo(html_body):
    """Extract ResearchGate publication URLs from Yahoo HTML."""
    results = []
    seen = set()
    ru_links = re.findall(r'RU=([^/&"]+)', html_body)
    for val in ru_links:
        unquoted = urllib.parse.unquote(val)
        if "researchgate.net/publication/" not in unquoted:
            continue
        pub_url = unquoted.split('/RK=')[0]
        m = re.match(r'(https?://(?:www\.)?researchgate\.net/publication/\d+_[^/&?"]+)', pub_url)
        if not m:
            m = re.match(r'(https?://(?:www\.)?researchgate\.net/publication/\d+[^/&?"]*)', pub_url)
        if m and m.group(1) not in seen:
            seen.add(m.group(1))
            results.append(m.group(1))
    return results

def _collect_ddg(html_body):
    """Extract ResearchGate publication URLs from DuckDuckGo HTML."""
    results = []
    seen = set()
    encoded_links = re.findall(r'uddg=(https?%3A%2F%2F[^&"]*researchgate\.net%2Fpublication%2F[^&"]*)', html_body)
    for enc_link in encoded_links:
        resolved = urllib.parse.unquote(enc_link).split("&")[0]
        if resolved not in seen:
            seen.add(resolved)
            results.append(resolved)
    direct_links = re.findall(r'href="([^"]*researchgate\.net/publication/[^"]*)"', html_body)
    for link in direct_links:
        resolved = urllib.parse.unquote(link).split("&")[0]
        if resolved not in seen:
            seen.add(resolved)
            results.append(resolved)
    return results

def _collect_bing(html_body):
    """Extract ResearchGate publication URLs from Bing HTML."""
    results = []
    seen = set()
    links = re.findall(r'href="(https?://(?:www\.)?researchgate\.net/publication/[^"&]+)"', html_body)
    for link in links:
        if link not in seen:
            seen.add(link)
            results.append(link)
    return results

def _collect_google(html_body):
    """Extract ResearchGate publication URLs from Google HTML."""
    results = []
    seen = set()
    links = re.findall(r'url\?q=(https://(?:www\.)?researchgate\.net/publication/[^&"()]+)', html_body)
    for link in links:
        unquoted = urllib.parse.unquote(link)
        m = re.match(r'(https?://(?:www\.)?researchgate\.net/publication/\d+_[^/&?"]+)', unquoted)
        if not m:
            m = re.match(r'(https?://(?:www\.)?researchgate\.net/publication/\d+[^/&?"]*)', unquoted)
        if m and m.group(1) not in seen:
            seen.add(m.group(1))
            results.append(m.group(1))
    return results

def _try_validate(candidates, engine_name, title, doi, target_year):
    """Run title-similarity pre-check + page validation on a list of candidates.
    Returns (accepted_url, accepted_html) on first match, or (None, None)."""
    for url in candidates:
        if not check_title_similarity(title, url):
            continue
        print(f"[INFO] {engine_name}: candidate passed URL similarity check: {url}. Fetching to validate...")
        page_src = fetch_html_resilient(url)
        if validate_researchgate_page(page_src, title, doi, target_year):
            return url, page_src
    return None, None


def _resolve_direct_doi(doi, title, target_year):
    """Attempt to resolve DOI to a ResearchGate profile via direct links or DOI resolvers."""
    if not doi:
        return None, None

    rg_profile_url = None
    rg_page_source = None
    
    # 0. Check if DOI is already a direct ResearchGate publication URL
    if "researchgate.net/publication/" in doi:
        rg_profile_url = doi
        print(f"[INFO] Using provided direct ResearchGate publication URL: {rg_profile_url}")
        
    # 1. If it is a ResearchGate specific DOI, attempt direct internal resolver link
    elif doi.strip().startswith("10.13140/"):
        resolver_url = f"https://www.researchgate.net/doi/{doi.strip()}"
        print(f"[INFO] Detected ResearchGate DOI. Attempting direct internal resolver: {resolver_url}")
        try:
            req = urllib.request.Request(resolver_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as response:
                final_url = response.geturl()
                if "researchgate.net/publication/" in final_url:
                    print(f"[INFO] Direct internal resolver redirected to candidate: {final_url}. Fetching page to validate...")
                    page_source = fetch_html_resilient(final_url)
                    if validate_researchgate_page(page_source, title, doi, target_year):
                        rg_profile_url = final_url
                        rg_page_source = page_source
                        print(f"[INFO] Direct internal resolver succeeded and validated: {rg_profile_url}")
        except Exception as e:
            print(f"[WARNING] Direct internal resolver bypassed/failed (usually due to 403 Forbidden): {e}")
            
    # 2. Direct resolution using Crossref / Handle API as fallback
    if not rg_profile_url:
        resolved_url = resolve_doi_to_url(doi)
        if resolved_url:
            print(f"[INFO] Resolving resolved DOI URL: {resolved_url}")
            try:
                req = urllib.request.Request(resolved_url, headers=HEADERS)
                with urllib.request.urlopen(req, timeout=10) as response:
                    final_url = response.geturl()
                    if "researchgate.net/publication/" in final_url:
                        print(f"[INFO] Direct DOI resolution redirected to candidate: {final_url}. Fetching page to validate...")
                        page_source = fetch_html_resilient(final_url)
                        if validate_researchgate_page(page_source, title, doi, target_year):
                            rg_profile_url = final_url
                            rg_page_source = page_source
                            print(f"[INFO] Direct DOI resolution succeeded and validated: {rg_profile_url}")
            except Exception as e:
                print(f"[WARNING] Direct DOI URL resolution bypassed/failed: {e}")
            
    # 3. Direct resolution via doi.org redirect as a fallback
    if not rg_profile_url:
        print(f"[INFO] Attempting direct DOI resolution via doi.org...")
        try:
            url = f"https://doi.org/{doi}"
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as response:
                final_url = response.geturl()
                if "researchgate.net/publication/" in final_url:
                    print(f"[INFO] doi.org resolution redirected to candidate: {final_url}. Fetching page to validate...")
                    page_source = fetch_html_resilient(final_url)
                    if validate_researchgate_page(page_source, title, doi, target_year):
                        rg_profile_url = final_url
                        rg_page_source = page_source
                        print(f"[INFO] Direct DOI resolution succeeded and validated: {rg_profile_url}")
        except Exception as e:
            print(f"[WARNING] Direct DOI resolution bypassed/failed: {e}")
            
    return rg_profile_url, rg_page_source

def _resolve_by_author(doi, title, metadata, target_year):
    """Attempt author-profile-based resolution on ResearchGate as a highly reliable fallback."""
    if not doi or not metadata or not metadata.get('authors'):
        return None, None

    print("[INFO] Attempting author-profile-based resolution on ResearchGate...")
    for author in metadata['authors'][:3]:
        try:
            # search_researchgate_by_author queries Yahoo/DDG for profile, then scrapes it
            pub_entries = search_researchgate_by_author(author)
            for entry in pub_entries:
                entry_url = entry.get('doi')  # search_researchgate_by_author stores publication URL in 'doi'
                if entry_url:
                    # Verify if this is the correct publication using title segment checking
                    if check_title_similarity(title if title else metadata.get('title'), entry_url):
                        print(f"[INFO] Author profile search found candidate: {entry_url}. Fetching page to validate...")
                        page_source = fetch_html_resilient(entry_url)
                        if validate_researchgate_page(page_source, title if title else metadata.get('title'), doi, target_year):
                            rg_profile_url = entry_url
                            rg_page_source = page_source
                            print(f"[INFO] Author profile search resolved and validated ResearchGate publication: {rg_profile_url}")
                            return rg_profile_url, rg_page_source
        except Exception as e:
            print(f"[WARNING] Author-profile-based search failed for '{author}': {e}")

    return None, None


def _search_engines_for_profile(title, doi, target_year):
    """Discover the paper link using search engine queries targeting ResearchGate."""
    search_queries = []
    if title:
        cleaned_title = re.sub(r'\s+', ' ', title).strip().strip('"').strip("'")
        if cleaned_title:
            search_queries.append(f'"{cleaned_title}"')
            search_queries.append(cleaned_title)
    if doi and doi.strip() not in search_queries:
        search_queries.append(doi.strip())

    for search_query in search_queries:
        # ── Yahoo ──────────────────────────────────────────────────────────────
        print(f"[INFO] Searching ResearchGate for {repr(search_query)} via Yahoo...")
        try:
            yahoo_url = f"https://search.yahoo.com/search?p={urllib.parse.quote(search_query + ' site:researchgate.net/publication/')}"
            html = fetch_html_resilient(yahoo_url)
            if html:
                accepted_url, accepted_html = _try_validate(_collect_yahoo(html), "Yahoo", title, doi, target_year)
                if accepted_url:
                    print(f"[INFO] Yahoo resolved and validated ResearchGate publication: {accepted_url}")
                    return accepted_url, accepted_html
        except Exception as e:
            print(f"[WARNING] Yahoo ResearchGate publication search failed: {e}")

        # ── DuckDuckGo ────────────────────────────────────────────────────────
        print(f"[INFO] Searching ResearchGate for {repr(search_query)} via DuckDuckGo...")
        try:
            ddg_url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(search_query + ' site:researchgate.net/publication/')}"
            html = fetch_html_resilient(ddg_url)
            if html:
                accepted_url, accepted_html = _try_validate(_collect_ddg(html), "DuckDuckGo", title, doi, target_year)
                if accepted_url:
                    print(f"[INFO] DuckDuckGo resolved and validated ResearchGate publication: {accepted_url}")
                    return accepted_url, accepted_html
        except Exception as e:
            print(f"[WARNING] DuckDuckGo ResearchGate publication search failed: {e}")

        # ── Bing ──────────────────────────────────────────────────────────────
        print(f"[INFO] Searching ResearchGate for {repr(search_query)} via Bing...")
        try:
            bing_url = f"https://www.bing.com/search?q={urllib.parse.quote(search_query + ' site:researchgate.net/publication/')}&count=10"
            html = fetch_html_resilient(bing_url)
            if html:
                accepted_url, accepted_html = _try_validate(_collect_bing(html), "Bing", title, doi, target_year)
                if accepted_url:
                    print(f"[INFO] Bing resolved and validated ResearchGate publication: {accepted_url}")
                    return accepted_url, accepted_html
        except Exception as e:
            print(f"[WARNING] Bing ResearchGate publication search failed: {e}")
            
        # ── Google ────────────────────────────────────────────────────────────
        print(f"[INFO] Searching ResearchGate for {repr(search_query)} via Google (Best Effort)...")
        try:
            google_url = f"https://www.google.com/search?q={urllib.parse.quote(search_query + ' site:researchgate.net/publication/')}"
            html = fetch_html_resilient(google_url)
            if html:
                accepted_url, accepted_html = _try_validate(_collect_google(html), "Google", title, doi, target_year)
                if accepted_url:
                    print(f"[INFO] Google resolved and validated ResearchGate publication: {accepted_url}")
                    return accepted_url, accepted_html
        except Exception as e:
            print(f"[WARNING] Google ResearchGate publication search failed: {e}")

    return None, None


def _scrape_and_download_profile(rg_profile_url, rg_page_source, title, doi):
    """Scrape the actual profile page for open full-text assets and download."""
    try:
        # Use cached page source if available, otherwise fetch
        if rg_page_source:
            page_source = rg_page_source
        else:
            page_source = fetch_html_resilient(rg_profile_url)
            
        final_profile_url = rg_profile_url
        if not page_source:
            print("[WARNING] Could not fetch ResearchGate publication page source.")
            return False
            
        # Check for standard ResearchGate asset download links 
        # (Usually match: /publication/X_Title/file/Y.pdf or specific token structures)
        pdf_matches = re.findall(r'href="([^"]+\.pdf[^"]*)"', page_source)
        pdf_matches += re.findall(r'["\'](https://www\.researchgate\.net/profile/[^"\']+/publication/[^"\']+/file/[^"\']+ \.pdf)["\']', page_source)
        
        # Fallback to look for raw data-attributes or download endpoints
        pdf_matches += [f"https://www.researchgate.net/{m}" for m in re.findall(r'href="(/publication/[^"]+/file/[^"]+)"', page_source)]
        
        # Highly robust patterns for links, files, and direct download paths
        pdf_matches += re.findall(r'href="([^"]*?publication/\d+[^"]*/link/[a-f0-9]+/download)"', page_source)
        pdf_matches += re.findall(r'href="([^"]*?publication/\d+[^"]*/links/[a-f0-9]+/[^"]+)"', page_source)
        pdf_matches += re.findall(r'href="([^"]*?publication/\d+[^"]*/file/[^"]+)"', page_source)

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
            if link.startswith('publication/'):
                link = '/' + link
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
            
            # Check if this is a "Request full-text" paper versus a "Download full-text" paper
            is_request_full_text = False
            if 'page_source' in locals() and page_source:
                src_lower = page_source.lower()
                has_download = (
                    "download full-text" in src_lower or 
                    "download full text" in src_lower or 
                    "download pdf" in src_lower or
                    "full-text available" in page_source or
                    "Download" in page_source
                )
                has_request = "request full-text" in src_lower or "request full text" in src_lower
                if has_request and not has_download:
                    is_request_full_text = True

            if is_request_full_text:
                fallback_url = rg_profile_url
                print(f"[INFO] 'Request full-text' paper detected. Launching web browser for manual request: {fallback_url}")
            else:
                fallback_url = target_pdf if target_pdf else rg_profile_url
                print(f"[INFO] Public PDF download failed/blocked. Restoring browser launch to view/download manually: {fallback_url}")

            if fallback_url:
                try:
                    import webbrowser
                    webbrowser.open(fallback_url)
                except Exception as browser_err:
                    print(f"[WARNING] Failed to launch web browser: {browser_err}")
            return False
            
    except Exception as e:
        print(f"[WARNING] ResearchGate scraping routine failed: {e}")
        print("[TIP] ResearchGate may be prompting a Captcha verification wall against scripts.")
    return False

def try_researchgate(doi, title):
    """Strategy 3: Automated extraction from ResearchGate."""
    if not doi and not title:
        print("\n--- [STRATEGY 3] Skipped (No DOI or Title available) ---")
        return False
    print("\n--- [STRATEGY 3] Scraping ResearchGate for Full-Text ---")

    target_year = None
    metadata = None
    # Resolve DOI metadata if missing or for validation parameters
    if doi:
        metadata = resolve_doi_metadata(doi)
        if metadata:
            if not title:
                title = metadata.get('title')
                if title:
                    print(f"[INFO] Resolved DOI to exact title: '{title}'")
            target_year = metadata.get('year')

    rg_profile_url, rg_page_source = _resolve_direct_doi(doi, title, target_year)

    if not rg_profile_url and metadata:
        rg_profile_url, rg_page_source = _resolve_by_author(doi, title, metadata, target_year)

    # Step 1: Discover the paper link using search engine queries targeting ResearchGate.
    if not rg_profile_url:
        rg_profile_url, rg_page_source = _search_engines_for_profile(title, doi, target_year)

    if rg_profile_url:
        register_discovered_url(rg_profile_url, "ResearchGate Profile Page")

    if not rg_profile_url:
        print("[INFO] Could not map paper details to a definitive ResearchGate profile.")
        return False

    # Step 2: Scrape the actual profile page for open full-text assets
    return _scrape_and_download_profile(rg_profile_url, rg_page_source, title, doi)
