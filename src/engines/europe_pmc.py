import urllib.request
import urllib.parse
import json
from src.core.config import HEADERS
from src.core.utils import clean_filename, register_discovered_url
from src.network.downloader import download_file

def try_europe_pmc(doi, title):
    """Strategy 5: Query Europe PMC Open Access Repository."""
    if doi and (doi.startswith("http://") or doi.startswith("https://")):
        return False
        
    if not doi and not title:
        print("\n--- [STRATEGY 5] Skipped (No DOI or Title available) ---")
        return False
        
    print("\n--- [STRATEGY 5] Querying Europe PMC Open Access Repository ---")
    url = None
    if doi:
        url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:{urllib.parse.quote(doi)}&format=json"
    elif title:
        url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22{urllib.parse.quote(title)}%22&format=json"
        
    if not url:
        return False
        
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            
        results = data.get('resultList', {}).get('result', [])
        if results:
            best_match = results[0]
            pmcid = best_match.get('pmcid')
            is_oa = best_match.get('isOpenAccess') == 'Y'
            
            pdf_url = None
            url_list = best_match.get('fullTextUrlList', {}).get('fullTextUrl', [])
            for u in url_list:
                if u.get('documentStyle') == 'pdf' or u.get('availabilityCode') == 'OA':
                    test_url = u.get('url', '')
                    if 'pdf' in test_url.lower() or test_url.endswith('.pdf'):
                        pdf_url = test_url
                        break
                        
            if not pdf_url and is_oa and pmcid:
                pdf_url = f"https://europepmc.org/articles/{pmcid}?pdf=render"
                
            if pdf_url:
                print(f"[INFO] Found Europe PMC PDF Target: {pdf_url}")
                register_discovered_url(pdf_url, "Europe PMC Open Access PDF")
                paper_name = title if title else (pmcid if pmcid else 'europepmc_paper')
                filename = f"pmc_{clean_filename(paper_name)}.pdf"
                return download_file(pdf_url, filename)
            else:
                print("[INFO] Document found on Europe PMC, but no direct PDF link is available.")
        else:
            print("[INFO] No matching document found on Europe PMC.")
    except Exception as e:
        print(f"[WARNING] Europe PMC lookup failed: {e}")
    return False
