import re

with open('src/engines/researchgate.py', 'r') as f:
    content = f.read()


search_engines_logic = """
def _search_engines_for_profile(title, doi, target_year):
    \"\"\"Discover the paper link using search engine queries targeting ResearchGate.\"\"\"
    search_queries = []
    if title:
        cleaned_title = re.sub(r'\s+', ' ', title).strip().strip('"').strip("'")
        if cleaned_title:
            search_queries.append(f'"{cleaned_title}"')
            search_queries.append(cleaned_title)
    if doi and doi.strip() not in search_queries:
        search_queries.append(doi.strip())

    for search_query in search_queries:
        # ── Yahoo ──────────────────────────────────────────────────────────────
        print(f"[INFO] Searching ResearchGate for {repr(search_query)} via Yahoo...")
        try:
            yahoo_url = f"https://search.yahoo.com/search?p={urllib.parse.quote(search_query + ' site:researchgate.net/publication/')}"
            html = fetch_html_resilient(yahoo_url)
            if html:
                accepted_url, accepted_html = _try_validate(_collect_yahoo(html), "Yahoo", title, doi, target_year)
                if accepted_url:
                    print(f"[INFO] Yahoo resolved and validated ResearchGate publication: {accepted_url}")
                    return accepted_url, accepted_html
        except Exception as e:
            print(f"[WARNING] Yahoo ResearchGate publication search failed: {e}")

        # ── DuckDuckGo ────────────────────────────────────────────────────────
        print(f"[INFO] Searching ResearchGate for {repr(search_query)} via DuckDuckGo...")
        try:
            ddg_url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(search_query + ' site:researchgate.net/publication/')}"
            html = fetch_html_resilient(ddg_url)
            if html:
                accepted_url, accepted_html = _try_validate(_collect_ddg(html), "DuckDuckGo", title, doi, target_year)
                if accepted_url:
                    print(f"[INFO] DuckDuckGo resolved and validated ResearchGate publication: {accepted_url}")
                    return accepted_url, accepted_html
        except Exception as e:
            print(f"[WARNING] DuckDuckGo ResearchGate publication search failed: {e}")

        # ── Bing ──────────────────────────────────────────────────────────────
        print(f"[INFO] Searching ResearchGate for {repr(search_query)} via Bing...")
        try:
            bing_url = f"https://www.bing.com/search?q={urllib.parse.quote(search_query + ' site:researchgate.net/publication/')}&count=10"
            html = fetch_html_resilient(bing_url)
            if html:
                accepted_url, accepted_html = _try_validate(_collect_bing(html), "Bing", title, doi, target_year)
                if accepted_url:
                    print(f"[INFO] Bing resolved and validated ResearchGate publication: {accepted_url}")
                    return accepted_url, accepted_html
        except Exception as e:
            print(f"[WARNING] Bing ResearchGate publication search failed: {e}")

        # ── Google ────────────────────────────────────────────────────────────
        print(f"[INFO] Searching ResearchGate for {repr(search_query)} via Google (Best Effort)...")
        try:
            google_url = f"https://www.google.com/search?q={urllib.parse.quote(search_query + ' site:researchgate.net/publication/')}"
            html = fetch_html_resilient(google_url)
            if html:
                accepted_url, accepted_html = _try_validate(_collect_google(html), "Google", title, doi, target_year)
                if accepted_url:
                    print(f"[INFO] Google resolved and validated ResearchGate publication: {accepted_url}")
                    return accepted_url, accepted_html
        except Exception as e:
            print(f"[WARNING] Google ResearchGate publication search failed: {e}")

    return None, None
"""

content = content.replace("def try_researchgate(doi, title):", search_engines_logic + "\ndef try_researchgate(doi, title):")


original_search_logic = """    # Step 1: Discover the paper link using search engine queries targeting ResearchGate.
    # We try three query variants per engine to maximize coverage:
    #   1. Quoted exact title   (highest precision — avoids keyword-overlap false positives)
    #   2. Plain title          (broader fallback)
    #   3. DOI string           (most authoritative, but not always indexed by engines)
    if not rg_profile_url:
        search_queries = []
        if title:
            cleaned_title = re.sub(r'\s+', ' ', title).strip().strip('"').strip("'")
            if cleaned_title:
                search_queries.append(f'"{cleaned_title}"')
                search_queries.append(cleaned_title)
        if doi and doi.strip() not in search_queries:
            search_queries.append(doi.strip())

        for search_query in search_queries:
            if rg_profile_url:
                break

            # ── Yahoo ──────────────────────────────────────────────────────────────
            print(f"[INFO] Searching ResearchGate for {repr(search_query)} via Yahoo...")
            try:
                yahoo_url = f"https://search.yahoo.com/search?p={urllib.parse.quote(search_query + ' site:researchgate.net/publication/')}"
                html = fetch_html_resilient(yahoo_url)
                if html:
                    accepted_url, accepted_html = _try_validate(_collect_yahoo(html), "Yahoo", title, doi, target_year)
                    if accepted_url:
                        rg_profile_url = accepted_url
                        rg_page_source = accepted_html
                        print(f"[INFO] Yahoo resolved and validated ResearchGate publication: {rg_profile_url}")
            except Exception as e:
                print(f"[WARNING] Yahoo ResearchGate publication search failed: {e}")

            if rg_profile_url:
                break

            # ── DuckDuckGo ────────────────────────────────────────────────────────
            print(f"[INFO] Searching ResearchGate for {repr(search_query)} via DuckDuckGo...")
            try:
                ddg_url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(search_query + ' site:researchgate.net/publication/')}"
                html = fetch_html_resilient(ddg_url)
                if html:
                    accepted_url, accepted_html = _try_validate(_collect_ddg(html), "DuckDuckGo", title, doi, target_year)
                    if accepted_url:
                        rg_profile_url = accepted_url
                        rg_page_source = accepted_html
                        print(f"[INFO] DuckDuckGo resolved and validated ResearchGate publication: {rg_profile_url}")
            except Exception as e:
                print(f"[WARNING] DuckDuckGo ResearchGate publication search failed: {e}")

            if rg_profile_url:
                break

            # ── Bing ──────────────────────────────────────────────────────────────
            print(f"[INFO] Searching ResearchGate for {repr(search_query)} via Bing...")
            try:
                bing_url = f"https://www.bing.com/search?q={urllib.parse.quote(search_query + ' site:researchgate.net/publication/')}&count=10"
                html = fetch_html_resilient(bing_url)
                if html:
                    accepted_url, accepted_html = _try_validate(_collect_bing(html), "Bing", title, doi, target_year)
                    if accepted_url:
                        rg_profile_url = accepted_url
                        rg_page_source = accepted_html
                        print(f"[INFO] Bing resolved and validated ResearchGate publication: {rg_profile_url}")
            except Exception as e:
                print(f"[WARNING] Bing ResearchGate publication search failed: {e}")

            if rg_profile_url:
                break

            # ── Google ────────────────────────────────────────────────────────────
            print(f"[INFO] Searching ResearchGate for {repr(search_query)} via Google (Best Effort)...")
            try:
                google_url = f"https://www.google.com/search?q={urllib.parse.quote(search_query + ' site:researchgate.net/publication/')}"
                html = fetch_html_resilient(google_url)
                if html:
                    accepted_url, accepted_html = _try_validate(_collect_google(html), "Google", title, doi, target_year)
                    if accepted_url:
                        rg_profile_url = accepted_url
                        rg_page_source = accepted_html
                        print(f"[INFO] Google resolved and validated ResearchGate publication: {rg_profile_url}")
            except Exception as e:
                print(f"[WARNING] Google ResearchGate publication search failed: {e}")"""

replacement = """    # Step 1: Discover the paper link using search engine queries targeting ResearchGate.
    if not rg_profile_url:
        rg_profile_url, rg_page_source = _search_engines_for_profile(title, doi, target_year)"""

content = content.replace(original_search_logic, replacement)

with open('src/engines/researchgate.py', 'w') as f:
    f.write(content)
