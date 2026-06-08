import urllib.parse
import re
from src.core.utils import clean_filename, register_discovered_url
from src.network.client import fetch_html_resilient
from src.network.downloader import download_file

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
