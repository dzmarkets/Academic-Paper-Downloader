import re

with open('src/engines/researchgate.py', 'r') as f:
    content = f.read()

# Let's clean up the whole try_researchgate function now that we have helpers

main_func = """def try_researchgate(doi, title):
    \"\"\"Strategy 3: Automated extraction from ResearchGate.\"\"\"
    if not doi and not title:
        print("\\n--- [STRATEGY 3] Skipped (No DOI or Title available) ---")
        return False
    print("\\n--- [STRATEGY 3] Scraping ResearchGate for Full-Text ---")

    target_year = None
    metadata = None
    # Resolve DOI metadata if missing or for validation parameters
    if doi:
        metadata = resolve_doi_metadata(doi)
        if metadata:
            if not title:
                title = metadata.get('title')
                if title:
                    print(f"[INFO] Resolved DOI to exact title: '{title}'")
            target_year = metadata.get('year')

    rg_profile_url, rg_page_source = _resolve_direct_doi(doi, title, target_year)

    if not rg_profile_url and metadata:
        rg_profile_url, rg_page_source = _resolve_by_author(doi, title, metadata, target_year)

    # Step 1: Discover the paper link using search engine queries targeting ResearchGate.
    if not rg_profile_url:
        rg_profile_url, rg_page_source = _search_engines_for_profile(title, doi, target_year)

    if rg_profile_url:
        register_discovered_url(rg_profile_url, "ResearchGate Profile Page")

    if not rg_profile_url:
        print("[INFO] Could not map paper details to a definitive ResearchGate profile.")
        return False

    # Step 2: Scrape the actual profile page for open full-text assets
    return _scrape_and_download_profile(rg_profile_url, rg_page_source, title, doi)
"""

# I need to replace everything from "def try_researchgate(doi, title):" to the end of the file
# with our new try_researchgate function
idx = content.find("def try_researchgate(doi, title):")
if idx != -1:
    new_content = content[:idx] + main_func

    with open('src/engines/researchgate.py', 'w') as f:
        f.write(new_content)
else:
    print("Could not find try_researchgate definition!")
