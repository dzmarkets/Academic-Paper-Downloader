import re

with open('src/engines/researchgate.py', 'r') as f:
    content = f.read()

scraping_logic = """
def _scrape_and_download_profile(rg_profile_url, rg_page_source, title, doi):
    \"\"\"Scrape the actual profile page for open full-text assets and download.\"\"\"
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
            print("\\n[WARNING] ResearchGate's Cloudflare security walls are actively blocking automated scripts.")

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
"""

content = content.replace("def try_researchgate(doi, title):", scraping_logic + "\ndef try_researchgate(doi, title):")

original_scraping_logic = """    # Step 2: Scrape the actual profile page for open full-text assets
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
    return False"""

replacement = """    # Step 2: Scrape the actual profile page for open full-text assets
    return _scrape_and_download_profile(rg_profile_url, rg_page_source, title, doi)"""

content = content.replace(original_scraping_logic, replacement)

with open('src/engines/researchgate.py', 'w') as f:
    f.write(content)
