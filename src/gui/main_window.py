import os
import sys
import re
import threading
import urllib.parse
import tkinter as tk
from tkinter import ttk

from src.core import state
from src.core.config import VERSION, HEADERS, _TF_DOI_PREFIXES
from src.core.utils import clean_filename, register_discovered_url
from src.network.client import get_user_country
from src.network.downloader import download_file
from src.metadata.crossref import search_crossref, resolve_title_to_doi
from src.metadata.openalex import search_openalex_keyword
from src.metadata.google_scholar import search_google_scholar
from src.metadata.researchgate import resolve_rg_pdf_url
from src.main import run_download_pipeline

from src.gui.yazid_assma import fetch_yazid_rg_publications, fetch_assma_publications
from src.gui.updates import check_updates_gui

# Module-level GUI state variables
is_running = False
research_query = ""
current_page = 1
has_more_results = True
card_buttons = []
prev_btn = None
next_btn = None
page_lbl = None
results_frame = None
results_visible = False
pagination_start_page = 1
max_available_page = None

# Caching and prefetching variables
cached_research_results = {}
prefetched_pages = set()
active_search_query = ""
page_buttons = []
page_num_frame = None
results_container = None

running_event = threading.Event()
_app_mutex = None


def view_document_in_browser(doi, paper_title, is_book=False):
    """Resolve the paper and open it in the default web browser for viewing."""
    def open_thread():
        url = None
        if doi:
            ident = doi.strip()
            if ident.startswith("http://") or ident.startswith("https://"):
                if "researchgate.net/publication/" in doi:
                    url = resolve_rg_pdf_url(doi)
                else:
                    url = doi
            elif ":" in ident:
                prefix, key = ident.split(":", 1)
                prefix = prefix.strip().lower()
                key = key.strip()
                if prefix == "ia":
                    url = f"https://archive.org/details/{key}"
                elif prefix == "isbn":
                    url = f"https://openlibrary.org/isbn/{key}"
                elif prefix == "ol":
                    clean_key = key.lstrip('/')
                    if not clean_key.startswith("works/") and not clean_key.startswith("books/") and not clean_key.startswith("authors/"):
                        clean_key = f"works/{clean_key}"
                    url = f"https://openlibrary.org/{clean_key}"
                else:
                    if is_book:
                        url = f"https://openlibrary.org/search?q={urllib.parse.quote(paper_title)}"
                    else:
                        url = f"https://doi.org/{doi}"
            else:
                if is_book:
                    url = f"https://openlibrary.org/search?q={urllib.parse.quote(paper_title)}"
                else:
                    url = f"https://doi.org/{doi}"
        else:
            # Fallback to search query
            if is_book:
                url = f"https://openlibrary.org/search?q={urllib.parse.quote(paper_title)}"
            else:
                url = f"https://www.google.com/search?q={urllib.parse.quote(paper_title)}"
            
        print(f"\n[INFO] Opening document for viewing in browser: {url}")
        try:
            import webbrowser
            webbrowser.open(url)
        except Exception as e:
            print(f"[ERROR] Failed to open document in browser: {e}")
            
    t = threading.Thread(target=open_thread)
    t.daemon = True
    t.start()


def open_url_in_browser(url):
    """Open a URL in the default browser in a background thread."""
    if not url:
        return
    def open_thread():
        try:
            import webbrowser
            webbrowser.open(url)
        except Exception as e:
            print(f"[ERROR] Failed to open URL in browser: {e}")
    t = threading.Thread(target=open_thread)
    t.daemon = True
    t.start()


def score_and_rank_results(results):
    """Sort and rank results based on Open Access status, recency, and journal diversity."""
    import datetime
    current_year = datetime.datetime.now().year
    
    scored_items = []
    for item in results:
        score = 0.0
        
        # 1. Open Access boost
        is_oa = item.get('is_oa', False)
        journal_name = item.get('journal', '').lower()
        is_known_oa = any(oa in journal_name for oa in ["mdpi", "frontiers", "plos", "springer open", "biomed central", "scielo", "doaj"])
        
        if is_oa:
            score += 100.0
        if is_known_oa:
            score += 80.0
            
        # 2. Recency boost
        year_str = item.get('year', 'n.d.')
        year_val = None
        match = re.search(r'\b(19\d{2}|20\d{2})\b', year_str)
        if match:
            year_val = int(match.group(1))
            
        if year_val:
            year_diff = current_year - year_val
            if year_diff >= 0:
                score += max(0.0, 50.0 - (year_diff * 4.0))
        else:
            score += 10.0
            
        scored_items.append((score, item))
        
    # Sort items by score descending
    scored_items.sort(key=lambda x: x[0], reverse=True)
    
    # 3. Diversity filtering: greedily select unseen journals first
    selected_items = []
    skipped_items = []
    seen_journals = set()
    
    for score, item in scored_items:
        journal = item.get('journal', '').strip().lower()
        if journal and journal not in seen_journals:
            selected_items.append(item)
            seen_journals.add(journal)
        else:
            skipped_items.append(item)
            
    return selected_items + skipped_items


def reset_gui_state(run_button, entry_widget):
    """Restore the GUI button and entry box back to their idle states."""
    global is_running, prev_btn, next_btn, card_buttons
    is_running = False
    run_button.config(text="Search / Download", bg="#8B5CF6", activebackground="#A78BFA", fg="#FFFFFF", activeforeground="#FFFFFF", state='normal')
    entry_widget.config(state='normal')
    
    # Re-enable pagination and cards
    if prev_btn and next_btn:
        update_pagination_states()
    for btn in card_buttons:
        try:
            btn.config(state='normal')
        except:
            pass


def update_pagination_states():
    """Helper to update the enabled/disabled states of pagination controls."""
    global current_page, prev_btn, next_btn, cached_research_results
    if not prev_btn or not next_btn:
        return
        
    if current_page == 1:
        prev_btn.config(state='disabled')
    else:
        prev_btn.config(state='normal')
        
    if (current_page + 1) in cached_research_results:
        next_btn.config(state='normal')
    else:
        next_btn.config(state='disabled')


def run_pipeline_bg(identifier, status_label, log_widget, run_button, entry_widget, root_widget, journal_url=None):
    """Run the download pipeline in a background thread and output logs to the GUI."""
    state.discovered_urls = []
    if journal_url:
        register_discovered_url(journal_url, "Journal Homepage Fallback")
    
    # Resolve identifier (DOI or Title)
    target_doi = None
    target_title = None
    
    ident = identifier.strip()
    if ident.startswith("10."):
        target_doi = ident
    elif ident.startswith("http://") or ident.startswith("https://"):
        target_doi = ident
    elif any(ident.lower().startswith(prefix) for prefix in ("ia:", "isbn:", "ol:")):
        target_doi = ident
    else:
        target_title = ident
        
    class RedirectText:
        def __init__(self, text_widget):
            self.text_widget = text_widget
        def write(self, string):
            self.text_widget.insert('end', string)
            self.text_widget.see('end')
        def flush(self):
            pass
            
    old_stdout = sys.stdout
    sys.stdout = RedirectText(log_widget)
    
    try:
        if state.abort_requested:
            raise InterruptedError("Cancelled by user")

        if not target_doi and target_title:
            print(f"Beginning Processing Pipeline for Title: '{target_title}'...")
            status_label.config(text="Resolving Title DOI...", fg="#00ADB5")
            target_doi = resolve_title_to_doi(target_title)
        else:
            print(f"Beginning Processing Pipeline for DOI: {target_doi}...")
            
        if target_doi:
            # Register manual fallback URLs in case programmatic downloads fail
            if target_doi.startswith("http://") or target_doi.startswith("https://"):
                register_discovered_url(target_doi, "Direct URL Fallback")
            elif any(target_doi.lower().startswith(prefix) for prefix in ("ia:", "isbn:", "ol:")):
                register_discovered_url(f"https://annas-archive.li/search?q={urllib.parse.quote(target_doi)}", "Anna's Archive Book Search (.li)")
                register_discovered_url(f"https://annas-archive.pk/search?q={urllib.parse.quote(target_doi)}", "Anna's Archive Book Search (.pk)")
            else:
                register_discovered_url(f"https://annas-archive.li/scidb/{urllib.parse.quote(target_doi)}", "Anna's Archive SciDB (.li)")
                register_discovered_url(f"https://annas-archive.pk/scidb/{urllib.parse.quote(target_doi)}", "Anna's Archive SciDB (.pk)")
            
        if state.abort_requested:
            raise InterruptedError("Cancelled by user")

        success = run_download_pipeline(target_doi, target_title, status_label=status_label, root_widget=root_widget)

        if success:
            status_label.config(text="Document Pulled Successfully!", fg="#4CAF50")
            print("\n==============================================")
            print("[PROCESS FINISHED] Document pulled successfully.")
            print("==============================================")
        else:
            # All strategies failed — report failure clearly, no browser popup
            valid_fallbacks = sorted(state.discovered_urls, key=lambda x: x[1])
            status_label.config(text="Download Failed. Publisher blocked all channels.", fg="#F44336")
            print("\n==============================================")
            print("[PROCESS FAILED] Could not retrieve a downloadable PDF.")
            if valid_fallbacks:
                print("[INFO] Discovered URLs (copy-paste to access manually):")
                for fu, rank, label in valid_fallbacks:
                    print(f"  -> [{label}] {fu}")
            print("==============================================")
            
    except InterruptedError:
        status_label.config(text="Research Stopped.", fg="#FF9800")
        print("\n==============================================")
        print("[PROCESS CANCELLED] Stopped by user request.")
        print("==============================================")
    except Exception as ex:
        status_label.config(text="An error occurred during download.", fg="#F44336")
        print(f"\n[ERROR] Thread failed: {ex}")
    finally:
        sys.stdout = old_stdout
        reset_gui_state(run_button, entry_widget)


def create_app_mutex():
    global _app_mutex
    try:
        import ctypes
        _app_mutex = ctypes.windll.kernel32.CreateMutexW(None, False, "AcademicPaperDownloaderMutex")
    except Exception:
        pass


def launch_gui():
    """Launch the modern dark-themed desktop GUI for Paper Downloader."""
    state.GUI_MODE = True
    global prev_btn, next_btn, page_lbl, results_frame, results_container, card_buttons, clear_res_btn, status_label, dl_link_lbl, results_visible, main_container, toggle_console_btn
    
    create_app_mutex()
    
    root = tk.Tk()
    root.title(f"Premium Paper Downloader v{VERSION} by Yazid YOUCEF")
    root.configure(bg="#0D0B14")
    
    # Custom styled scrollbar matching Deep Purple palette
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Vertical.TScrollbar", gripcount=0,
                    background="#2E2543", darkcolor="#1A1625", lightcolor="#1A1625",
                    troughcolor="#1A1625", bordercolor="#1A1625", arrowcolor="#8B5CF6")
    style.map("Vertical.TScrollbar",
              background=[('active', '#8B5CF6'), ('!disabled', '#2E2543')])
    
    # Load and set personalized application icon gracefully
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "app_icon.png")
    _icon_ref = None  # keep a reference to prevent GC
    if os.path.exists(icon_path):
        # Try PIL/Pillow first (handles all PNG types reliably)
        try:
            from PIL import Image, ImageTk
            pil_img = Image.open(icon_path).resize((64, 64), Image.LANCZOS)
            _icon_ref = ImageTk.PhotoImage(pil_img)
            root.iconphoto(True, _icon_ref)
        except ImportError:
            # PIL not installed — fall back to native Tkinter PNG loader
            try:
                _icon_ref = tk.PhotoImage(file=icon_path)
                root.iconphoto(True, _icon_ref)
            except Exception as e:
                print(f"[WARNING] Could not load icon (install Pillow for best results): {e}")
        except Exception as e:
            print(f"[WARNING] Failed to load custom window icon via PIL: {e}")
    
    # Center window on screen (taller to fit permanently visible logs and keyword results)
    w, h = 650, 750
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(True, True)
    try:
        root.state('zoomed')
    except Exception:
        pass
    
    # Header Section (Centered)
    header_frame = tk.Frame(root, bg="#0D0B14", pady=12)
    header_frame.pack(fill='x', padx=25)
    
    # Title & Update symbols container centered beautifully
    title_container = tk.Frame(header_frame, bg="#0D0B14")
    title_container.pack(anchor='center')
    
    header_lbl = tk.Label(title_container, text=f"PAPER DOWNLOADER v{VERSION}", bg="#0D0B14", fg="#A855F7", font=('Segoe UI Semibold', 16))
    header_lbl.pack(side='left')
    
    # Flat spacer label
    tk.Label(title_container, text="  ", bg="#0D0B14").pack(side='left')
    
    # Update interactive label/symbol (🔄)
    update_sym = tk.Label(title_container, text="🔄", bg="#0D0B14", fg="#A78BFA", font=('Segoe UI', 11), cursor="hand2")
    update_sym.pack(side='left', padx=3)
    update_sym.bind("<Button-1>", lambda e: check_updates_gui(root, manual=True))
    
    # Hover states to make elements feel alive
    def on_sym_enter(lbl):
        lbl.config(fg="#C084FC")
        
    def on_sym_leave(lbl):
        lbl.config(fg="#A78BFA")
        
    update_sym.bind("<Enter>", lambda e: on_sym_enter(update_sym))
    update_sym.bind("<Leave>", lambda e: on_sym_leave(update_sym))
    
    sub_lbl = tk.Label(header_frame, text="Enter a DOI to download directly · Enter keywords to search and browse results.", bg="#0D0B14", fg="#A78BFA", font=('Segoe UI', 9))
    sub_lbl.pack(anchor='center', pady=(2, 0))
    
    author_lbl = tk.Label(header_frame, text="Designed & Developed by Yazid YOUCEF", bg="#0D0B14", fg="#8B5CF6", font=('Segoe UI', 8, 'italic'))
    author_lbl.pack(anchor='center', pady=(3, 0))
    
    # Frame to hold updates labels horizontally
    updates_frame = tk.Frame(header_frame, bg="#0D0B14")
    updates_frame.pack(anchor='center', pady=(4, 0))
    
    # Clickable download releases link
    def open_releases(e=None):
        import webbrowser
        webbrowser.open("https://github.com/dzmarkets/Academic-Paper-Downloader/releases")
        
    dl_link_lbl = tk.Label(updates_frame, text="🌐 Get Latest Releases & Updates", bg="#0D0B14", fg="#10B981", font=('Segoe UI Semibold', 9, 'underline'), cursor="hand2")
    dl_link_lbl.pack(side='left')
    dl_link_lbl.bind("<Button-1>", open_releases)
    
    # Hover states to make elements feel alive
    def on_link_enter(e):
        dl_link_lbl.config(fg="#34D399")
        
    def on_link_leave(e):
        dl_link_lbl.config(fg="#10B981")
        
    dl_link_lbl.bind("<Enter>", on_link_enter)
    dl_link_lbl.bind("<Leave>", on_link_leave)

    # Bullet separator (hidden by default)
    sep_lbl = tk.Label(updates_frame, text="  •  ", bg="#0D0B14", fg="#A78BFA", font=('Segoe UI Semibold', 9))

    # Database update link/label (fetches latest Category A/B and Rank data over the web)
    def trigger_db_update(e=None):
        if getattr(state, "db_updating", False):
            return
        state.db_updating = True
        db_update_lbl.config(text="📥 Updating Journal Database...")
        status_label.config(text="Starting journal database update from GitHub...", fg="#3B82F6")
        
        def bg_update():
            from src.network.db_updater import run_db_update
            
            def on_status(txt):
                root.after(0, lambda: status_label.config(text=txt, fg="#3B82F6"))
                
            def on_progress(p):
                root.after(0, lambda: status_label.config(text=f"Updating Database: {p}%...", fg="#3B82F6"))
                
            success = run_db_update(status_callback=on_status, progress_callback=on_progress)
            
            def on_finish():
                state.db_updating = False
                db_update_lbl.config(text="📥 Update Journal Database (Online)")
                if success:
                    status_label.config(text="Journal database updated successfully!", fg="#10B981")
                    sep_lbl.pack_forget()
                    db_update_lbl.pack_forget()
                else:
                    status_label.config(text="Database update failed. Check logs.", fg="#F44336")
                    
            root.after(0, on_finish)
            
        t = threading.Thread(target=bg_update)
        t.daemon = True
        t.start()

    db_update_lbl = tk.Label(updates_frame, text="📥 Update Journal Database (Online)", bg="#0D0B14", fg="#3B82F6", font=('Segoe UI Semibold', 9, 'underline'), cursor="hand2")
    # Packed only when update is available
    
    def on_db_enter(e):
        if not getattr(state, "db_updating", False):
            db_update_lbl.config(fg="#60A5FA")
            
    def on_db_leave(e):
        if not getattr(state, "db_updating", False):
            db_update_lbl.config(fg="#3B82F6")
            
    db_update_lbl.bind("<Enter>", on_db_enter)
    db_update_lbl.bind("<Leave>", on_db_leave)
    db_update_lbl.bind("<Button-1>", trigger_db_update)
    
    # Set references in state
    state.dl_link_lbl = dl_link_lbl
    
    # Dynamic check for database updates
    def check_db_updates_gui():
        def check_db_bg():
            try:
                import urllib.request
                from src.core.utils import get_data_filepath
                from src.network.db_updater import EXTRACTED_URL, RESOLVED_URL
                
                ext_local = get_data_filepath("extracted_journals.json")
                res_local = get_data_filepath("resolved_journal_links.json")
                
                # Show updates if local files don't exist
                if not os.path.exists(ext_local) or not os.path.exists(res_local):
                    root.after(0, show_db_update_ui)
                    return
                    
                local_ext_size = os.path.getsize(ext_local)
                local_res_size = os.path.getsize(res_local)
                
                headers = {'User-Agent': 'Mozilla/5.0'}
                
                # Extracted size
                req_ext = urllib.request.Request(EXTRACTED_URL, method='HEAD', headers=headers)
                with urllib.request.urlopen(req_ext, timeout=5) as resp:
                    online_ext_size = int(resp.getheader('Content-Length', 0))
                    
                # Resolved size
                req_res = urllib.request.Request(RESOLVED_URL, method='HEAD', headers=headers)
                with urllib.request.urlopen(req_res, timeout=5) as resp:
                    online_res_size = int(resp.getheader('Content-Length', 0))
                    
                if online_ext_size != local_ext_size or online_res_size != local_res_size:
                    root.after(0, show_db_update_ui)
            except Exception as e:
                print(f"[WARNING] Failed to check for journal database updates: {e}")
                
        def show_db_update_ui():
            sep_lbl.pack(side='left')
            db_update_lbl.pack(side='left')
            
        t = threading.Thread(target=check_db_bg)
        t.daemon = True
        t.start()
    
    # Silent update check on startup after 1.5 seconds
    root.after(1500, lambda: check_updates_gui(root, manual=False))
    root.after(2000, check_db_updates_gui)

    # Main Input Card (Centered Elements)
    card_frame = tk.Frame(root, bg="#1A1625", bd=1, relief='flat', padx=20, pady=15)
    card_frame.pack(fill='x', padx=25, pady=(5, 5))
    
    # Side-by-side main container
    global main_container
    main_container = tk.Frame(root, bg="#0D0B14")
    main_container.pack(fill='both', expand=True, pady=(0, 10))
    main_container.grid_columnconfigure(0, weight=2)
    main_container.grid_columnconfigure(1, weight=1)
    main_container.grid_rowconfigure(0, weight=1)
    
    input_lbl = tk.Label(card_frame, text="Enter DOI or Keywords:", bg="#1A1625", fg="#EEEEEE", font=('Segoe UI Semibold', 10))
    input_lbl.pack(anchor='center', pady=(8, 5))
    
    # Modern rounded entry emulation
    entry_container = tk.Frame(card_frame, bg="#2E2543", bd=0, padx=8, pady=6)
    entry_container.pack(fill='x', pady=5)
    
    entry = tk.Entry(entry_container, bg="#2E2543", fg="#FFFFFF", insertbackground="#FFFFFF", bd=0, font=('Segoe UI', 11), relief='flat', justify='center')
    entry.pack(fill='x')
    entry.focus_set()
    
    # Status label — always visible
    status_label = tk.Label(card_frame, text="Ready for input.", bg="#1A1625", fg="#A78BFA", font=('Segoe UI', 10, 'italic'))
    status_label.pack(pady=5, anchor='center')
    state.status_label = status_label
    
    # --- Interactive Research Mode Results Frame ---
    results_frame = tk.Frame(main_container, bg="#0D0B14", padx=25)

    # Sub-frame for canvas + scrollbar to separate from pagination and prevent packing squeeze
    canvas_frame = tk.Frame(results_frame, bg="#0D0B14")
    canvas_frame.pack(side='top', fill='both', expand=True)

    # Scrollable canvas wrapper for results
    _results_canvas = tk.Canvas(canvas_frame, bg="#0D0B14", highlightthickness=0)
    _results_scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=_results_canvas.yview, style="Vertical.TScrollbar")
    _results_canvas.configure(yscrollcommand=_results_scrollbar.set)
    _results_scrollbar.pack(side="right", fill="y")
    _results_canvas.pack(side="left", fill="both", expand=True)

    results_container = tk.Frame(_results_canvas, bg="#0D0B14")
    _results_canvas_window = _results_canvas.create_window((0, 0), window=results_container, anchor="nw")

    def _on_results_frame_configure(event):
        _results_canvas.configure(scrollregion=_results_canvas.bbox("all"))
        # Decide canvas height: fit content up to 300px, then scroll
        content_h = results_container.winfo_reqheight()
        canvas_h = min(content_h, 300)
        _results_canvas.configure(height=canvas_h)
        # Also update wraplength on all visible cards
        new_width = _results_canvas.winfo_width()
        new_wrap = max(300, new_width - 180)
        for card in results_container.winfo_children():
            try:
                details_f = card.winfo_children()[0]
                children = details_f.winfo_children()
                if len(children) >= 1:
                    children[0].config(wraplength=new_wrap)
                if len(children) >= 3:
                    children[2].config(wraplength=new_wrap)
            except Exception:
                pass

    def _on_canvas_width_change(event):
        _results_canvas.itemconfig(_results_canvas_window, width=event.width)

    results_container.bind("<Configure>", _on_results_frame_configure)
    _results_canvas.bind("<Configure>", _on_canvas_width_change)

    # Mouse-wheel scrolling (Windows)
    def _on_mousewheel(event):
        _results_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    _results_canvas.bind_all("<MouseWheel>", _on_mousewheel)

    def clear_research_results(clear_cache=True):
        """Clear all loaded paper cards from the research view."""
        global card_buttons, cached_research_results, prefetched_pages, active_search_query, max_available_page, results_visible
        for widget in results_container.winfo_children():
            widget.destroy()
        card_buttons = []
        _results_canvas.yview_moveto(0)  # Reset scroll to top
        
        if clear_cache:
            nav_frame.pack_forget()          # Hide nav bar together with results
            results_visible = False
            _update_grid_layout()
            entry.delete(0, tk.END)
            status_label.config(text="Ready for input.", fg="#A78BFA")
            
            # Clear search cache and reset page numbers UI
            cached_research_results.clear()
            prefetched_pages.clear()
            active_search_query = ""
            max_available_page = None
            reset_page_buttons_ui()

    # Navigation bar — placed AFTER the canvas so it appears at the bottom of results
    nav_frame = tk.Frame(results_frame, bg="#0D0B14", pady=5)

    def on_prev_click():
        global current_page, research_query
        if current_page > 1:
            load_research_page(research_query, current_page - 1)

    def on_next_click():
        global current_page, research_query
        load_research_page(research_query, current_page + 1)

    prev_btn = tk.Button(nav_frame, text="◄ Previous", bg="#2E2543", fg="#EEEEEE", activebackground="#3F335C", activeforeground="#FFFFFF", disabledforeground="#8E8A9F", bd=0, font=('Segoe UI', 9), padx=12, pady=4, cursor="hand2", command=on_prev_click, state='disabled')
    prev_btn.pack(side='left', padx=15)

    global page_buttons, page_num_frame, page_lbl
    page_buttons = []
    page_num_frame = tk.Frame(nav_frame, bg="#0D0B14")
    page_num_frame.pack(side='left', fill='x', expand=True)

    page_subframe = tk.Frame(page_num_frame, bg="#0D0B14")
    page_subframe.pack(anchor='center')

    page_lbl = tk.Label(page_subframe, text="Page", bg="#0D0B14", fg="#8E8A9F", font=('Segoe UI Semibold', 9))
    page_lbl.pack(side='left', padx=(0, 6))

    for p in range(1, 11):
        btn = tk.Button(
            page_subframe,
            text=str(p),
            bg="#1E1A2B",
            fg="#6B7280",
            activebackground="#3F335C",
            activeforeground="#FFFFFF",
            disabledforeground="#4B5563",
            bd=0,
            font=('Segoe UI Semibold', 9),
            padx=8,
            pady=3,
            cursor="hand2",
            state='disabled',
            command=lambda p_idx=p: load_cached_page(p_idx)
        )
        btn.pack(side='left', padx=3)
        page_buttons.append(btn)

    clear_res_btn = tk.Button(nav_frame, text="Clear Results", bg="#2E2543", fg="#EEEEEE", activebackground="#D32F2F", activeforeground="#FFFFFF", disabledforeground="#8E8A9F", bd=0, font=('Segoe UI Semibold', 9), padx=12, pady=4, cursor="hand2", command=clear_research_results)
    clear_res_btn.pack(side='right', padx=(0, 15))

    next_btn = tk.Button(nav_frame, text="Next ►", bg="#2E2543", fg="#EEEEEE", activebackground="#3F335C", activeforeground="#FFFFFF", disabledforeground="#8E8A9F", bd=0, font=('Segoe UI', 9), padx=12, pady=4, cursor="hand2", command=on_next_click)
    next_btn.pack(side='right', padx=15)

    # ── Console / Logs area ────────────────────────────────────────────────────
    # The header is always visible; the body (log_area) can be toggled.
    logs_frame = tk.Frame(main_container, bg="#0D0B14", padx=25)

    logs_header = tk.Frame(logs_frame, bg="#0D0B14")
    logs_header.pack(fill='x', pady=(0, 4))

    console_lbl = tk.Label(logs_header, text="📜  Pipeline Console Logs",
                           bg="#0D0B14", fg="#A78BFA", font=('Segoe UI Semibold', 9))
    console_lbl.pack(side='left')

    # Collapsible body frame that holds log_area + its scrollbar
    _console_body = tk.Frame(logs_frame, bg="#0D0B14")
    _console_body.pack(fill='both', expand=True)
    _console_visible = [True]   # mutable flag

    def _update_grid_layout():
        try:
            results_frame.grid_forget()
            logs_frame.grid_forget()
            
            is_results_visible = results_visible
            is_logs_visible = _console_visible[0]
            
            if is_results_visible and is_logs_visible:
                main_container.grid_columnconfigure(0, weight=2, uniform="group1")
                main_container.grid_columnconfigure(1, weight=1, uniform="group1")
                results_frame.grid(row=0, column=0, sticky='nsew', padx=(25, 10))
                logs_frame.grid(row=0, column=1, sticky='nsew', padx=(10, 25))
            elif is_results_visible and not is_logs_visible:
                main_container.grid_columnconfigure(0, weight=1, uniform="")
                main_container.grid_columnconfigure(1, weight=0, uniform="")
                results_frame.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=25)
            elif not is_results_visible and is_logs_visible:
                main_container.grid_columnconfigure(0, weight=0, uniform="")
                main_container.grid_columnconfigure(1, weight=1, uniform="")
                logs_frame.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=25)
        except Exception as e:
            print(f"[ERROR] Grid update failed: {e}")

    def _toggle_console():
        if _console_visible[0]:
            _console_visible[0] = False
            toggle_console_btn.config(text="Show Console [+]")
        else:
            _console_visible[0] = True
            toggle_console_btn.config(text="Hide Console [-]")
        _update_grid_layout()

    def _force_show_console():
        if not _console_visible[0]:
            _console_visible[0] = True
            toggle_console_btn.config(text="Hide Console [-]")
            _update_grid_layout()

    def clear_logs():
        log_area.delete('1.0', 'end')

    clear_btn = tk.Button(
        logs_header,
        text="Clear Logs",
        bg="#2E2543",
        fg="#EEEEEE",
        activebackground="#3F335C",
        activeforeground="#FFFFFF",
        disabledforeground="#8E8A9F",
        bd=0,
        font=('Segoe UI Semibold', 8),
        padx=10,
        pady=2,
        cursor="hand2",
        command=clear_logs
    )
    clear_btn.pack(side='right')

    log_area = tk.Text(_console_body, bg="#1A1625", fg="#F3E8FF", insertbackground="#FFFFFF",
                       bd=0, font=('Consolas', 9), relief='flat', height=10)
    scrollbar = ttk.Scrollbar(_console_body, orient="vertical", command=log_area.yview,
                              style="Vertical.TScrollbar")
    log_area.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    log_area.pack(side="left", fill="both", expand=True)
    
    if getattr(state, "first_run_changelog", None):
        log_area.insert('end', state.first_run_changelog)
        log_area.see('end')
    
    
    def animate_loading(label, run_event, count=0):
        if not run_event.is_set():
            return
        dots = "." * ((count % 3) + 1)
        spaces = " " * (3 - len(dots))
        label.config(text=f"Processing Pipeline {dots}{spaces}")
        root.after(400, lambda: animate_loading(label, run_event, count + 1))
        
    def reset_inputs():
        """Re-enable all input fields (called after any operation completes)."""
        entry.config(state='normal')
        clear_res_btn.config(state='normal')
        
    def start_individual_download(doi, paper_title, journal_url=None):
        """Trigger threaded background downloader for a specific result card's DOI."""
        global is_running
        
        # Disable all UI controls to prevent multiple actions
        is_running = True
        state.abort_requested = False
        
        entry.config(state='disabled')
        run_button.config(text="Stop Downloading", bg="#D32F2F", activebackground="#EF5350", fg="#FFFFFF", activeforeground="#FFFFFF", state='normal')
        prev_btn.config(state='disabled')
        next_btn.config(state='disabled')
        clear_res_btn.config(state='disabled')
        for btn in card_buttons:
            btn.config(state='disabled')
            
        status_label.config(text="Downloading paper...", fg="#A855F7")
        _force_show_console()
        running_event.set()
        animate_loading(status_label, running_event)
        
        # Clear log area
        log_area.delete('1.0', 'end')
        
        def dl_thread():
            try:
                # Use DOI if present, fallback to exact Title
                target = doi if doi else paper_title
                run_pipeline_bg(target, status_label, log_area, run_button, entry, root, journal_url=journal_url)
            finally:
                running_event.clear()
                
        t = threading.Thread(target=dl_thread)
        t.daemon = True
        t.start()
        
    def update_pagination_buttons_ui():
        global page_buttons, pagination_start_page, current_page, cached_research_results, max_available_page
        if not page_buttons:
            return
            
        # Unpack all buttons first to maintain correct sequence
        for btn in page_buttons:
            btn.pack_forget()
            
        # Pack and style visible buttons based on cache / active page
        for i in range(10):
            p = pagination_start_page + i
            btn = page_buttons[i]
            
            # Rebind button configuration dynamically
            btn.config(text=str(p), command=lambda p_idx=p: load_cached_page(p_idx))
            
            # Determine visibility:
            # We show a button if:
            # - p is <= max_available_page (if max_available_page is set)
            # - OR max_available_page is None (we show all 10 buttons of the current block)
            show_btn = False
            if max_available_page is None:
                show_btn = True
            else:
                if p <= max_available_page:
                    show_btn = True
                    
            if show_btn:
                btn.pack(side='left', padx=3)
                if p in cached_research_results:
                    if p == current_page:
                        btn.config(state='normal', bg="#8B5CF6", fg="#FFFFFF")
                    else:
                        btn.config(state='normal', bg="#2E2543", fg="#EEEEEE")
                else:
                    # Not cached yet
                    if p == current_page:
                        btn.config(state='normal', bg="#8B5CF6", fg="#FFFFFF")
                    else:
                        btn.config(state='disabled', bg="#1E1A2B", fg="#6B7280")

    def reset_page_buttons_ui():
        global pagination_start_page, current_page, max_available_page
        pagination_start_page = 1
        current_page = 1
        max_available_page = None
        update_pagination_buttons_ui()

    def enable_page_button(page_idx):
        update_pagination_buttons_ui()
        update_pagination_states()

    def update_page_buttons_style(active_page):
        update_pagination_buttons_ui()

    def load_cached_page(page_idx):
        global current_page, research_query, cached_research_results
        if page_idx in cached_research_results:
            display_research_results(cached_research_results[page_idx], research_query, page_idx)

    def on_prefetch_complete(query):
        global active_search_query
        if active_search_query == query:
            if state.abort_requested:
                status_label.config(text="Search stopped by user.", fg="#F44336")
            else:
                pages_found = len(cached_research_results)
                if pages_found > 0:
                    status_label.config(text=f"Search complete. Found {pages_found} pages of results.", fg="#4CAF50")
                else:
                    status_label.config(text="No matching documents found.", fg="#F44336")
            reset_gui_state(run_button, entry)
            reset_inputs()
            # Final update to ensure buttons visibility aligns with search completeness
            update_pagination_buttons_ui()

    def start_background_prefetch(query, clear_cache=True):
        global active_search_query, cached_research_results, prefetched_pages, pagination_start_page, max_available_page
        active_search_query = query
        if clear_cache:
            cached_research_results.clear()
            prefetched_pages.clear()
            pagination_start_page = 1
            max_available_page = None
            reset_page_buttons_ui()
        else:
            max_available_page = None
            update_pagination_buttons_ui()
        
        def prefetch_loop():
            global active_search_query, max_available_page
            
            start_p = pagination_start_page
            end_p = pagination_start_page + 9
            
            for p in range(start_p, end_p + 1):
                if state.abort_requested:
                    break
                if active_search_query != query:
                    break
                    
                # Skip already cached pages (e.g. page 10 when shifting to 10-19 range)
                if p in cached_research_results and cached_research_results[p]:
                    continue
                    
                try:
                    # 1. Fetch priority works
                    yazid_works = fetch_yazid_rg_publications()
                    assma_works = fetch_assma_publications()
                    priority_works = yazid_works + assma_works
                    
                    # Deduplicate priority works by title to prevent duplicates
                    seen_priority = set()
                    unique_priority = []
                    for w in priority_works:
                        t_low = w['title'].lower().strip()
                        if t_low not in seen_priority:
                            seen_priority.add(t_low)
                            unique_priority.append(w)
                    priority_works = unique_priority
                    
                    # 2. Check for matches against keywords
                    stripped = query.strip()
                    is_exact = (stripped.startswith('"') and stripped.endswith('"')) or (stripped.startswith("'") and stripped.endswith("'"))
                    exact_phrase = stripped.strip('"').strip("'").strip() if is_exact else None
                    
                    matching_priority = []
                    query_words = [w.lower() for w in re.split(r'\W+', query) if len(w) > 2]
                    
                    for work in priority_works:
                        title_lower = work['title'].lower()
                        authors_lower = work['authors'].lower()
                        is_match = False
                        
                        if not query_words:
                            is_match = True
                        elif "yazid" in query.lower() or "youcef" in query.lower():
                            if "yazid" in authors_lower or "youcef" in authors_lower:
                                is_match = True
                        elif "assma" in query.lower() or "derdoukh" in query.lower():
                            if "assma" in authors_lower or "derdoukh" in authors_lower:
                                is_match = True
                        elif exact_phrase:
                            phrase = exact_phrase.lower()
                            if (phrase in title_lower) or (phrase in authors_lower):
                                is_match = True
                        else:
                            for word in query_words:
                                if word in title_lower or word in authors_lower:
                                    is_match = True
                                    break
                                    
                        if is_match:
                            matching_priority.append(work)
                    
                    effective_priority = min(5, len(matching_priority))
                    if p == 1:
                        adjusted_offset = 0
                    else:
                        adjusted_offset = (p - 1) * 5 - effective_priority
                        
                    # Fetch results from Crossref, OpenAlex, and Scholar
                    crossref_results = search_crossref(query, offset=adjusted_offset, rows=15, type_filter="Papers", author="")
                    openalex_results = search_openalex_keyword(query, offset=adjusted_offset, rows=15, type_filter="Papers")
                    scholar_results = search_google_scholar(query, offset=adjusted_offset, rows=15)
                    
                    results = []
                    results.extend(crossref_results)
                    for r in openalex_results:
                        if not any(r['title'].lower() in x['title'].lower() or x['title'].lower() in r['title'].lower() or (r['doi'] and r['doi'] == x['doi']) for x in results):
                            results.append(r)
                    for r in scholar_results:
                        if not any(r['title'].lower() in x['title'].lower() or x['title'].lower() in r['title'].lower() or (r['doi'] and r['doi'] == x['doi']) for x in results):
                            results.append(r)
                            
                    # Prioritize and rank results
                    results = score_and_rank_results(results)
                            
                    if p == 1 and matching_priority:
                        cleaned_results = []
                        for r in results:
                            if not any(y['title'].lower() in r['title'].lower() or r['title'].lower() in y['title'].lower() for y in matching_priority):
                                cleaned_results.append(r)
                        results = matching_priority + cleaned_results
                        
                    results = results[:5]
                    
                    if state.abort_requested or active_search_query != query:
                        break
                        
                    cached_research_results[p] = results
                    prefetched_pages.add(p)
                    
                    if p == 1:
                        running_event.clear()  # Stop loading animation
                        if results:
                            root.after(0, lambda r=results: display_research_results(r, query, 1))
                            root.after(0, lambda: status_label.config(text="Page 1 loaded. Fetching subsequent pages in background...", fg="#10B981"))
                        else:
                            max_available_page = 1
                            root.after(0, lambda: display_research_results([], query, 1))
                            break
                    else:
                        if results:
                            root.after(0, lambda p_idx=p: enable_page_button(p_idx))
                        else:
                            max_available_page = p - 1
                            root.after(0, update_pagination_buttons_ui)
                            break
                            
                except Exception as e:
                    print(f"[WARNING] Prefetch page {p} failed: {e}")
                    if p == 1:
                        running_event.clear()
                        root.after(0, lambda: status_label.config(text="Failed to fetch search results.", fg="#F44336"))
                        root.after(0, lambda: reset_gui_state(run_button, entry))
                        root.after(0, reset_inputs)
                        break
                        
                import time
                time.sleep(0.5)
                
            running_event.clear()
            root.after(0, lambda: on_prefetch_complete(query))
            
        t_prefetch = threading.Thread(target=prefetch_loop)
        t_prefetch.daemon = True
        t_prefetch.start()

    def display_research_results(results, query, page):
        """Render the 5 results cards dynamically into the results frame."""
        global current_page, research_query, card_buttons, has_more_results, pagination_start_page, results_visible
        
        if not results:
            if page > 1:
                status_label.config(text="No more results available.", fg="#FBBF24")
                current_page = page - 1
                update_page_buttons_style(current_page)
                update_pagination_states()
                reset_gui_state(run_button, entry)
                return
            else:
                status_label.config(text="No matching documents found.", fg="#F44336")
                clear_research_results()
                reset_gui_state(run_button, entry)
                reset_inputs()
                return
                
        # Shift pagination range if necessary
        if page == pagination_start_page + 9:
            pagination_start_page = page
            # Prefetch the next window of pages (e.g. from page + 1 to page + 9)
            start_background_prefetch(query, clear_cache=False)
        elif page < pagination_start_page:
            pagination_start_page = max(1, page - 8)
            start_background_prefetch(query, clear_cache=False)
            
        current_page = page
        research_query = query
        card_buttons = []
        has_more_results = (len(results) == 5)
        
        clear_research_results(clear_cache=False)

        results_visible = True
        _update_grid_layout()
        nav_frame.pack(side='bottom', fill='x', pady=5)          # nav at the bottom of results_frame
        _results_canvas.yview_moveto(0)   # Always scroll back to top on new results
        update_page_buttons_style(page)
        update_pagination_states()
        
        # Determine initial dynamic wraplength
        current_wrap = max(380, results_container.winfo_width() - 180)
        
        # Build 5 dynamic results cards
        for idx, result in enumerate(results):
            card = tk.Frame(results_container, bg="#1A1625", pady=6, padx=12, bd=0)
            card.pack(fill='x', pady=3)
            
            # Left panel - Paper details
            details_f = tk.Frame(card, bg="#1A1625")
            details_f.pack(side='left', fill='both', expand=True)
            
            title_lbl = tk.Label(details_f, text=f"{idx+1}. {result['title']}", bg="#1A1625", fg="#FFFFFF", font=('Segoe UI Semibold', 9), anchor='w', wraplength=current_wrap, justify='left')
            title_lbl.pack(anchor='w')
            
            # Format identifier label (DOI for papers)
            raw_id = result['doi']
            is_book = (result.get('source') == 'openlibrary') or (raw_id and any(raw_id.lower().startswith(prefix) for prefix in ("ia:", "isbn:", "ol:")))
            
            if raw_id:
                if raw_id.lower().startswith("ia:"):
                    id_label = "Internet Archive ID"
                    id_val = raw_id.split(":", 1)[1]
                elif raw_id.lower().startswith("isbn:"):
                    id_label = "ISBN"
                    id_val = raw_id.split(":", 1)[1]
                elif raw_id.lower().startswith("ol:"):
                    id_label = "OpenLibrary Key"
                    id_val = raw_id.split(":", 1)[1]
                else:
                    if raw_id.startswith("http://") or raw_id.startswith("https://"):
                        if "researchgate.net" in raw_id:
                            id_label = "DOI"
                            id_val = "N/A"
                        else:
                            id_label = "URL"
                            id_val = raw_id
                    else:
                        id_label = "DOI"
                        id_val = raw_id
                doi_str = f"{id_label}: {id_val}"
            else:
                doi_str = "ISBN/ID: N/A" if is_book else "DOI: N/A"
                
            if is_book:
                can_dl = result.get('can_download', True)  # default True for ia: items
                # Also check T&F DOI prefix (doi like 10.1201/ etc.)
                raw_doi = result.get('doi', '')
                if not can_dl and raw_doi and any(raw_doi.startswith(p) for p in _TF_DOI_PREFIXES):
                    can_dl = True
                if can_dl:
                    badge_text = "  [PDF Download Available]"
                    badge_fg = "#10B981"
                else:
                    badge_text = "  [No Direct PDF Available]"
                    badge_fg = "#6B7280"
            else:
                badge_text = "  [Direct PDF Available]" if result.get('is_oa') else "  [Sci-Hub / ResearchGate Fallback]"
                badge_fg = "#10B981" if result.get('is_oa') else "#8B5CF6"
            
            doi_frame = tk.Frame(details_f, bg="#1A1625")
            doi_frame.pack(anchor='w', pady=(1, 0))
            
            doi_lbl = tk.Label(doi_frame, text=doi_str, bg="#1A1625", fg="#A78BFA", font=('Segoe UI', 8, 'italic'), anchor='w')
            doi_lbl.pack(side='left')
            
            badge_lbl = tk.Label(doi_frame, text=badge_text, bg="#1A1625", fg=badge_fg, font=('Segoe UI Semibold', 8), anchor='w')
            badge_lbl.pack(side='left')
            
            # Render Year Badge in doi_frame in chroma green
            year_val = result.get('year', 'n.d.')
            year_lbl = tk.Label(doi_frame, text=f"  [{year_val}]", bg="#1A1625", fg="#10B981", font=('Segoe UI Semibold', 8), anchor='w')
            year_lbl.pack(side='left')
            
            # Render Journal Details Label under the DOI frame
            jd = result.get('journal_details')
            raw_issns = result.get('issns', [])
            
            # Gather all unique ISSNs in standardized clean form to avoid duplicates
            seen_clean = set()
            parts = []
            
            def add_issn_display(issn_val, label):
                if not issn_val or issn_val == "N/A":
                    return
                clean = issn_val.strip().replace(" ", "").replace("-", "").upper()
                if clean not in seen_clean:
                    seen_clean.add(clean)
                    if len(clean) == 8:
                        formatted = f"{clean[:4]}-{clean[4:]}"
                    else:
                        formatted = issn_val.strip().upper()
                    parts.append(f"{label}: {formatted}")

            if jd:
                add_issn_display(jd.get('issn'), "ISSN")
                add_issn_display(jd.get('eissn'), "E-ISSN")
                
            for idx, raw_issn in enumerate(raw_issns):
                lbl = "ISSN" if idx == 0 and not any(p.startswith("ISSN:") for p in parts) else "E-ISSN"
                add_issn_display(raw_issn, lbl)
                
            if not parts:
                issn_part = "ISSN: N/A"
            else:
                issn_part = " | ".join(parts)
                
            if jd:
                cat_color = "#10B981" if jd['category'] == "A" else "#3B82F6"
                details_text = f"{issn_part}  •  Category {jd['category']} (Rank: {jd['rank']})"
                details_fg = cat_color
            else:
                details_text = f"{issn_part}  •  Category: Unindexed/Other  •  Rank: N/A"
                details_fg = "#6B7280"
                
            jd_lbl = tk.Label(details_f, text=details_text, bg="#1A1625", fg=details_fg, font=('Segoe UI Semibold', 8), anchor='w')
            jd_lbl.pack(anchor='w', pady=(1, 0))
            
            meta_str = f"Authors: {result['authors']} | {result['journal']} ({result['year']})"
            meta_lbl = tk.Label(details_f, text=meta_str, bg="#1A1625", fg="#9CA3AF", font=('Segoe UI', 8), anchor='w', wraplength=current_wrap, justify='left')
            meta_lbl.pack(anchor='w', pady=(1, 0))
            
            # Right panel - Action Buttons
            btn_container = tk.Frame(card, bg="#1A1625")
            btn_container.pack(side='right', padx=(10, 0))
            
            # Use DOI closure variable
            target_doi = result['doi']
            target_title = result['title']
            
            # Journal Button (if available)
            if result.get('journal_url'):
                journal_btn = tk.Button(
                    btn_container, 
                    text="🌐  Journal", 
                    bg="#06B6D4", 
                    fg="#FFFFFF", 
                    activebackground="#22D3EE", 
                    activeforeground="#FFFFFF", 
                    disabledforeground="#8E8A9F", 
                    bd=0, 
                    font=('Segoe UI Semibold', 9), 
                    width=13, 
                    pady=4, 
                    cursor="hand2", 
                    command=lambda url=result['journal_url']: open_url_in_browser(url)
                )
                journal_btn.pack(side='left', padx=(0, 6))
                card_buttons.append(journal_btn)

            # View Button
            view_btn = tk.Button(
                btn_container, 
                text="👁️  View", 
                bg="#8B5CF6", 
                fg="#FFFFFF", 
                activebackground="#A78BFA", 
                activeforeground="#FFFFFF", 
                disabledforeground="#8E8A9F", 
                bd=0, 
                font=('Segoe UI Semibold', 9), 
                width=13, 
                pady=4, 
                cursor="hand2", 
                command=lambda d=target_doi, t=target_title, ib=is_book: view_document_in_browser(d, t, is_book=ib)
            )
            view_btn.pack(side='left', padx=(0, 6))
            card_buttons.append(view_btn)
            
            # Download Button
            dl_btn = tk.Button(
                btn_container, 
                text="📥  Download", 
                bg="#10B981", 
                fg="#FFFFFF", 
                activebackground="#059669", 
                activeforeground="#FFFFFF", 
                disabledforeground="#8E8A9F", 
                bd=0, 
                font=('Segoe UI Semibold', 9), 
                width=13, 
                pady=4, 
                cursor="hand2", 
                command=lambda d=target_doi, t=target_title, ju=result.get('journal_url'): start_individual_download(d, t, journal_url=ju)
            )
            dl_btn.pack(side='left')
            card_buttons.append(dl_btn)
            
        # Update navigation buttons state
        update_pagination_states()
        
    def load_research_page(query, page):
        """Fetch keyword search results for a page offset.
        Uses cached results if query matches the current active query;
        otherwise triggers background prefetching for pages 1-10.
        """
        global is_running, active_search_query, cached_research_results
        
        # If this page is already cached for the active query, display it instantly!
        if active_search_query == query and page in cached_research_results:
            load_cached_page(page)
            return
            
        # Otherwise, this is a new query. Start background prefetching!
        is_running = True
        state.abort_requested = False
        
        # Disable entry and change search button to stop
        entry.config(state='disabled')
        run_button.config(text="Stop Search", bg="#D32F2F", activebackground="#EF5350", fg="#FFFFFF", activeforeground="#FFFFFF")
        prev_btn.config(state='disabled')
        next_btn.config(state='disabled')
        clear_res_btn.config(state='disabled')
        for btn in card_buttons:
            btn.config(state='disabled')
            
        status_label.config(text="Searching Crossref & OpenAlex...", fg="#A855F7")
        running_event.set()
        animate_loading(status_label, running_event)
        
        start_background_prefetch(query)
        
    def run_thread(identifier):
        try:
            run_pipeline_bg(identifier, status_label, log_area, run_button, entry, root)
        finally:
            running_event.clear()
            
    def handle_button_click():
        global is_running
        
        if not is_running:
            # START ACTION
            identifier = entry.get().strip()
            if not identifier:
                status_label.config(text="Please enter a DOI or keywords first!", fg="#F44336")
                return
            
            # Auto-detect: is this a DOI / identifier, or a keyword query?
            is_doi = (
                identifier.startswith("10.")               # Standard DOI
                or identifier.startswith("http://")        # URL DOI
                or identifier.startswith("https://")
                or any(identifier.lower().startswith(p) for p in ("ia:", "isbn:", "ol:"))  # Book IDs
                or re.match(r'^10\.\d{4,}/\S+$', identifier)  # Strict DOI pattern
            )

            if is_doi:
                # --- DIRECT DOWNLOAD MODE ---
                clear_research_results()
                is_running = True
                state.abort_requested = False
                entry.config(state='disabled')
                run_button.config(text="Stop Downloading", bg="#D32F2F", activebackground="#EF5350", fg="#FFFFFF", activeforeground="#FFFFFF")
                status_label.config(text="Initializing pipeline...", fg="#A855F7")
                _force_show_console()
                running_event.set()
                animate_loading(status_label, running_event)
                log_area.delete('1.0', 'end')
                t = threading.Thread(target=run_thread, args=(identifier,))
                t.daemon = True
                t.start()
            else:
                # --- KEYWORD SEARCH MODE ---
                load_research_page(identifier, 1)
        else:
            # STOP ACTION
            state.abort_requested = True
            status_label.config(text="Stopping...", fg="#FF9800")
            run_button.config(state='disabled')
        
    # Center Search / Download Button
    btn_frame = tk.Frame(card_frame, bg="#1A1625")
    btn_frame.pack(anchor='center', pady=(10, 0))
    
    run_button = tk.Button(btn_frame, text="Search / Download", bg="#8B5CF6", fg="#FFFFFF", activebackground="#A78BFA", activeforeground="#FFFFFF", disabledforeground="#8E8A9F", bd=0, font=('Segoe UI Semibold', 10), padx=25, pady=8, cursor="hand2", command=handle_button_click)
    run_button.pack(side='left', padx=10)
    
    toggle_console_btn = tk.Button(btn_frame, text="Hide Console [-]", bg="#2E2543", fg="#EEEEEE", activebackground="#3F335C", activeforeground="#FFFFFF", bd=0, font=('Segoe UI Semibold', 10), padx=20, pady=8, cursor="hand2", command=_toggle_console)
    toggle_console_btn.pack(side='left', padx=10)
    
    # Style button hover bindings
    def on_btn_enter(e):
        global is_running
        if run_button['state'] != 'disabled':
            if is_running:
                run_button['bg'] = '#EF5350' # Hover state for Stop button (brighter red)
            else:
                run_button['bg'] = '#A78BFA' # Hover state for Download button (brighter purple)
                
    def on_btn_leave(e):
        global is_running
        if run_button['state'] != 'disabled':
            if is_running:
                run_button['bg'] = '#D32F2F' # Idle state for Stop button
            else:
                run_button['bg'] = '#8B5CF6' # Idle state for Download button
            
    run_button.bind("<Enter>", on_btn_enter)
    run_button.bind("<Leave>", on_btn_leave)
    
    # Handle enter key press (only trigger search if not running)
    def on_enter_key(e):
        global is_running
        if not is_running:
            handle_button_click()
    entry.bind("<Return>", on_enter_key)
    
    # ── Algeria-only Support Panel ────────────────────────────────────────────
    # Built but hidden; revealed if country detection confirms Algeria (DZ)
    support_frame = tk.Frame(root, bg="#120F1E", pady=0)
    
    # Thin accent separator
    sep = tk.Frame(support_frame, bg="#8B5CF6", height=1)
    sep.pack(fill='x')
    
    inner = tk.Frame(support_frame, bg="#120F1E", padx=30, pady=12)
    inner.pack(fill='x')
    
    # Left: Services offered (with premium, highly attractive freelance copywriting)
    services_frame = tk.Frame(inner, bg="#120F1E")
    services_frame.pack(side='left', fill='both', expand=True, padx=(0, 20))
    
    services_title = tk.Label(services_frame, text="🚀  Besoin d'un Expert Tech ?",
                               bg="#120F1E", fg="#A855F7", font=('Segoe UI Semibold', 9))
    services_title.pack(anchor='w', pady=(0, 6))
    
    services = [
        ("🌐", "Applications Web Modernes"),
        ("🛒", "E-Commerce & Vitrines Pro"),
        ("📡", "Projets IoT & Domotique"),
    ]
    for icon, label in services:
        row = tk.Frame(services_frame, bg="#120F1E")
        row.pack(anchor='w', pady=1)
        tk.Label(row, text=icon, bg="#120F1E", fg="#C084FC", font=('Segoe UI', 8), width=3, anchor='w').pack(side='left')
        tk.Label(row, text=label, bg="#120F1E", fg="#D1D5DB",
                 font=('Segoe UI', 8)).pack(side='left')
                 
    # Center: Contact & Collaboration (Clean 2nd column)
    contact_frame = tk.Frame(inner, bg="#120F1E")
    contact_frame.pack(side='left', fill='both', expand=True, padx=(20, 20))
    
    contact_title = tk.Label(contact_frame, text="📬  Collaborons Ensemble !",
                             bg="#120F1E", fg="#A855F7", font=('Segoe UI Semibold', 9))
    contact_title.pack(anchor='w', pady=(0, 6))
    
    contacts = [
        ("💬", "WhatsApp : 0661342180"),
        ("📧", "yazid.youcef@gmail.com"),
        ("📍", "Batna, Algérie")
    ]
    for icon, label in contacts:
        row = tk.Frame(contact_frame, bg="#120F1E")
        row.pack(anchor='w', pady=1)
        tk.Label(row, text=icon, bg="#120F1E", fg="#C084FC", font=('Segoe UI', 8), width=3, anchor='w').pack(side='left')
        tk.Label(row, text=label, bg="#120F1E", fg="#D1D5DB",
                 font=('Segoe UI', 8), wraplength=220, justify='left').pack(side='left')
                 
    # Right: Buy Me a Coffee button (Supportive & Inspiring copy)
    bmc_frame = tk.Frame(inner, bg="#120F1E")
    bmc_frame.pack(side='left', fill='both', expand=True, padx=(20, 0))
    
    def open_bmc():
        import re
        import os
 
        # ── Enable ANSI in Windows terminal ───────────────────────────────────
        if os.name == 'nt':
            try:
                os.system('')
            except Exception:
                pass
 
        # ── ANSI colours for terminal ──────────────────────────────────────────
        GOLD       = "\033[1;33m"
        PURPLE     = "\033[1;35m"
        CYAN       = "\033[1;36m"
        GREEN      = "\033[1;32m"
        WHITE_BOLD = "\033[1;37m"
        RESET      = "\033[0m"
 
        terminal_width = 80
 
        # Plain text lines (stripped of ANSI) for in-app console
        # Each entry: (plain_text, tag_name)  tag_name=None means default colour
        styled_lines = [
            ("", None),
            ("* ------------------------------------------------------------- *", "gold"),
            ("  Soutenir l'Innovation Locale / Support Local Innovation [DZ]  ", "purple"),
            ("* ------------------------------------------------------------- *", "gold"),
            ("", None),
            ("Buy Me a Coffee ne fonctionne pas directement en Algerie.", "white_bold"),
            ("Encouragez ce travail par transfert local (Baridimob / CCP).", None),
            ("", None),
            ("Cette application reduit considerablement votre temps de recherche", "cyan"),
            ("en interrogeant simultanement plus de 11 sources academiques majeures", "cyan"),
            ("et en resolvant plus de 65 000 journaux scientifiques en 1 seul clic !", "green"),
            ("", None),
            ("Votre contribution permet de perenniser le developpement de cet outil gratuit.", None),
            ("", None),
            ("Informations de Transfert / Donation Details :", "white_bold"),
            ("-------------------------------------------------------------", None),
            ("Nom Complet :   Yazid Youcef", "cyan"),
            ("RIP CCP :       00799999000605964735", "green"),
            ("-------------------------------------------------------------", None),
            ("", None),
            ("Merci infiniment pour votre generosite et votre soutien ! <3", "gold"),
            ("* ------------------------------------------------------------- *", "gold"),
            ("", None),
        ]
 
        # ── Print to terminal (with ANSI) ──────────────────────────────────────
        ansi_map = {
            "gold":       GOLD,
            "purple":     PURPLE,
            "cyan":       CYAN,
            "green":      GREEN,
            "white_bold": WHITE_BOLD,
            None:         "",
        }
        for plain, tag in styled_lines:
            colour = ansi_map.get(tag, "")
            raw_line = f"{colour}{plain}{RESET}" if colour else plain
            try:
                padding = max(0, (terminal_width - len(plain)) // 2)
                print(" " * padding + raw_line)
            except Exception:
                try:
                    print(plain)
                except Exception:
                    pass
 
        # ── Write into the in-app Pipeline Console log_area ───────────────────
        try:
            # Force the console visible first
            _force_show_console()
            # Colour tag definitions (Tkinter colours)
            tag_colours = {
                "gold":       "#F59E0B",
                "purple":     "#A855F7",
                "cyan":       "#22D3EE",
                "green":      "#10B981",
                "white_bold": "#FFFFFF",
            }
            # Configure tags once (safe to call multiple times)
            for tag_name, hex_colour in tag_colours.items():
                log_area.tag_configure(
                    f"bmc_{tag_name}",
                    foreground=hex_colour,
                    font=('Consolas', 9, 'bold')
                )
            log_area.tag_configure("bmc_normal", foreground="#F3E8FF", font=('Consolas', 9))
 
            log_area.config(state='normal')
            log_area.delete('1.0', 'end')   # Clear logs first for a clean donation display
 
            for plain, tag in styled_lines:
                padding = max(0, (terminal_width - len(plain)) // 2)
                centered = " " * padding + plain
                tk_tag = f"bmc_{tag}" if tag else "bmc_normal"
                log_area.insert('end', centered + "\n", tk_tag)
 
            log_area.see('end')
        except Exception:
            pass
 
 
    # Title for coffee column
    coffee_title = tk.Label(bmc_frame, text="☕  Soutenir mon Travail",
                            bg="#120F1E", fg="#A855F7", font=('Segoe UI Semibold', 9))
    coffee_title.pack(anchor='center', pady=(0, 6))
    
    bmc_btn = tk.Button(
        bmc_frame,
        text="☕  Buy Me a Coffee",
        bg="#FBBF24",
        fg="#1C1410",
        activebackground="#F59E0B",
        activeforeground="#1C1410",
        bd=0,
        font=('Segoe UI Semibold', 9),
        padx=14,
        pady=4,
        cursor="hand2",
        command=open_bmc
    )
    bmc_btn.pack(anchor='center')
    
    rip_lbl = tk.Label(bmc_frame, text="RIP CCP : 00799999000605964735",
                       bg="#120F1E", fg="#10B981", font=('Segoe UI Semibold', 8))
    rip_lbl.pack(pady=(4, 0), anchor='center')
    
    tk.Label(bmc_frame, text="Encourager l'innovation locale 🇩🇿",
             bg="#120F1E", fg="#6B7280", font=('Segoe UI', 7, 'italic')).pack(pady=(2, 0))
    
    def check_country_bg():
        """Background thread: reveal support panel only for Algerian users."""
        country = get_user_country()
        if country == 'DZ':
            root.after(0, lambda: support_frame.pack(fill='x', side='bottom'))
    
    t_geo = threading.Thread(target=check_country_bg)
    t_geo.daemon = True
    t_geo.start()
    # ─────────────────────────────────────────────────────────────────────────
    
    _update_grid_layout()
    root.mainloop()
