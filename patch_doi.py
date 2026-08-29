import re

with open('src/engines/researchgate.py', 'r') as f:
    content = f.read()

# Extract DOI and author logic
doi_logic = """
def _resolve_direct_doi(doi, title, target_year):
    \"\"\"Attempt to resolve DOI to a ResearchGate profile via direct links or DOI resolvers.\"\"\"
    if not doi:
        return None, None

    rg_profile_url = None
    rg_page_source = None

    # 0. Check if DOI is already a direct ResearchGate publication URL
    if "researchgate.net/publication/" in doi:
        rg_profile_url = doi
        print(f"[INFO] Using provided direct ResearchGate publication URL: {rg_profile_url}")

    # 1. If it is a ResearchGate specific DOI, attempt direct internal resolver link
    elif doi.strip().startswith("10.13140/"):
        resolver_url = f"https://www.researchgate.net/doi/{doi.strip()}"
        print(f"[INFO] Detected ResearchGate DOI. Attempting direct internal resolver: {resolver_url}")
        try:
            req = urllib.request.Request(resolver_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as response:
                final_url = response.geturl()
                if "researchgate.net/publication/" in final_url:
                    print(f"[INFO] Direct internal resolver redirected to candidate: {final_url}. Fetching page to validate...")
                    page_source = fetch_html_resilient(final_url)
                    if validate_researchgate_page(page_source, title, doi, target_year):
                        rg_profile_url = final_url
                        rg_page_source = page_source
                        print(f"[INFO] Direct internal resolver succeeded and validated: {rg_profile_url}")
        except Exception as e:
            print(f"[WARNING] Direct internal resolver bypassed/failed (usually due to 403 Forbidden): {e}")

    # 2. Direct resolution using Crossref / Handle API as fallback
    if not rg_profile_url:
        resolved_url = resolve_doi_to_url(doi)
        if resolved_url:
            print(f"[INFO] Resolving resolved DOI URL: {resolved_url}")
            try:
                req = urllib.request.Request(resolved_url, headers=HEADERS)
                with urllib.request.urlopen(req, timeout=10) as response:
                    final_url = response.geturl()
                    if "researchgate.net/publication/" in final_url:
                        print(f"[INFO] Direct DOI resolution redirected to candidate: {final_url}. Fetching page to validate...")
                        page_source = fetch_html_resilient(final_url)
                        if validate_researchgate_page(page_source, title, doi, target_year):
                            rg_profile_url = final_url
                            rg_page_source = page_source
                            print(f"[INFO] Direct DOI resolution succeeded and validated: {rg_profile_url}")
            except Exception as e:
                print(f"[WARNING] Direct DOI URL resolution bypassed/failed: {e}")

    # 3. Direct resolution via doi.org redirect as a fallback
    if not rg_profile_url:
        print(f"[INFO] Attempting direct DOI resolution via doi.org...")
        try:
            url = f"https://doi.org/{doi}"
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as response:
                final_url = response.geturl()
                if "researchgate.net/publication/" in final_url:
                    print(f"[INFO] doi.org resolution redirected to candidate: {final_url}. Fetching page to validate...")
                    page_source = fetch_html_resilient(final_url)
                    if validate_researchgate_page(page_source, title, doi, target_year):
                        rg_profile_url = final_url
                        rg_page_source = page_source
                        print(f"[INFO] Direct DOI resolution succeeded and validated: {rg_profile_url}")
        except Exception as e:
            print(f"[WARNING] Direct DOI resolution bypassed/failed: {e}")

    return rg_profile_url, rg_page_source

def _resolve_by_author(doi, title, metadata, target_year):
    \"\"\"Attempt author-profile-based resolution on ResearchGate as a highly reliable fallback.\"\"\"
    if not doi or not metadata or not metadata.get('authors'):
        return None, None

    print("[INFO] Attempting author-profile-based resolution on ResearchGate...")
    for author in metadata['authors'][:3]:
        try:
            # search_researchgate_by_author queries Yahoo/DDG for profile, then scrapes it
            pub_entries = search_researchgate_by_author(author)
            for entry in pub_entries:
                entry_url = entry.get('doi')  # search_researchgate_by_author stores publication URL in 'doi'
                if entry_url:
                    # Verify if this is the correct publication using title segment checking
                    if check_title_similarity(title if title else metadata.get('title'), entry_url):
                        print(f"[INFO] Author profile search found candidate: {entry_url}. Fetching page to validate...")
                        page_source = fetch_html_resilient(entry_url)
                        if validate_researchgate_page(page_source, title if title else metadata.get('title'), doi, target_year):
                            rg_profile_url = entry_url
                            rg_page_source = page_source
                            print(f"[INFO] Author profile search resolved and validated ResearchGate publication: {rg_profile_url}")
                            return rg_profile_url, rg_page_source
        except Exception as e:
            print(f"[WARNING] Author-profile-based search failed for '{author}': {e}")

    return None, None
"""

content = content.replace("def try_researchgate(doi, title):", doi_logic + "\ndef try_researchgate(doi, title):")

original_doi_logic = """    # 0. Check if DOI is already a direct ResearchGate publication URL
    if doi and "researchgate.net/publication/" in doi:
        rg_profile_url = doi
        print(f"[INFO] Using provided direct ResearchGate publication URL: {rg_profile_url}")

    # 1. If it is a ResearchGate specific DOI, attempt direct internal resolver link
    elif doi and doi.strip().startswith("10.13140/"):
        resolver_url = f"https://www.researchgate.net/doi/{doi.strip()}"
        print(f"[INFO] Detected ResearchGate DOI. Attempting direct internal resolver: {resolver_url}")
        try:
            req = urllib.request.Request(resolver_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as response:
                final_url = response.geturl()
                if "researchgate.net/publication/" in final_url:
                    print(f"[INFO] Direct internal resolver redirected to candidate: {final_url}. Fetching page to validate...")
                    page_source = fetch_html_resilient(final_url)
                    if validate_researchgate_page(page_source, title, doi, target_year):
                        rg_profile_url = final_url
                        rg_page_source = page_source
                        print(f"[INFO] Direct internal resolver succeeded and validated: {rg_profile_url}")
        except Exception as e:
            print(f"[WARNING] Direct internal resolver bypassed/failed (usually due to 403 Forbidden): {e}")

    # 2. Direct resolution using Crossref / Handle API as fallback
    if doi and not rg_profile_url:
        resolved_url = resolve_doi_to_url(doi)
        if resolved_url:
            print(f"[INFO] Resolving resolved DOI URL: {resolved_url}")
            try:
                req = urllib.request.Request(resolved_url, headers=HEADERS)
                with urllib.request.urlopen(req, timeout=10) as response:
                    final_url = response.geturl()
                    if "researchgate.net/publication/" in final_url:
                        print(f"[INFO] Direct DOI resolution redirected to candidate: {final_url}. Fetching page to validate...")
                        page_source = fetch_html_resilient(final_url)
                        if validate_researchgate_page(page_source, title, doi, target_year):
                            rg_profile_url = final_url
                            rg_page_source = page_source
                            print(f"[INFO] Direct DOI resolution succeeded and validated: {rg_profile_url}")
            except Exception as e:
                print(f"[WARNING] Direct DOI URL resolution bypassed/failed: {e}")

    # 3. Direct resolution via doi.org redirect as a fallback
    if doi and not rg_profile_url:
        print(f"[INFO] Attempting direct DOI resolution via doi.org...")
        try:
            url = f"https://doi.org/{doi}"
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as response:
                final_url = response.geturl()
                if "researchgate.net/publication/" in final_url:
                    print(f"[INFO] doi.org resolution redirected to candidate: {final_url}. Fetching page to validate...")
                    page_source = fetch_html_resilient(final_url)
                    if validate_researchgate_page(page_source, title, doi, target_year):
                        rg_profile_url = final_url
                        rg_page_source = page_source
                        print(f"[INFO] Direct DOI resolution succeeded and validated: {rg_profile_url}")
        except Exception as e:
            print(f"[WARNING] Direct DOI resolution bypassed/failed: {e}")

    # 4. Attempt author-profile-based resolution on ResearchGate as a highly reliable fallback
    if doi and not rg_profile_url and 'metadata' in locals() and metadata and metadata.get('authors'):
        print("[INFO] Attempting author-profile-based resolution on ResearchGate...")
        for author in metadata['authors'][:3]:
            if rg_profile_url:
                break
            try:
                # search_researchgate_by_author queries Yahoo/DDG for profile, then scrapes it
                pub_entries = search_researchgate_by_author(author)
                for entry in pub_entries:
                    entry_url = entry.get('doi')  # search_researchgate_by_author stores publication URL in 'doi'
                    if entry_url:
                        # Verify if this is the correct publication using title segment checking
                        if check_title_similarity(title if title else metadata.get('title'), entry_url):
                            print(f"[INFO] Author profile search found candidate: {entry_url}. Fetching page to validate...")
                            page_source = fetch_html_resilient(entry_url)
                            if validate_researchgate_page(page_source, title if title else metadata.get('title'), doi, target_year):
                                rg_profile_url = entry_url
                                rg_page_source = page_source
                                print(f"[INFO] Author profile search resolved and validated ResearchGate publication: {rg_profile_url}")
                                break
            except Exception as e:
                print(f"[WARNING] Author-profile-based search failed for '{author}': {e}")"""

replacement = """    rg_profile_url, rg_page_source = _resolve_direct_doi(doi, title, target_year)

    if not rg_profile_url and 'metadata' in locals() and metadata:
        rg_profile_url, rg_page_source = _resolve_by_author(doi, title, metadata, target_year)"""

content = content.replace(original_doi_logic, replacement)

import urllib.request # Ensure it compiles after change
with open('src/engines/researchgate.py', 'w') as f:
    f.write(content)
