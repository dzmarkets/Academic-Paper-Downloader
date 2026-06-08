import urllib.request
import re
from src.core import state
from src.core.config import SCIHUB_DOMAINS, HEADERS
from src.core.utils import register_discovered_url
from src.network.downloader import download_file

def try_scihub(doi):
    """Strategy 2: Repository scrape via Sci-Hub Mirrors."""
    if not doi:
        print("\n--- [STRATEGY 2] Skipped (No DOI available) ---")
        return False
    if doi.startswith("http://") or doi.startswith("https://"):
        return False
        
    print("\n--- [STRATEGY 2] Querying Sci-Hub Shadow Library Mirrors ---")
    for domain in SCIHUB_DOMAINS:
        if state.abort_requested:
            print("[INFO] Sci-Hub strategy aborted.")
            return False
        print(f"[INFO] Trying Sci-Hub mirror: {domain}")
        url = f"{domain}/{doi}"
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as response:
                html = response.read().decode('utf-8', errors='ignore')
            
            # Pull potential PDF URLs from scripts/embeds
            pdf_paths = re.findall(r'[\'"]([^\'"]+\.pdf[^\'"]*)[\'"]', html)
            pdf_paths += re.findall(r'src=([^ >]+\.pdf[^ >]*)', html)
            pdf_paths += re.findall(r'href=([^ >]+\.pdf[^ >]*)', html)
    
            pdf_url = None
            for path in pdf_paths:
                path = path.replace('\\', '')
                if ".pdf" in path:
                    pdf_url = path
                    break
    
            if pdf_url:
                if pdf_url.startswith('//'):
                    pdf_url = 'https:' + pdf_url
                elif pdf_url.startswith('/'):
                    pdf_url = domain + pdf_url
                elif not pdf_url.startswith('http'):
                    pdf_url = f"{domain}/{pdf_url}"
                    
                print(f"[INFO] Found Sci-Hub PDF Target: {pdf_url}")
                register_discovered_url(pdf_url, f"Sci-Hub PDF ({domain})")
                filename = doi.replace("/", "_") + ".pdf"
                if download_file(pdf_url, filename):
                    return True
            else:
                print(f"[INFO] Sci-Hub layout on {domain} hid or didn't contain this file.")
        except Exception as e:
            print(f"[WARNING] Mirror {domain} failed: {e}")
            
    return False
