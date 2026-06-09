import os
import sys
import urllib.request
import json
from src.core.utils import get_data_filepath

# Raw URLs for the database files on GitHub
EXTRACTED_URL = "https://raw.githubusercontent.com/dzmarkets/Academic-Paper-Downloader/main/data/extracted_journals.json"
RESOLVED_URL = "https://raw.githubusercontent.com/dzmarkets/Academic-Paper-Downloader/main/data/resolved_journal_links.json"

def get_appdata_data_dir():
    """Return the AppData data directory path and create it if necessary."""
    appdata_base = os.path.join(os.environ.get('APPDATA', os.path.expanduser('~')), "AcademicPaperDownloader")
    data_dir = os.path.join(appdata_base, "data")
    os.makedirs(data_dir, exist_ok=True)
    return data_dir

def download_file_with_progress(url, dest_path, progress_callback=None):
    """Download a file from url to dest_path, calling progress_callback with percentage."""
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)
    
    with urllib.request.urlopen(req, timeout=30) as response:
        # Try to get total size if Content-Length header is present
        total_size = response.getheader('Content-Length')
        if total_size:
            total_size = int(total_size)
        else:
            total_size = None
            
        block_size = 1024 * 64 # 64KB blocks
        downloaded = 0
        
        with open(dest_path, 'wb') as f:
            while True:
                block = response.read(block_size)
                if not block:
                    break
                f.write(block)
                downloaded += len(block)
                if total_size and progress_callback:
                    percent = int((downloaded / total_size) * 100)
                    progress_callback(percent)

def run_db_update(status_callback=None, progress_callback=None):
    """Downloads both database files to the AppData override directory.
    
    Parameters
    ----------
    status_callback : callable(str)
        Function to notify status updates.
    progress_callback : callable(int)
        Function to notify progress percentage (0-100).
    """
    try:
        appdata_dir = get_appdata_data_dir()
        
        # Paths to write
        dest_ext = os.path.join(appdata_dir, "extracted_journals.json")
        dest_res = os.path.join(appdata_dir, "resolved_journal_links.json")
        
        if status_callback:
            status_callback("Downloading journal listings (1/2)...")
        
        # Download extracted_journals.json
        def ext_progress(p):
            if progress_callback:
                # First file represents 0% to 40% of total download progress
                progress_callback(int(p * 0.4))
                
        download_file_with_progress(EXTRACTED_URL, dest_ext, progress_callback=ext_progress)
        
        if status_callback:
            status_callback("Downloading resolved link directory (2/2)...")
            
        # Download resolved_journal_links.json
        def res_progress(p):
            if progress_callback:
                # Second file represents 40% to 100% of total download progress
                progress_callback(40 + int(p * 0.6))
                
        download_file_with_progress(RESOLVED_URL, dest_res, progress_callback=res_progress)
        
        if status_callback:
            status_callback("Reloading journal database...")
            
        # Clear the internal cache in src.core.journals so it reloads from the new AppData paths
        from src.core import journals
        journals._journal_details_map = None
        journals._journal_title_map = None
        
        # Trigger reload of details database in the background
        journals.get_journal_details("dummy-issn")
        
        if status_callback:
            status_callback("Database updated successfully!")
        return True
    except Exception as e:
        if status_callback:
            status_callback(f"Database update failed: {e}")
        print(f"[ERROR] Database update failed: {e}")
        return False
