import re
from src.core.utils import clean_filename, register_discovered_url
from src.network.client import fetch_html_resilient
from src.network.downloader import download_file

def try_ssrn(doi, title):
    """Strategy: Download papers from SSRN (Social Science Research Network).
    
    SSRN DOIs follow the pattern: 10.2139/ssrn.{abstract_id}
    Direct PDF download URL: https://download.ssrn.com/sol3/papers.cfm?abstract_id={id}&download=yes
    Fallback: scrape the abstract page for the embedded PDF link.
    """
    if not doi:
        return False
    
    abstract_id = None
    if doi.startswith("10.2139/ssrn."):
        abstract_id = doi.split("10.2139/ssrn.", 1)[1].strip()
    elif "ssrn.com" in doi:
        # Handle direct SSRN URL passed as DOI
        m = re.search(r'abstract[_=]id[=_](\d+)', doi)
        if m:
            abstract_id = m.group(1)
    
    if not abstract_id:
        return False
    
    print("\n--- [STRATEGY] Querying SSRN (Social Science Research Network) ---")
    print(f"[INFO] SSRN Abstract ID: {abstract_id}")
    
    abstract_page = f"https://papers.ssrn.com/sol3/papers.cfm?abstract_id={abstract_id}"
    register_discovered_url(abstract_page, "SSRN Abstract Page")
    
    # Strategy 1: Direct download endpoint
    direct_url = f"https://download.ssrn.com/sol3/papers.cfm?abstract_id={abstract_id}&download=yes"
    filename = f"SSRN_{abstract_id}_{clean_filename(title) if title else abstract_id}.pdf"
    print(f"[INFO] Trying SSRN direct download: {direct_url}")
    register_discovered_url(direct_url, "SSRN Direct PDF Download")
    if download_file(direct_url, filename, referer=abstract_page):
        return True
    
    # Strategy 2: Scrape abstract page for embedded PDF URL
    print(f"[INFO] Scraping SSRN abstract page for PDF link: {abstract_page}")
    try:
        html = fetch_html_resilient(abstract_page)
        if html:
            # SSRN embeds links like: href="/sol3/Delivery.cfm/.../...pdf?..."
            pdf_links = re.findall(r'href=["\']([^"\']*\.pdf[^"\']*)["\']', html, re.IGNORECASE)
            pdf_links += re.findall(r'href=["\']([^"\']*delivery\.cfm[^"\']*)["\']', html, re.IGNORECASE)
            for link in pdf_links:
                if link.startswith('/'):
                    link = 'https://papers.ssrn.com' + link
                elif not link.startswith('http'):
                    link = 'https://papers.ssrn.com/' + link
                link = link.replace('&amp;', '&')
                print(f"[INFO] SSRN PDF candidate: {link}")
                register_discovered_url(link, "SSRN PDF Link")
                if download_file(link, filename, referer=abstract_page):
                    return True
    except Exception as e:
        print(f"[WARNING] SSRN page scraping failed: {e}")
    
    return False
