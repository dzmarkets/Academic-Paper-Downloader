import urllib.parse
import re
from src.core.utils import clean_filename, register_discovered_url
from src.network.client import fetch_html_resilient
from src.network.downloader import download_file

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
