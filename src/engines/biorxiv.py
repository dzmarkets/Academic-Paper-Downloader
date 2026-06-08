import json
import urllib.parse
from src.core.utils import clean_filename, register_discovered_url
from src.network.client import fetch_html_resilient
from src.network.downloader import download_file

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
