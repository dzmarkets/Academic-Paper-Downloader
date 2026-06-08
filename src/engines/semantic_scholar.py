import urllib.parse
import json
from src.core.utils import clean_filename, register_discovered_url
from src.network.client import fetch_html_resilient
from src.network.downloader import download_file

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
