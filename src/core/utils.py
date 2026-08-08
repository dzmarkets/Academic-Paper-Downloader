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


def get_data_filepath(filename):
    """Return the absolute path to a data file, checking AppData override first, then falling back to PyInstaller/dev base paths."""
    # Check AppData override directory first (handles dynamic online database updates)
    appdata_dir = os.path.join(os.environ.get('APPDATA', os.path.expanduser('~')), "AcademicPaperDownloader", "data")
    override_path = os.path.join(appdata_dir, filename)
    if os.path.exists(override_path):
        return override_path

    # Fallback to packaged/dev path
    if getattr(sys, 'frozen', False):
        # Bundled data folder inside temporary _MEIPASS folder
        base_dir = getattr(sys, '_MEIPASS', None)
        if not base_dir:
            exe_dir = os.path.dirname(os.path.abspath(sys.executable))
            base_dir = os.path.join(exe_dir, "_internal")
            if not os.path.exists(base_dir):
                base_dir = exe_dir
    else:
        # Development mode
        base_dir = get_app_dir()
    return os.path.join(base_dir, "data", filename)


def check_first_run_changelog():
    """Check if this is the first run of the current version.
    Returns the changelog text if yes, or None if it's already been run for this version."""
    from src.core.config import VERSION
    appdata_base = os.path.join(os.environ.get('APPDATA', os.path.expanduser('~')), "AcademicPaperDownloader")
    os.makedirs(appdata_base, exist_ok=True)
    version_file = os.path.join(appdata_base, "last_version.txt")
    
    last_version = ""
    if os.path.exists(version_file):
        try:
            with open(version_file, "r", encoding="utf-8") as f:
                last_version = f.read().strip()
        except Exception:
            pass
            
    if last_version != VERSION:
        # Save current version immediately to prevent displaying changelog again
        try:
            with open(version_file, "w", encoding="utf-8") as f:
                f.write(VERSION)
        except Exception:
            pass
            
        # Return changelog text (v3.0.0.0 release notes without Metadata & Build Updates)
        changelog = (
            "======================================================================\n"
            f"         ACADEMIC PAPER DOWNLOADER - VERSION {VERSION} UPGRADE\n"
            "======================================================================\n\n"
            "What's New in v3.0.0.0:\n\n"
            "📚 Massive Journal Database Expansion\n"
            "- 7 New Integrated Sources: CNRS, AERES, De Gruyter, Erih Plus, Journal Quality, Scopus LT, and Financial Times (FT50).\n"
            "- Enhanced Coverage: Over 65,000+ journals resolved in a single click.\n"
            "- Offline Resiliency: Hardcoded fallbacks to ensure lookup works offline.\n\n"
            "🔍 Advanced Classification & Metadata Engine\n"
            "- Multi-Category Indexing: Real-time classification for Category A (High) and Category B (Medium) journals.\n"
            "- Title-Based Fallback Matching: Retrieve rankings by title when ISSN matching fails.\n"
            "- E-ISSN Resolution: Displays and resolves journals where only E-ISSN is available.\n\n"
            "🎨 Modernized User Interface Enhancements\n"
            "- Refined Header Controls: Aligned \"Get Latest Releases\" and \"Update Journal Database\" side-by-side.\n"
            "- Dynamic Database Update Tracker: Background size check for remote database changes.\n"
            "- Enhanced Search Cards: Integrated full ISSN/E-ISSN values with Category colors.\n\n"
            "======================================================================\n"
        )
        return changelog
    return None


def calculate_title_similarity(t1, t2):
    """Calculate normalized similarity ratio (0.0 to 1.0) between two title strings."""
    if not t1 or not t2:
        return 0.0
    import difflib
    clean_t1 = re.sub(r'[^\w\s]', '', str(t1).lower()).strip()
    clean_t2 = re.sub(r'[^\w\s]', '', str(t2).lower()).strip()
    if clean_t1 == clean_t2:
        return 1.0
    if len(clean_t2) > 10 and clean_t2 in clean_t1:
        return 0.95
    if len(clean_t1) > 10 and clean_t1 in clean_t2:
        return 0.95
    return difflib.SequenceMatcher(None, clean_t1, clean_t2).ratio()



def parse_search_query(raw_query):
    """Parse raw query into title, author, year, and doi components (works with or without quotes).
    
    Handles unquoted inputs like:
    Particle swarm optimization with adaptive mutation for multimodal optimization Hui Wang, Wenjun Wang, Zhijian Wu, 2013
    10.1016/j.amc.2013.06.074 Particle swarm optimization 2013
    """
    if not raw_query:
        return {'title': '', 'author': '', 'year': None, 'doi': None, 'clean_query': ''}
        
    s = raw_query.strip()
    
    # 1. Extract embedded DOI if present
    doi = None
    doi_match = re.search(r'\b(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)', s)
    if doi_match:
        doi = doi_match.group(1).rstrip('.,;)')
        s = s.replace(doi_match.group(0), '').strip()
        
    # 2. Extract publication year (4-digit number between 1900 and 2099)
    year = None
    year_match = re.search(r'\b(19\d{2}|20\d{2})\b', s)
    if year_match:
        year = year_match.group(1)
        s = s[:year_match.start()] + s[year_match.end():]
        s = re.sub(r'\s*,\s*$', '', s.strip())
        
    # 3. Extract title & author
    title = ''
    author = ''
    quote_match = re.search(r'["\']([^"\']+)["\']', s)
    if quote_match:
        title = quote_match.group(1).strip()
        remaining = (s[:quote_match.start()] + ' ' + s[quote_match.end():]).strip()
        author = re.sub(r'^[\s,]+|[\s,]+$', '', remaining)
    else:
        # Unquoted input: check for comma-separated authors at the end
        if ',' in s:
            # Find boundary where author names start (e.g. capitalized Names separated by commas)
            comma_idx = s.find(',')
            # Look backwards from first comma for start of author name (e.g. "Hui Wang, ...")
            pre_comma = s[:comma_idx].rstrip()
            words = pre_comma.split()
            # If last 1-2 words before comma are capitalized name (like Hui Wang), separate title and author
            if len(words) >= 3 and words[-1][0].isupper() and words[-2][0].isupper():
                title = ' '.join(words[:-2]).strip()
                author = ' '.join(words[-2:]) + s[comma_idx:]
            else:
                title = pre_comma
                author = s[comma_idx+1:].strip()
        else:
            title = s.strip()
            author = ''

            
    print("\n" + "="*70)
    print(f"[STEP 1/3] SEARCH QUERY ANALYSIS & ENTITY EXTRACTION")
    print(f"  - Raw Input       : {raw_query}")
    if doi:
        print(f"  - Extracted DOI   : {doi}")
    if year:
        print(f"  - Extracted Year  : {year}")
    if author:
        print(f"  - Extracted Author: {author}")
    print(f"  - Target Title/Text: '{title}'")
    print("="*70)
            
    return {
        'title': title,
        'author': author,
        'year': year,
        'doi': doi,
        'clean_query': raw_query.strip()
    }



