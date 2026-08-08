import os
import urllib.request
import urllib.parse
import urllib.error
from src.core import state
from src.core.config import HEADERS
from src.core.utils import get_download_dir, get_app_dir, open_in_explorer

def download_file(url, filename, referer=None, cookie=None, category="paper"):
    """Helper to perform standard binary file downloads with PDF validation.

    Parameters
    ----------
    url : str
        Direct download URL.
    filename : str
        Destination filename (basename only) or absolute path.
    referer : str, optional
        Referer header value.
    cookie : str, optional
        Cookie header value.
    category : str, optional
        Document category used to select the output subfolder.
        One of ``"paper"`` (default), ``"book"``, or ``"thesis"``.
    """
    if state.abort_requested:
        print("[INFO] Download aborted by user.")
        return False

    # Route downloads to the correct named subfolder next to the .exe / script
    downloads_dir = get_download_dir(category)
    if not os.path.isabs(filename):
        filename = os.path.join(downloads_dir, filename)

    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
    except Exception as e:
        print(f"[WARNING] Failed to create parent directory: {e}. Falling back to app root.")
        filename = os.path.join(get_app_dir(), os.path.basename(filename))

    is_pdf = filename.lower().endswith('.pdf')
    content = None
    
    # Build progressive header sets to try (some publishers require specific Accept/Referer combos)
    header_attempts = [
        # Attempt 1: Standard browser headers
        {
            'User-Agent': HEADERS['User-Agent'],
            'Accept': 'application/pdf,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            **(({'Referer': referer}) if referer else {}),
            **(({'Cookie': cookie}) if cookie else {}),
        },
        # Attempt 2: Academic publisher-friendly headers (OUP, Springer, Elsevier)
        {
            'User-Agent': HEADERS['User-Agent'],
            'Accept': 'application/pdf,application/x-pdf,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            **(({'Referer': referer}) if referer else {}),
            **(({'Cookie': cookie}) if cookie else {}),
        },
    ]
    
    for attempt_num, hdrs in enumerate(header_attempts, 1):
        try:
            req = urllib.request.Request(url, headers=hdrs)
            with urllib.request.urlopen(req, timeout=25) as response:
                chunks = []
                while True:
                    if state.abort_requested:
                        print("[INFO] Download aborted by user.")
                        return False
                    chunk = response.read(65536)
                    if not chunk:
                        break
                    chunks.append(chunk)
                content = b"".join(chunks)
            # Validate immediately
            if is_pdf and content and not content.startswith(b'%PDF'):
                content = None  # not a real PDF, try next
                continue
            break  # success
        except Exception as e:
            if attempt_num == 1:
                print(f"[WARNING] urllib download failed: {e}. Trying system curl fallback...")
            content = None

    # Fallback to system curl command if urllib failed
    if not content or (is_pdf and not content.startswith(b'%PDF')):
        try:
            import subprocess
            print(f"[INFO] Bypassing via native system curl...")
            cmd = ["curl", "-s", "-L",
                   "-H", f"User-Agent: {HEADERS['User-Agent']}",
                   "-H", "Accept: application/pdf,*/*;q=0.8"]
            if referer:
                cmd += ["-H", f"Referer: {referer}"]
            if cookie:
                cmd += ["-H", f"Cookie: {cookie}"]
            cmd += ["-o", filename, url]
            extra_kwargs = {'creationflags': 0x08000000} if os.name == 'nt' else {}
            res = subprocess.run(cmd, capture_output=True, **extra_kwargs)
            if res.returncode == 0 and os.path.exists(filename):
                with open(filename, "rb") as f:
                    content = f.read()
        except Exception as curl_err:
            print(f"[ERROR] Native curl fallback failed: {curl_err}")
            return False

    # Validate PDF magic bytes if we expect a PDF
    if is_pdf:
        if not content or not content.startswith(b'%PDF'):
            print(f"[WARNING] Downloaded content from {url} is not a valid PDF! (Size: {len(content) if content else 0} bytes)")
            if content and (b'<html' in content.lower() or b'<!doctype' in content.lower()):
                print("[TIP] The server served an HTML page/blocker instead of the raw PDF.")
            if os.path.exists(filename):
                try:
                    os.remove(filename)
                except:
                    pass
            return False

    # Parallel race guard: bail out if another engine already won
    if state.download_success_event.is_set():
        print(f"[RACE] Another source already won. Discarding result.")
        return False

    with state.download_write_lock:
        # Double-check inside the lock to handle simultaneous finishers
        if state.download_success_event.is_set():
            print(f"[RACE] Lost the write race. Discarding result.")
            return False

        # Ensure content is saved to disk
        with open(filename, "wb") as out_file:
            out_file.write(content)
        state.download_success_event.set()  # Signal: we won the race

    print(f"[SUCCESS] Saved flawlessly inside Downloads folder: '{os.path.basename(filename)}'")
    print(f"[INFO] Absolute Location: {filename}")
    if state.GUI_MODE:
        open_in_explorer(filename)
    return True
