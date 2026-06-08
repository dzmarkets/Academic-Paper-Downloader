import urllib.request
import urllib.parse
import re
from src.core.config import HEADERS
from src.core.utils import clean_filename, register_discovered_url
from src.network.downloader import download_file

def try_arxiv(doi, title):
    """Strategy 4: Query arXiv Open Access Preprint Server."""
    if doi and (doi.startswith("http://") or doi.startswith("https://")):
        return False
        
    if not doi and not title:
        print("\n--- [STRATEGY 4] Skipped (No DOI or Title available) ---")
        return False
        
    print("\n--- [STRATEGY 4] Querying arXiv Open Access Preprint Server ---")
    url = None
    if doi:
        clean_doi = doi.strip()
        url = f"http://export.arxiv.org/api/query?search_query=doi:{urllib.parse.quote(clean_doi)}&max_results=1"
    elif title:
        clean_title = title.strip().strip('"').strip("'")
        url = f"http://export.arxiv.org/api/query?search_query=ti:%22{urllib.parse.quote(clean_title)}%22&max_results=1"
        
    if not url:
        return False
        
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as response:
            xml_data = response.read().decode('utf-8', errors='ignore')
            
        pdf_links = re.findall(r'<link[^>]*?href=["\'](https?://arxiv\.org/pdf/[^"\']+)["\']', xml_data)
        ids = re.findall(r'<id>https?://arxiv\.org/abs/([^<\s]+)</id>', xml_data)
        
        if not pdf_links and ids:
            pdf_links = [f"https://arxiv.org/pdf/{ids[0]}.pdf"]
            
        if pdf_links:
            pdf_url = pdf_links[0]
            if not pdf_url.endswith('.pdf'):
                pdf_url += '.pdf'
            print(f"[INFO] Found arXiv PDF Target: {pdf_url}")
            register_discovered_url(pdf_url, "arXiv Open Access PDF")
            
            paper_name = title if title else (ids[0] if ids else 'arxiv_paper')
            filename = f"arxiv_{clean_filename(paper_name)}.pdf"
            return download_file(pdf_url, filename)
        else:
            print("[INFO] No matching document found on arXiv.")
    except Exception as e:
        print(f"[WARNING] arXiv lookup failed: {e}")
    return False
