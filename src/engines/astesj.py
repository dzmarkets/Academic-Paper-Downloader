import urllib.request
import urllib.parse
import re
from src.core.config import HEADERS
from src.core.utils import clean_filename, register_discovered_url
from src.network.downloader import download_file

def try_astesj(doi, title):
    """Strategy: Download papers from ASTESJ (open-access engineering journal).
    
    ASTESJ DOIs: 10.25046/aj{volume}{issue}{sequence}
    Article page: https://doi.org/{doi}  →  redirects to astesj.com article page
    The article page contains a direct PDF download link.
    """
    if not doi:
        return False
    if not doi.startswith("10.25046/"):
        return False
    
    print("\n--- [STRATEGY] Querying ASTESJ (Advances in Science, Technology and Engineering Systems) ---")
    
    # Resolve DOI to get article page URL
    article_url = f"https://doi.org/{doi}"
    print(f"[INFO] Resolving ASTESJ DOI: {article_url}")
    register_discovered_url(f"https://www.astesj.com/", "ASTESJ Journal")
    
    try:
        req = urllib.request.Request(article_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            final_url = resp.geturl()
            html = resp.read().decode('utf-8', errors='ignore')
        
        print(f"[INFO] ASTESJ article page: {final_url}")
        register_discovered_url(final_url, "ASTESJ Article Page")
        
        # Extract direct PDF link from article page
        # Pattern: href=".../ASTESJ_XXXX/XX.pdf" or similar
        pdf_links = re.findall(r'href=["\']([^"\']*\.pdf[^"\']*)["\']', html, re.IGNORECASE)
        
        for link in pdf_links:
            if not link.startswith('http'):
                if link.startswith('/'):
                    base = 'https://www.astesj.com'
                    link = base + link
                else:
                    link = urllib.parse.urljoin(final_url, link)
            link = link.replace('&amp;', '&')
            print(f"[INFO] ASTESJ PDF candidate: {link}")
            register_discovered_url(link, "ASTESJ PDF")
            filename = f"ASTESJ_{clean_filename(title if title else doi.replace('/', '_'))}.pdf"
            if download_file(link, filename, referer=final_url):
                return True
                
    except Exception as e:
        print(f"[WARNING] ASTESJ resolution failed: {e}")
    
    return False
