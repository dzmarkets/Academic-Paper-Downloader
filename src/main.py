import sys
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

def run_download_pipeline(target_doi, target_title, status_label=None, root_widget=None):
    """Run through all download strategies sequentially until one succeeds."""
    def update_status(text, fg="#00ADB5"):
        if status_label:
            if root_widget:
                root_widget.after(0, lambda: status_label.config(text=text, fg=fg))
            else:
                status_label.config(text=text, fg=fg)

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

    success = False
    is_book_identifier = target_doi and any(target_doi.lower().startswith(prefix) for prefix in ("ia:", "isbn:", "ol:"))

    if is_book_identifier:
        update_status("Querying Book Repositories...")
        success = try_download_book(target_doi, target_title, status_label=status_label, root_widget=root_widget)
    else:
        if target_doi:
            # Try fast-path pattern matching (PLOS, BioRxiv) before requesting APIs
            if not success and target_doi.lower().startswith("10.1371/"):
                update_status("Querying PLOS Database...")
                success = try_plos(target_doi, target_title)
                
            if not success and target_doi.lower().startswith("10.1101/"):
                update_status("Querying BioRxiv/MedRxiv API...")
                success = try_biorxiv(target_doi, target_title)

            if not success:
                update_status("Querying Publisher Direct...")
                success = try_publisher_direct(target_doi, target_title, status_label=status_label)

            # Try direct URL download first if target_doi is a direct URL (and not a ResearchGate publication url)
            if not success and (target_doi.startswith("http://") or target_doi.startswith("https://")) and ("researchgate.net" not in target_doi or "/links/" in target_doi):
                update_status("Directly Downloading URL...")
                success = download_file(target_doi, clean_filename(target_title or "Downloaded_Paper") + ".pdf")
                if success:
                    print(f"[SUCCESS] Directly downloaded PDF from URL: {target_doi}")

            # Try Taylor & Francis first for known T&F DOI prefixes
            if not success and any(target_doi.startswith(p) for p in _TF_DOI_PREFIXES):
                update_status("Querying Taylor & Francis API...")
                success = try_download_taylorfrancis(target_doi, target_title)

            if not success:
                update_status("Querying Unpaywall Database...")
                success = try_unpaywall(target_doi)

            if state.abort_requested:
                raise InterruptedError("Cancelled by user")

            if not success:
                update_status("Querying Semantic Scholar...")
                success = try_semantic_scholar(target_doi, target_title)

            if state.abort_requested:
                raise InterruptedError("Cancelled by user")

            if not success:
                update_status("Querying Zenodo...")
                success = try_zenodo(target_doi, target_title)

            if state.abort_requested:
                raise InterruptedError("Cancelled by user")

            if not success:
                update_status("Querying DOAJ...")
                success = try_doaj(target_doi, target_title)

            if state.abort_requested:
                raise InterruptedError("Cancelled by user")

            if not success:
                update_status("Querying CORE...")
                success = try_core(target_doi, target_title)
            
            if state.abort_requested:
                raise InterruptedError("Cancelled by user")
                
            if not success:
                update_status("Querying SSRN...")
                success = try_ssrn(target_doi, target_title)

            if state.abort_requested:
                raise InterruptedError("Cancelled by user")

            if not success:
                update_status("Querying Sci-Hub Shadows...")
                success = try_scihub(target_doi)

            if state.abort_requested:
                raise InterruptedError("Cancelled by user")

            if not success:
                update_status("Querying Library Genesis...")
                success = try_libgen(target_doi, target_title)
            
        if state.abort_requested:
            raise InterruptedError("Cancelled by user")

        if not success:
            update_status("Querying arXiv...")
            success = try_arxiv(target_doi, target_title)
            
        if state.abort_requested:
            raise InterruptedError("Cancelled by user")

        if not success:
            update_status("Querying ASTESJ...")
            success = try_astesj(target_doi, target_title)

        if state.abort_requested:
            raise InterruptedError("Cancelled by user")

        if not success:
            update_status("Querying Europe PMC...")
            success = try_europe_pmc(target_doi, target_title)
            
        if state.abort_requested:
            raise InterruptedError("Cancelled by user")

        if not success:
            update_status("Querying ResearchGate...")
            success = try_researchgate(target_doi, target_title)
            
        if state.abort_requested:
            raise InterruptedError("Cancelled by user")

        # Final resort: check if it matches Gutenberg / OpenLibrary public domain books
        if not success:
            update_status("Querying Book Repositories...")
            success = try_download_book(target_doi, target_title, status_label=status_label, root_widget=root_widget)
            
        if state.abort_requested:
            raise InterruptedError("Cancelled by user")

    return success


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
