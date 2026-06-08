import urllib.parse
import json
from src.core.utils import clean_filename, register_discovered_url
from src.network.client import fetch_html_resilient
from src.network.downloader import download_file

def try_doaj(doi, title):
    """Strategy: Query DOAJ API for article metadata containing direct fulltext links."""
    if not doi:
        return False
    if doi.startswith("http://") or doi.startswith("https://"):
        return False
        
    print("\n--- [STRATEGY] Querying DOAJ API ---")
    query_url = f"https://doaj.org/api/v2/search/articles/doi:{urllib.parse.quote(doi)}"
    register_discovered_url(query_url, "DOAJ API Query")
    
    try:
        res_text = fetch_html_resilient(query_url)
        if res_text:
            data = json.loads(res_text)
            results = data.get('results', [])
            if results:
                article = results[0]
                bibjson = article.get('bibjson', {})
                links = bibjson.get('link', [])
                
                # Sort links to prioritize direct PDFs first
                sorted_links = []
                for l in links:
                    url = l.get('url', '')
                    content_type = l.get('content_type', '').lower()
                    
                    # Direct PDF check
                    if content_type == 'application/pdf' or url.lower().endswith('.pdf'):
                        sorted_links.insert(0, l)
                    else:
                        sorted_links.append(l)
                        
                for l in sorted_links:
                    download_url = l.get('url')
                    if not download_url:
                        continue
                        
                    content_type = l.get('content_type', '').lower()
                    is_pdf = content_type == 'application/pdf' or download_url.lower().endswith('.pdf')
                    
                    # If it's an MDPI landing page, construct the PDF URL directly
                    if not is_pdf and "mdpi.com" in download_url.lower() and not download_url.lower().endswith('/pdf'):
                        download_url = download_url.rstrip('/') + '/pdf'
                        is_pdf = True
                        
                    print(f"[INFO] DOAJ link candidate: {download_url} (is_pdf={is_pdf})")
                    register_discovered_url(download_url, "DOAJ Link")
                    
                    filename = f"DOAJ_{clean_filename(title if title else doi.replace('/', '_'))}.pdf"
                    if download_file(download_url, filename):
                        return True
            else:
                print("[INFO] DOAJ API returned no results for this DOI.")
    except Exception as e:
        print(f"[WARNING] DOAJ lookup failed: {e}")
        
    return False
