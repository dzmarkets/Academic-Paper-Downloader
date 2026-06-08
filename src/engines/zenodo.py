import urllib.parse
import json
import re
from src.core.utils import clean_filename, register_discovered_url
from src.network.client import fetch_html_resilient
from src.network.downloader import download_file

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
