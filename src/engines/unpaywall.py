import urllib.request
import json
from src.core.config import UNPAYWALL_EMAIL, HEADERS
from src.core.utils import clean_filename, register_discovered_url
from src.network.downloader import download_file

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
