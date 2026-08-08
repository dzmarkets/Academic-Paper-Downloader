# Shared dynamic run-time state
import threading

abort_requested = False
discovered_urls = []
dl_link_lbl = None  # Reference to download link label in the GUI
GUI_MODE = False
status_label = None
first_run_changelog = None

# --- Parallel race state ---
# Set by the first engine that successfully saves a file; causes all others to bail out.
download_success_event = threading.Event()
# Prevents two threads from writing to disk at exactly the same millisecond.
download_write_lock    = threading.Lock()

