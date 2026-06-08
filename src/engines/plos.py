import urllib.parse
from src.core.utils import clean_filename, register_discovered_url
from src.network.downloader import download_file

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
