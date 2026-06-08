import os
import re
import json
import threading
import urllib.request
import urllib.error
import tkinter as tk
from src.core import state
from src.core.config import VERSION, HEADERS

def check_for_updates():
    """Check GitHub for the latest release version of Academic Paper Downloader."""
    url = "https://api.github.com/repos/dzmarkets/Academic-Paper-Downloader/releases/latest"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            latest_version = data.get("tag_name", "").strip().lstrip("v")
            changelog = data.get("body", "")
            # Find direct download link for exe if available, else standard HTML release url
            html_url = data.get("html_url", "https://github.com/dzmarkets/Academic-Paper-Downloader/releases/latest")
            download_url = html_url
            if "assets" in data:
                setup_asset = None
                for asset in data["assets"]:
                    name = asset.get("name", "")
                    if name.endswith("_Setup.exe") or "setup" in name.lower():
                        setup_asset = asset.get("browser_download_url")
                        break
                
                if setup_asset:
                    download_url = setup_asset
                else:
                    for asset in data["assets"]:
                        if asset.get("name", "").endswith(".exe"):
                            download_url = asset.get("browser_download_url", html_url)
                            break
            return latest_version, changelog, download_url
    except urllib.error.HTTPError as e:
        if e.code == 404:
            # 404 means no releases are published yet!
            print("[INFO] No releases found on GitHub. Assuming up-to-date.")
            return VERSION, "No releases published yet on GitHub.", "https://github.com/dzmarkets/Academic-Paper-Downloader"
        print(f"[WARNING] Update check HTTP error: {e}")
        return None, None, None
    except Exception as e:
        print(f"[WARNING] Update check failed: {e}")
        return None, None, None


def start_update_download(parent, latest_version, download_url):
    """Downloads the installer in the background and updates the header label progress."""
    
    # Disable further clicks by unbinding event
    state.dl_link_lbl.unbind("<Button-1>")
    state.dl_link_lbl.unbind("<Enter>")
    state.dl_link_lbl.unbind("<Leave>")
    state.dl_link_lbl.config(text="📥 Initializing download...", fg="#A78BFA", cursor="")
    
    def do_download():
        try:
            import urllib.request
            import tempfile
            import subprocess
            import sys
            
            # Extract filename from the URL or default to setup exe name
            filename = download_url.split('/')[-1]
            if not filename.endswith('.exe'):
                filename = "AcademicPaperDownloader_Setup.exe"
                
            temp_path = os.path.join(tempfile.gettempdir(), filename)
            
            req = urllib.request.Request(download_url, headers=HEADERS)
            with urllib.request.urlopen(req) as response:
                total_size = int(response.info().get('Content-Length', 0))
                downloaded = 0
                
                with open(temp_path, 'wb') as f:
                    block_size = 65536
                    while True:
                        buffer = response.read(block_size)
                        if not buffer:
                            break
                        downloaded += len(buffer)
                        f.write(buffer)
                        
                        if total_size > 0:
                            pct = int(downloaded * 100 / total_size)
                            parent.after(0, lambda p=pct: state.dl_link_lbl.config(text=f"📥 Downloading update: {p}%"))
                        else:
                            parent.after(0, lambda: state.dl_link_lbl.config(text="📥 Downloading update..."))
                            
            # Verify the downloaded file is a valid Windows executable (magic bytes 'MZ')
            if os.path.exists(temp_path):
                with open(temp_path, 'rb') as f:
                    magic = f.read(2)
                if magic != b'MZ':
                    raise ValueError("Downloaded file does not have a valid Windows executable signature.")
                            
            # Launch installer and exit app immediately so the file is not locked
            parent.after(0, lambda: state.dl_link_lbl.config(text="⚡ Launching Installer..."))
            cmd_str = f'cmd.exe /c timeout /t 2 & start "" "{temp_path}" /SILENT /SP- /SUPPRESSMSGBOXES /NORESTART'
            subprocess.Popen(cmd_str, creationflags=0x08000000)
            parent.after(100, lambda: os._exit(0))
            
        except Exception as e:
            print(f"[ERROR] Failed to download update: {e}")
            # Fallback on failure
            parent.after(0, lambda: reset_failed_update(parent, latest_version, download_url))

    def reset_failed_update(parent, latest_version, download_url):
        state.dl_link_lbl.config(
            text="❌ Update Failed. Click to try again.", 
            fg="#EF4444", 
            cursor="hand2"
        )
        # Re-bind click and hover events
        state.dl_link_lbl.bind("<Button-1>", lambda e: start_update_download(parent, latest_version, download_url))
        state.dl_link_lbl.bind("<Enter>", lambda e: state.dl_link_lbl.config(fg="#FCA5A5"))
        state.dl_link_lbl.bind("<Leave>", lambda e: state.dl_link_lbl.config(fg="#EF4444"))

    t = threading.Thread(target=do_download)
    t.daemon = True
    t.start()


def trigger_update_available_ui(parent, latest_version, download_url):
    """Replaces the releases label in the header with an update notification."""
    
    # Change the link label to update action
    state.dl_link_lbl.config(
        text=f"🚀 Update to v{latest_version} available! (Click to Install)", 
        fg="#F59E0B", 
        font=('Segoe UI Semibold', 9, 'underline')
    )
    
    # Bind the click action to start the update process
    state.dl_link_lbl.bind("<Button-1>", lambda e: start_update_download(parent, latest_version, download_url))
    
    # Configure hover states for the update notification
    state.dl_link_lbl.bind("<Enter>", lambda e: state.dl_link_lbl.config(fg="#FBBF24"))
    state.dl_link_lbl.bind("<Leave>", lambda e: state.dl_link_lbl.config(fg="#F59E0B"))


def check_updates_gui(parent, manual=True):
    """Trigger a background thread to check for updates and present the result beautifully."""
    progress_win = None
    if manual:
        progress_win = tk.Toplevel(parent)
        progress_win.title("Checking for Updates")
        progress_win.configure(bg="#0D0B14")
        progress_win.transient(parent)
        progress_win.grab_set()
        
        w, h = 300, 120
        ws = progress_win.winfo_screenwidth()
        hs = progress_win.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        progress_win.geometry(f"{w}x{h}+{int(x)}+{int(y)}")
        progress_win.resizable(False, False)
        
        lbl = tk.Label(progress_win, text="Checking GitHub for updates...", bg="#0D0B14", fg="#A78BFA", font=('Segoe UI', 10), pady=20)
        lbl.pack()
        progress_win.update()
        
    def thread_proc():
        latest_ver, changelog, dl_url = check_for_updates()
        
        if progress_win:
            try:
                progress_win.destroy()
            except Exception:
                pass
                
        if not latest_ver:
            if manual and state.status_label:
                parent.after(0, lambda: state.status_label.config(text="Update check bypassed (offline/no releases found).", fg="#A78BFA"))
            return
            
        def parse_version(v_str):
            parts = []
            for p in re.findall(r'\d+', v_str):
                try:
                    parts.append(int(p))
                except ValueError:
                    pass
            return parts
            
        current_parsed = parse_version(VERSION)
        latest_parsed = parse_version(latest_ver)
        
        is_newer = False
        for c, l in zip(current_parsed, latest_parsed):
            if l > c:
                is_newer = True
                break
            elif c > l:
                break
        else:
            if len(latest_parsed) > len(current_parsed):
                is_newer = True
                
        if is_newer:
            parent.after(0, lambda: trigger_update_available_ui(parent, latest_ver, dl_url))
            if manual and state.status_label:
                parent.after(0, lambda: state.status_label.config(text=f"New version v{latest_ver} available! Click the link at the top to install.", fg="#F59E0B"))
        else:
            if manual and state.status_label:
                parent.after(0, lambda: state.status_label.config(text=f"Academic Paper Downloader is up to date (v{VERSION}).", fg="#10B981"))
                
    t = threading.Thread(target=thread_proc)
    t.daemon = True
    t.start()
