import re

with open('src/engines/researchgate.py', 'r') as f:
    content = f.read()

# Extract inner functions and move them outside
collect_yahoo_code = """
def _collect_yahoo(html_body):
    \"\"\"Extract ResearchGate publication URLs from Yahoo HTML.\"\"\"
    results = []
    seen = set()
    ru_links = re.findall(r'RU=([^/&"]+)', html_body)
    for val in ru_links:
        unquoted = urllib.parse.unquote(val)
        if "researchgate.net/publication/" not in unquoted:
            continue
        pub_url = unquoted.split('/RK=')[0]
        m = re.match(r'(https?://(?:www\.)?researchgate\.net/publication/\d+_[^/&?"]+)', pub_url)
        if not m:
            m = re.match(r'(https?://(?:www\.)?researchgate\.net/publication/\d+[^/&?"]*)', pub_url)
        if m and m.group(1) not in seen:
            seen.add(m.group(1))
            results.append(m.group(1))
    return results

def _collect_ddg(html_body):
    \"\"\"Extract ResearchGate publication URLs from DuckDuckGo HTML.\"\"\"
    results = []
    seen = set()
    encoded_links = re.findall(r'uddg=(https?%3A%2F%2F[^&"]*researchgate\.net%2Fpublication%2F[^&"]*)', html_body)
    for enc_link in encoded_links:
        resolved = urllib.parse.unquote(enc_link).split("&")[0]
        if resolved not in seen:
            seen.add(resolved)
            results.append(resolved)
    direct_links = re.findall(r'href="([^"]*researchgate\.net/publication/[^"]*)"', html_body)
    for link in direct_links:
        resolved = urllib.parse.unquote(link).split("&")[0]
        if resolved not in seen:
            seen.add(resolved)
            results.append(resolved)
    return results

def _collect_bing(html_body):
    \"\"\"Extract ResearchGate publication URLs from Bing HTML.\"\"\"
    results = []
    seen = set()
    links = re.findall(r'href="(https?://(?:www\.)?researchgate\.net/publication/[^"&]+)"', html_body)
    for link in links:
        if link not in seen:
            seen.add(link)
            results.append(link)
    return results

def _collect_google(html_body):
    \"\"\"Extract ResearchGate publication URLs from Google HTML.\"\"\"
    results = []
    seen = set()
    links = re.findall(r'url\?q=(https://(?:www\.)?researchgate\.net/publication/[^&"()]+)', html_body)
    for link in links:
        unquoted = urllib.parse.unquote(link)
        m = re.match(r'(https?://(?:www\.)?researchgate\.net/publication/\d+_[^/&?"]+)', unquoted)
        if not m:
            m = re.match(r'(https?://(?:www\.)?researchgate\.net/publication/\d+[^/&?"]*)', unquoted)
        if m and m.group(1) not in seen:
            seen.add(m.group(1))
            results.append(m.group(1))
    return results

def _try_validate(candidates, engine_name, title, doi, target_year):
    \"\"\"Run title-similarity pre-check + page validation on a list of candidates.
    Returns (accepted_url, accepted_html) on first match, or (None, None).\"\"\"
    for url in candidates:
        if not check_title_similarity(title, url):
            continue
        print(f"[INFO] {engine_name}: candidate passed URL similarity check: {url}. Fetching to validate...")
        page_src = fetch_html_resilient(url)
        if validate_researchgate_page(page_src, title, doi, target_year):
            return url, page_src
    return None, None
"""

# Now write them right before try_researchgate
content = content.replace("def try_researchgate(doi, title):", collect_yahoo_code + "\ndef try_researchgate(doi, title):")

# Now remove them from inside try_researchgate
inner_funcs = """        def _collect_yahoo(html_body):
            \"\"\"Extract ResearchGate publication URLs from Yahoo HTML.\"\"\"
            results = []
            seen = set()
            ru_links = re.findall(r'RU=([^/&"]+)', html_body)
            for val in ru_links:
                unquoted = urllib.parse.unquote(val)
                if "researchgate.net/publication/" not in unquoted:
                    continue
                pub_url = unquoted.split('/RK=')[0]
                m = re.match(r'(https?://(?:www\.)?researchgate\.net/publication/\d+_[^/&?"]+)', pub_url)
                if not m:
                    m = re.match(r'(https?://(?:www\.)?researchgate\.net/publication/\d+[^/&?"]*)', pub_url)
                if m and m.group(1) not in seen:
                    seen.add(m.group(1))
                    results.append(m.group(1))
            return results

        def _collect_ddg(html_body):
            \"\"\"Extract ResearchGate publication URLs from DuckDuckGo HTML.\"\"\"
            results = []
            seen = set()
            encoded_links = re.findall(r'uddg=(https?%3A%2F%2F[^&"]*researchgate\.net%2Fpublication%2F[^&"]*)', html_body)
            for enc_link in encoded_links:
                resolved = urllib.parse.unquote(enc_link).split("&")[0]
                if resolved not in seen:
                    seen.add(resolved)
                    results.append(resolved)
            direct_links = re.findall(r'href="([^"]*researchgate\.net/publication/[^"]*)"', html_body)
            for link in direct_links:
                resolved = urllib.parse.unquote(link).split("&")[0]
                if resolved not in seen:
                    seen.add(resolved)
                    results.append(resolved)
            return results

        def _collect_bing(html_body):
            \"\"\"Extract ResearchGate publication URLs from Bing HTML.\"\"\"
            results = []
            seen = set()
            links = re.findall(r'href="(https?://(?:www\.)?researchgate\.net/publication/[^"&]+)"', html_body)
            for link in links:
                if link not in seen:
                    seen.add(link)
                    results.append(link)
            return results

        def _collect_google(html_body):
            \"\"\"Extract ResearchGate publication URLs from Google HTML.\"\"\"
            results = []
            seen = set()
            links = re.findall(r'url\?q=(https://(?:www\.)?researchgate\.net/publication/[^&"()]+)', html_body)
            for link in links:
                unquoted = urllib.parse.unquote(link)
                m = re.match(r'(https?://(?:www\.)?researchgate\.net/publication/\d+_[^/&?"]+)', unquoted)
                if not m:
                    m = re.match(r'(https?://(?:www\.)?researchgate\.net/publication/\d+[^/&?"]*)', unquoted)
                if m and m.group(1) not in seen:
                    seen.add(m.group(1))
                    results.append(m.group(1))
            return results

        def _try_validate(candidates, engine_name):
            \"\"\"Run title-similarity pre-check + page validation on a list of candidates.
            Returns (accepted_url, accepted_html) on first match, or (None, None).\"\"\"
            for url in candidates:
                if not check_title_similarity(title, url):
                    continue
                print(f"[INFO] {engine_name}: candidate passed URL similarity check: {url}. Fetching to validate...")
                page_src = fetch_html_resilient(url)
                if validate_researchgate_page(page_src, title, doi, target_year):
                    return url, page_src
            return None, None
"""
content = content.replace(inner_funcs, "")

content = content.replace('_try_validate(_collect_yahoo(html), "Yahoo")', '_try_validate(_collect_yahoo(html), "Yahoo", title, doi, target_year)')
content = content.replace('_try_validate(_collect_ddg(html), "DuckDuckGo")', '_try_validate(_collect_ddg(html), "DuckDuckGo", title, doi, target_year)')
content = content.replace('_try_validate(_collect_bing(html), "Bing")', '_try_validate(_collect_bing(html), "Bing", title, doi, target_year)')
content = content.replace('_try_validate(_collect_google(html), "Google")', '_try_validate(_collect_google(html), "Google", title, doi, target_year)')


with open('src/engines/researchgate.py', 'w') as f:
    f.write(content)
