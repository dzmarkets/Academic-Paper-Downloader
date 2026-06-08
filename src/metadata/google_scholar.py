import re
import urllib.parse
from src.core import state
from src.network.client import fetch_html_resilient

def search_google_scholar(query, offset=0, rows=5):
    """Query Google Scholar index via a robust, CAPTCHA-free DuckDuckGo fallback scraper.
    
    This retrieves high-quality academic titles, PDF links, authors, and journal names.
    """
    if state.abort_requested:
        return []
    if not query:
        return []
    
    # Check exact phrase match in quotes (Google-like intelligent search)
    stripped = query.strip()
    is_exact = (stripped.startswith('"') and stripped.endswith('"')) or (stripped.startswith("'") and stripped.endswith("'"))
    exact_phrase = stripped.strip('"').strip("'").strip() if is_exact else None
    
    clean_query = stripped
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(clean_query)}"
    print(f"[INFO] Querying Google Scholar (via DuckDuckGo proxy): {url}")
    
    try:
        html = fetch_html_resilient(url)
        if not html:
            return []
            
        blocks = re.split(r'<div class="[^"]*result__body[^"]*">', html)
        results = []
        
        for block in blocks[1:]:
            # Extract link and title
            a_match = re.search(r'<a[^>]*class="[^"]*result__a[^"]*"[^>]*>(.*?)</a>', block, re.DOTALL)
            if not a_match:
                continue
                
            title = re.sub('<[^<]+?>', '', a_match.group(1)).strip()
            
            href_match = re.search(r'href="([^"]+)"', a_match.group(0))
            if not href_match:
                continue
                
            raw_url = href_match.group(1)
            url_match = re.search(r'uddg=(https?%3A%2F%2F[^&"]*)', raw_url)
            actual_url = urllib.parse.unquote(url_match.group(1)) if url_match else raw_url
            if actual_url.startswith('//'):
                actual_url = 'https:' + actual_url
                
            # Skip profile pages, university directories, members lists, department lists, and search catalog result pages
            url_lower = actual_url.lower()
            title_lower = title.lower()
            
            is_profile = (
                "/profile/" in url_lower or
                "/institution/" in url_lower or
                "/members" in url_lower or
                "members" in title_lower or
                "dpartement" in title_lower or
                "département" in title_lower or
                "department" in title_lower or
                "faculty" in url_lower or
                "faculty" in title_lower or
                "central library" in title_lower or
                "catalogue en ligne" in title_lower or
                "index.php?lvl=more_results" in url_lower or
                ("search" in url_lower and "catalog" in url_lower) or
                "univ-" in url_lower or
                ("university" in title_lower and ("members" in title_lower or "profile" in title_lower))
            )
            if is_profile:
                continue
                
            # Skip non-academic / software / documentation / social domains —
            # only papers from academic repositories should appear in search results
            _NON_ACADEMIC_DOMAINS = (
                "github.com",
                "github.io",
                "readthedocs.io",
                "readthedocs.org",
                "pypi.org",
                "stackoverflow.com",
                "stackexchange.com",
                "reddit.com",
                "twitter.com",
                "x.com",
                "linkedin.com",
                "facebook.com",
                "youtube.com",
                "medium.com",
                "substack.com",
                "wikipedia.org",
                "conda-forge.org",
                "anaconda.org",
                "bioconductor.org",
                "npmjs.com",
                "cran.r-project.org",
                "sourceforge.net",
                "gitlab.com",
                "bitbucket.org",
                "docs.python.org",
                "docs.scipy.org",
                "galaxyproject.org",
                "snakemake.readthedocs.io",
            )
            if any(nd in url_lower for nd in _NON_ACADEMIC_DOMAINS):
                print(f"[INFO] Skipping non-academic URL: {actual_url}")
                continue
                
            # Snippet
            snippet_match = re.search(r'<a[^>]*class="[^"]*result__snippet[^"]*"[^>]*>(.*?)</a>', block, re.DOTALL)
            snippet = re.sub('<[^<]+?>', '', snippet_match.group(1)).strip() if snippet_match else ""
            
            # Exact phrase check (Google-like intelligent search)
            if exact_phrase:
                phrase = exact_phrase.lower()
                if (phrase not in title.lower()) and (phrase not in snippet.lower()):
                    continue
            
            authors = "Unknown Authors"
            journal = "Web Resource"
            year = "n.d."
            
            is_pdf = actual_url.lower().split('?')[0].endswith('.pdf') or 'pdf' in actual_url.lower()
            
            if "researchgate.net" in actual_url:
                journal = "ResearchGate Profile"
                if " | " in title:
                    authors = title.split(" | ")[0]
                elif " -" in title:
                    authors = title.split(" -")[0]
            elif "scholar.google.com" in actual_url:
                journal = "Google Scholar Citations"
            else:
                parsed = urllib.parse.urlparse(actual_url)
                journal = parsed.netloc.replace("www.", "")
                
            year_match = re.search(r'\b(19\d{2}|20\d{2})\b', snippet + " " + title)
            if year_match:
                year = year_match.group(1)
                
            if "Abstract" in snippet:
                before_abstract = snippet.split("Abstract")[0].strip()
                before_abstract = re.sub(r'[\.\-\s,]+$', '', before_abstract)
                if len(before_abstract) > 3 and len(before_abstract) < 150:
                    authors = before_abstract
            elif "Authors:" in snippet:
                authors_part = snippet.split("Authors:")[1].strip()
                authors_part = re.split(r'\b(download|published|abstract|index)\b', authors_part, flags=re.IGNORECASE)[0].strip()
                authors_part = re.sub(r'[\.\-\s,]+$', '', authors_part)
                if len(authors_part) > 3 and len(authors_part) < 150:
                    authors = authors_part
            
            if authors == "Unknown Authors" and exact_phrase:
                authors = exact_phrase
            
            # Skip results that still have unknown authors after all extraction
            if authors == "Unknown Authors":
                continue
                
            results.append({
                'title': title,
                'doi': actual_url,  # Direct download will resolve URL
                'authors': authors,
                'year': year,
                'journal': journal,
                'is_oa': is_pdf
            })
            
        return results[offset : offset + rows]
    except Exception as e:
        print(f"[WARNING] Google Scholar search failed: {e}")
        return []
