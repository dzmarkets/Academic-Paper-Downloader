import os
import urllib.parse
from src.core import state
from src.core.config import _TF_DOI_PREFIXES
from src.core.utils import clean_filename, register_discovered_url, get_download_dir, open_in_explorer

def try_download_taylorfrancis(doi, title):
    """Taylor & Francis / CRC Press book downloader via the T&F content API.
    
    The API URL:
        https://api.taylorfrancis.com/content/books/mono/download
        ?identifierName=doi&identifierValue={doi}&type=googlepdf
    
    This returns a 302 redirect to a time-limited signed AWS S3 URL.
    - GET works and follows redirects correctly.
    - HEAD returns 403 on S3 (STS token mismatch), so we use GET only.
    - No institutional login is required for preview PDFs.
    """
    if not doi:
        return False
    # Only attempt for recognised T&F DOI prefixes
    if not any(doi.startswith(p) for p in _TF_DOI_PREFIXES):
        return False
    
    print("\n--- [BOOK STRATEGY] Querying Taylor & Francis Content API ---")
    try:
        import requests as _req
    except ImportError:
        print("[WARNING] 'requests' library not installed. Skipping Taylor & Francis strategy.")
        return False
    
    api_url = (
        f"https://api.taylorfrancis.com/content/books/mono/download"
        f"?identifierName=doi&identifierValue={urllib.parse.quote(doi, safe=':/')}&type=googlepdf"
    )
    print(f"[INFO] T&F API URL: {api_url}")
    register_discovered_url(f"https://www.taylorfrancis.com/books/{urllib.parse.quote(doi, safe=':/.')}", "Taylor & Francis Book Page")
    
    tf_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Accept': 'application/pdf,text/html,application/xhtml+xml,*/*;q=0.8',
        'Referer': 'https://www.taylorfrancis.com/',
    }
    
    try:
        # Stream the response so we can inspect bytes before writing
        r = _req.get(api_url, headers=tf_headers, allow_redirects=True, timeout=30, stream=True)
        
        # Check final resolved URL for diagnostic purposes
        final_url = r.url
        content_type = r.headers.get('Content-Type', '')
        content_length = r.headers.get('Content-Length', 'unknown')
        print(f"[INFO] T&F API → Final URL: {final_url[:80]}...")
        print(f"[INFO] Content-Type: {content_type} | Size: {content_length} bytes")
        
        if r.status_code != 200:
            print(f"[WARNING] T&F API returned HTTP {r.status_code}. Skipping.")
            r.close()
            return False
        
        # Read first 16 bytes to verify it's a real PDF
        first_chunk = next(r.iter_content(16), b'')
        if not first_chunk.startswith(b'%PDF'):
            r.close()
            decoded = first_chunk.decode('utf-8', errors='replace')
            print(f"[WARNING] T&F response is not a PDF. Snippet: {decoded[:80]}")
            return False
        
        # It's a PDF! Stream the rest and save
        filename = f"{clean_filename(title if title else doi)}.pdf"
        downloads_dir = get_download_dir("book")
        pdf_path = os.path.join(downloads_dir, filename)
        
        print(f"[INFO] Downloading T&F PDF to: {pdf_path}")
        byte_count = len(first_chunk)
        with open(pdf_path, 'wb') as f:
            f.write(first_chunk)
            for chunk in r.iter_content(65536):
                if state.abort_requested:
                    r.close()
                    print("[INFO] T&F download aborted by user.")
                    return False
                f.write(chunk)
                byte_count += len(chunk)
        
        r.close()
        print(f"[SUCCESS] T&F PDF saved: '{filename}' ({byte_count:,} bytes)")
        if state.GUI_MODE:
            open_in_explorer(pdf_path)
        return True
    except _req.exceptions.Timeout:
        print("[WARNING] T&F API request timed out (30s).")
    except _req.exceptions.ConnectionError as e:
        print(f"[WARNING] T&F API connection error: {e}")
    except Exception as e:
        print(f"[WARNING] Taylor & Francis download failed: {e}")
    return False
