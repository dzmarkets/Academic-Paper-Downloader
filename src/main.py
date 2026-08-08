import sys
import concurrent.futures
import urllib.parse
from src.core import state
from src.core.config import _TF_DOI_PREFIXES
from src.core.utils import clean_filename, register_discovered_url
from src.metadata.crossref import resolve_title_to_doi
from src.network.downloader import download_file

# Import all download strategies
from src.engines import (
    try_plos,
    try_biorxiv,
    try_publisher_direct,
    try_download_taylorfrancis,
    try_unpaywall,
    try_semantic_scholar,
    try_zenodo,
    try_doaj,
    try_core,
    try_ssrn,
    try_scihub,
    try_libgen,
    try_arxiv,
    try_astesj,
    try_europe_pmc,
    try_researchgate,
    try_download_book
)


def _run_race(sources, update_status, label_text):
    """Run a list of (name, fn, *args) download sources in parallel.

    Returns True as soon as one callable returns True (sets
    state.download_success_event) or False if all sources are exhausted.

    Parameters
    ----------
    sources      : list of (name: str, fn: callable, *args)
    update_status: callable(text, fg) — updates the GUI status label
    label_text   : str — status bar message shown during the race
    """
    if not sources:
        return False

    update_status(label_text)

    def _worker(name, fn, args):
        if state.abort_requested or state.download_success_event.is_set():
            return False
        print(f"[RACE] Starting: {name}")
        try:
            result = fn(*args)
        except Exception as e:
            print(f"[RACE] {name} raised: {e}")
            result = False
        if result:
            # Set the event here so the poll loop wakes up immediately even
            # when the engine doesn't go through download_file() (e.g. tests).
            state.download_success_event.set()
            print(f"[RACE] \u2705 Winner: {name}")
        return result

    max_workers = min(len(sources), 8)
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)
    try:
        futures = {
            executor.submit(_worker, name, fn, tuple(args)): name
            for name, fn, *args in sources
        }
        # Poll every 200 ms; break as soon as we have a winner or abort
        while not state.download_success_event.is_set() and not state.abort_requested:
            done, _ = concurrent.futures.wait(
                futures, timeout=0.2,
                return_when=concurrent.futures.ALL_COMPLETED
            )
            if len(done) == len(futures):
                break  # All done, none succeeded
    finally:
        # If we have a winner or an abort, don't block waiting for slow threads.
        early_exit = state.download_success_event.is_set() or state.abort_requested
        executor.shutdown(wait=not early_exit, cancel_futures=early_exit)

    return state.download_success_event.is_set()


def run_download_pipeline(target_doi, target_title, status_label=None, root_widget=None):
    """Run all download strategies in a two-tier parallel race until one succeeds."""
    def update_status(text, fg="#00ADB5"):
        if status_label:
            if root_widget:
                root_widget.after(0, lambda: status_label.config(text=text, fg=fg))
            else:
                status_label.config(text=text, fg=fg)

    # Always reset race state at the top so back-to-back downloads work correctly
    state.download_success_event.clear()

    if state.abort_requested:
        raise InterruptedError("Cancelled by user")

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

    is_book_identifier = target_doi and any(target_doi.lower().startswith(prefix) for prefix in ("ia:", "isbn:", "ol:"))

    if is_book_identifier:
        update_status("Querying Book Repositories...")
        return try_download_book(target_doi, target_title, status_label=status_label, root_widget=root_widget)

    # ------------------------------------------------------------------
    # TIER 1 — Fast API race (all lightweight sources run simultaneously)
    # ------------------------------------------------------------------
    tier1_sources = []

    if target_doi:
        # DOI-specific fast-path sources
        if target_doi.lower().startswith("10.1371/"):
            tier1_sources.append(("PLOS", try_plos, target_doi, target_title))
        if target_doi.lower().startswith("10.1101/"):
            tier1_sources.append(("BioRxiv", try_biorxiv, target_doi, target_title))

        # Direct URL shortcut (not for bare ResearchGate publication pages)
        if (target_doi.startswith("http://") or target_doi.startswith("https://")) and \
                ("researchgate.net" not in target_doi or "/links/" in target_doi):
            def _direct_url_download(doi, title):
                result = download_file(doi, clean_filename(title or "Downloaded_Paper") + ".pdf")
                if result:
                    print(f"[SUCCESS] Directly downloaded PDF from URL: {doi}")
                return result
            tier1_sources.append(("Direct URL", _direct_url_download, target_doi, target_title))

        tier1_sources += [
            ("Publisher Direct",  try_publisher_direct,  target_doi, target_title),
            ("Unpaywall",         try_unpaywall,          target_doi),
            ("Semantic Scholar",  try_semantic_scholar,   target_doi, target_title),
            ("Zenodo",            try_zenodo,             target_doi, target_title),
            ("DOAJ",              try_doaj,               target_doi, target_title),
            ("CORE",              try_core,               target_doi, target_title),
            ("SSRN",              try_ssrn,               target_doi, target_title),
            ("arXiv",             try_arxiv,              target_doi, target_title),
            ("ASTESJ",            try_astesj,             target_doi, target_title),
            ("Europe PMC",        try_europe_pmc,         target_doi, target_title),
        ]

        # Taylor & Francis only for known T&F DOI prefixes (fast HTTP, so stays in Tier 1)
        if any(target_doi.startswith(p) for p in _TF_DOI_PREFIXES):
            tier1_sources.append(("Taylor & Francis", try_download_taylorfrancis, target_doi, target_title))
    else:
        # Title-only: can still try the sources that accept a title without a DOI
        tier1_sources += [
            ("arXiv",    try_arxiv,    target_doi, target_title),
            ("ASTESJ",   try_astesj,   target_doi, target_title),
            ("Zenodo",   try_zenodo,   target_doi, target_title),
            ("CORE",     try_core,     target_doi, target_title),
        ]

    success = _run_race(tier1_sources, update_status, "\U0001f50d Searching all open sources...")
    if success:
        return True

    if state.abort_requested:
        raise InterruptedError("Cancelled by user")

    # ------------------------------------------------------------------
    # TIER 2 — Heavy scraper race (subprocess-heavy, run after Tier 1)
    # ------------------------------------------------------------------
    tier2_sources = [
        ("Sci-Hub",            try_scihub,                    target_doi),
        ("LibGen",             try_libgen,                    target_doi, target_title),
        ("ResearchGate",       try_researchgate,              target_doi, target_title),
        ("Taylor & Francis",   try_download_taylorfrancis,   target_doi, target_title),
    ]

    success = _run_race(tier2_sources, update_status, "\U0001f512 Bypassing paywalls...")
    if success:
        return True

    if state.abort_requested:
        raise InterruptedError("Cancelled by user")

    # Final fallback: public-domain book repositories
    update_status("Querying Book Repositories...")
    return try_download_book(target_doi, target_title, status_label=status_label, root_widget=root_widget)



def main():
    from src.core.utils import check_first_run_changelog
    state.first_run_changelog = check_first_run_changelog()
    if state.first_run_changelog:
        try:
            print(state.first_run_changelog)
        except UnicodeEncodeError:
            # Fallback for systems/consoles that don't support UTF-8/emojis
            clean_log = state.first_run_changelog.encode('ascii', errors='ignore').decode('ascii')
            print(clean_log)
        
    # If arguments are passed, run in headless CLI mode. Otherwise, launch GUI.
    if len(sys.argv) > 1:
        state.discovered_urls.clear()
        target_doi = None
        target_title = None

        first_arg = sys.argv[1].strip()
        if first_arg.startswith("10."):
            target_doi = first_arg
            target_title = sys.argv[2] if len(sys.argv) > 2 else None
        elif first_arg.startswith("http://") or first_arg.startswith("https://"):
            target_doi = first_arg
            target_title = sys.argv[2] if len(sys.argv) > 2 else None
        elif any(first_arg.lower().startswith(prefix) for prefix in ("ia:", "isbn:", "ol:")):
            target_doi = first_arg
            target_title = sys.argv[2] if len(sys.argv) > 2 else None
        else:
            target_title = first_arg

        if not target_doi and target_title:
            print(f"Beginning Processing Pipeline for Target Document (Title: '{target_title}')...")
            # Attempt to resolve the title to a DOI via Crossref
            target_doi = resolve_title_to_doi(target_title)
        else:
            print(f"Beginning Processing Pipeline for Target Document (DOI: {target_doi})...")

        try:
            success = run_download_pipeline(target_doi, target_title)
            if success:
                print("\n==============================================")
                print("[PROCESS FINISHED] Document pulled successfully.")
                print("==============================================")
            else:
                # CLI mode failed to download programmatically. Report failure cleanly without browser popups.
                valid_fallbacks = sorted(state.discovered_urls, key=lambda x: x[1])
                print("\n==============================================")
                print("[PROCESS FAILED] Programmatic binary download failed.")
                if valid_fallbacks:
                    print("[INFO] Discovered URLs (copy-paste to access manually):")
                    for fu, rank, label in valid_fallbacks:
                        print(f"  -> [{label}] {fu}")
                print("==============================================")
        except InterruptedError:
            print("\n==============================================")
            print("[PROCESS CANCELLED] Stopped by user request.")
            print("==============================================")
        except Exception as e:
            print(f"\n[ERROR] Pipeline execution failed: {e}")
    else:
        # Launch beautiful GUI
        from src.gui.main_window import launch_gui
        launch_gui()

if __name__ == "__main__":
    main()
