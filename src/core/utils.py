import os
import sys
import re
import threading
import urllib.parse
from src.core.config import _FOLDER_FOR_CATEGORY
from src.core import state



def open_in_explorer(filepath):
    """Open the directory containing the file in Windows Explorer and select the file."""
    try:
        import subprocess
        abs_path = os.path.abspath(filepath).replace('/', '\\')
        if os.path.exists(abs_path):
            print(f"[INFO] Opening explorer to highlight file: {abs_path}")
            def run_explorer():
                extra_kwargs = {'creationflags': 0x08000000} if os.name == 'nt' else {}
                subprocess.run(f'explorer /select,"{abs_path}"', shell=True, **extra_kwargs)
            t = threading.Thread(target=run_explorer)
            t.daemon = True
            t.start()
    except Exception as e:
        print(f"[WARNING] Failed to open explorer: {e}")


def get_app_dir():
    """Return the directory that contains the running script / executable.

    When packaged with PyInstaller (sys.frozen is set) the interpreter lives
    inside a temporary _MEI... folder, so we must use sys.executable instead
    of __file__ to locate the real application directory.
    """
    if getattr(sys, 'frozen', False):
        # Running as a PyInstaller bundle — use the .exe location
        return os.path.dirname(os.path.abspath(sys.executable))
    # Running as a plain Python script - return the root project dir (2 levels up from src/core/utils.py)
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def get_documents_dir():
    """Locate the user's Windows Documents directory dynamically."""
    try:
        import ctypes
        from ctypes import wintypes
        buf = ctypes.create_unicode_buffer(wintypes.MAX_PATH)
        # CSIDL_PERSONAL = 5 is the CSIDL for "My Documents" (handles OneDrive redirects cleanly!)
        ctypes.windll.shell32.SHGetFolderPathW(None, 5, None, 0, buf)
        if buf.value:
            return buf.value
    except Exception:
        pass
    # Fallback to standard home directory Documents folder
    return os.path.join(os.path.expanduser('~'), 'Documents')


def get_download_dir(category="paper"):
    """Return (and create if necessary) the Downloads subfolder inside user's Documents.

    Parameters
    ----------
    category : str
        One of ``"paper"``, ``"book"``, ``"thesis"``, or ``"others"``.
        Anything else falls back to ``"Others"``.

    Returns
    -------
    str
        Absolute path to the category subfolder inside Documents, guaranteed to exist.
    """
    folder_name = _FOLDER_FOR_CATEGORY.get(category.lower(), "Others")
    base_dir = os.path.join(get_documents_dir(), "Academic Paper Downloader")
    path = os.path.join(base_dir, folder_name)
    os.makedirs(path, exist_ok=True)
    return path


def clean_filename(title_str):
    """Clean the title so operating systems allow it as a valid filename."""
    return re.sub(r'[\\/*?:"<>|]', "", title_str)


def check_title_similarity(target_title, url):
    """Check if the ResearchGate URL segment matches the target title."""
    if not target_title:
        return True # Can't validate without target title
    
    # Extract the title segment from the URL
    parsed = urllib.parse.urlparse(url)
    path_parts = parsed.path.strip('/').split('/')
    title_segment = None
    for part in path_parts:
        if part.startswith('publication/'):
            subparts = part.split('_', 1)
            if len(subparts) > 1:
                title_segment = subparts[1]
            break
            
    if not title_segment:
        for i, part in enumerate(path_parts):
            if part == 'publication' and i + 1 < len(path_parts):
                next_part = path_parts[i + 1]
                subparts = next_part.split('_', 1)
                if len(subparts) > 1:
                    title_segment = subparts[1]
                else:
                    title_segment = next_part
                break
                
    if not title_segment:
        return True # Fallback if we can't parse title segment
        
    # Clean and compare words
    target_words = set(w.lower() for w in re.split(r'[^a-zA-Z0-9]+', target_title) if len(w) > 2)
    segment_words = set(w.lower() for w in re.split(r'[^a-zA-Z0-9]+', title_segment) if len(w) > 2)
    
    if not target_words or not segment_words:
        return True
        
    # Overlap ratio relative to the smaller set
    shared_words = target_words.intersection(segment_words)
    overlap_ratio = len(shared_words) / min(len(target_words), len(segment_words))
    return overlap_ratio >= 0.8


def register_discovered_url(url, label):
    """Register a URL discovered during the pipeline for fallback web browser launching."""
    if not url:
        return
    # Avoid duplicate URLs
    if url not in [item[0] for item in state.discovered_urls]:
        is_pdf = any(ext in url.lower() for ext in [".pdf", "pdf?", "/pdf/", "/download", "file/"])
        rank = 1 if is_pdf else 2
        state.discovered_urls.append((url, rank, label))


