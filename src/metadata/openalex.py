import urllib.request
import urllib.parse
import json
from src.core import state
from src.core.config import HEADERS, UNPAYWALL_EMAIL
from src.metadata.crossref import search_crossref
from src.core.journals import resolve_journal_url, get_journal_details, get_journal_details_by_title

def search_openalex_by_author(author_name, offset=0, rows=5, type_filter="All"):
    """Search OpenAlex for works by author name.
    
    OpenAlex first resolves the name to an author entity, then fetches their
    full publication list — giving accurate results for authors not well-indexed
    by Crossref (e.g. French/Algerian researchers, non-English publications).
    Falls back to Crossref query.author if OpenAlex finds nothing.
    """
    if not author_name:
        return []
    clean_name = author_name.strip().strip('"').strip("'")
    
    import uuid
    # OpenAlex requires a polite mailto in the User-Agent for best rate limits.
    # Generate a fresh email on every single request to bypass global throttling.
    random_email = f"user_{uuid.uuid4().hex[:8]}@academicdownloader.com"
    oa_headers = {**HEADERS, 'User-Agent': f'PaperDownloader/2.1 (mailto:{random_email})'}
    
    # Step 1: Resolve author name → OpenAlex author ID
    author_id = None
    try:
        author_url = f"https://api.openalex.org/authors?search={urllib.parse.quote(clean_name)}&per_page=5"
        req = urllib.request.Request(author_url, headers=oa_headers)
        with urllib.request.urlopen(req, timeout=12) as resp:
            adata = json.loads(resp.read().decode())
        authors_found = adata.get('results', [])
        if authors_found:
            author_id = authors_found[0].get('id', '')  # e.g. https://openalex.org/A123456
            print(f"[INFO] OpenAlex author resolved: {authors_found[0].get('display_name')} → {author_id}")
    except Exception as e:
        print(f"[WARNING] OpenAlex author lookup failed: {e}")
    
    results = []
    
    # Step 2a: Fetch works by resolved author ID (most accurate)
    if author_id:
        filter_parts = [f"authorships.author.id:{author_id}"]
        if type_filter == "Papers":
            filter_parts.append("type:article|preprint|review")
        elif type_filter == "Books":
            filter_parts.append("type:book|book-chapter")
        filter_str = ",".join(filter_parts)
        
        works_url = (f"https://api.openalex.org/works"
                     f"?filter={urllib.parse.quote(filter_str)}"
                     f"&per_page=50&sort=publication_year:desc")
                         
        max_retries = 3
        for attempt in range(max_retries):
            try:
                req = urllib.request.Request(works_url, headers=oa_headers)
                with urllib.request.urlopen(req, timeout=12) as resp:
                    wdata = json.loads(resp.read().decode())
                works = wdata.get('results', [])
                
                for work in works:
                    title = work.get('title', '')
                    if not title:
                        continue
                    doi = work.get('doi', '') or ''
                    if doi.startswith('https://doi.org/'):
                        doi = doi[len('https://doi.org/'):]
                    authorships = work.get('authorships', [])
                    auth_names = [a.get('author', {}).get('display_name', '')
                                  for a in authorships if a.get('author', {}).get('display_name')]
                    if not auth_names:
                        continue
                    year = str(work.get('publication_year', 'n.d.'))
                    primary_loc = work.get('primary_location') or {}
                    source = primary_loc.get('source') or {}
                    journal = source.get('display_name', 'Unknown Journal')
                    is_oa = (work.get('open_access') or {}).get('is_oa', False)
                    
                    issn_list = []
                    if source.get('issn'):
                        if isinstance(source['issn'], list):
                            issn_list.extend(source['issn'])
                        else:
                            issn_list.append(source['issn'])
                    if source.get('issn_l'):
                        issn_list.append(source['issn_l'])
                    
                    journal_url = resolve_journal_url(issn_list, doi=doi)
                    
                    journal_details = None
                    for issn in issn_list:
                        jd = get_journal_details(issn)
                        if jd:
                            journal_details = jd
                            break
                    
                    if not journal_details:
                        journal_details = get_journal_details_by_title(journal)
    
                    results.append({
                        'title': title,
                        'doi': doi,
                        'authors': ', '.join(auth_names[:4]),
                        'year': year,
                        'journal': journal,
                        'is_oa': is_oa,
                        'source': 'openalex',
                        'journal_url': journal_url,
                        'journal_details': journal_details,
                        'issns': issn_list
                    })
                break # Success, exit retry loop
                
            except urllib.error.HTTPError as e:
                if e.code == 429 and attempt < max_retries - 1:
                    import time
                    wait_time = 2 ** attempt
                    print(f"[WARNING] OpenAlex rate limit hit (429). Retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    print(f"[WARNING] OpenAlex works fetch failed: {e}")
                    break
            except Exception as e:
                print(f"[WARNING] OpenAlex works fetch failed: {e}")
                break
    
    # Step 2b: Fallback — Crossref query.author if OpenAlex returned nothing
    if not results:
        print(f"[INFO] OpenAlex returned no results, falling back to Crossref author search...")
        results = search_crossref("", offset=0, rows=50, type_filter=type_filter, author=clean_name)
    
    if not results:
        return []
    
    page_items = results[offset: offset + rows]
    for idx, item in enumerate(page_items):
        item['original_index'] = idx
    return page_items


def search_openalex_keyword(query, offset=0, rows=5, type_filter="All"):
    """Search OpenAlex for works matching a keyword query."""
    if not query:
        return []
    
    page = (offset // rows) + 1
    import uuid
    # Generate a fresh email on every single request to bypass global throttling.
    random_email = f"user_{uuid.uuid4().hex[:8]}@academicdownloader.com"
    oa_headers = {**HEADERS, 'User-Agent': f'PaperDownloader/2.1 (mailto:{random_email})'}
    
    filter_parts = []
    if type_filter == "Papers":
        filter_parts.append("type:article|preprint|review")
    elif type_filter == "Books":
        filter_parts.append("type:book|book-chapter")
        
    filter_str = ""
    if filter_parts:
        filter_str = f"&filter={urllib.parse.quote(','.join(filter_parts))}"
        
    url = (f"https://api.openalex.org/works"
           f"?search={urllib.parse.quote(query)}"
           f"&page={page}&per_page={rows}"
           f"{filter_str}")
           
    results = []
    max_retries = 3
    
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url, headers=oa_headers)
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read().decode())
            
            works = data.get('results', [])
            for work in works:
                title = work.get('title', '')
                if not title:
                    continue
                doi = work.get('doi', '') or ''
                if doi.startswith('https://doi.org/'):
                    doi = doi[len('https://doi.org/'):]
                authorships = work.get('authorships', [])
                auth_names = [a.get('author', {}).get('display_name', '')
                              for a in authorships if a.get('author', {}).get('display_name')]
                year = str(work.get('publication_year', 'n.d.'))
                primary_loc = work.get('primary_location') or {}
                source = primary_loc.get('source') or {}
                journal = source.get('display_name', 'Unknown Journal')
                is_oa = (work.get('open_access') or {}).get('is_oa', False)
                
                issn_list = []
                if source.get('issn'):
                    if isinstance(source['issn'], list):
                        issn_list.extend(source['issn'])
                    else:
                        issn_list.append(source['issn'])
                if source.get('issn_l'):
                    issn_list.append(source['issn_l'])
                
                journal_url = resolve_journal_url(issn_list, doi=doi)
                
                journal_details = None
                for issn in issn_list:
                    jd = get_journal_details(issn)
                    if jd:
                        journal_details = jd
                        break
                
                if not journal_details:
                    journal_details = get_journal_details_by_title(journal)
    
                results.append({
                    'title': title,
                    'doi': doi,
                    'authors': ', '.join(auth_names[:4]),
                    'year': year,
                    'journal': journal,
                    'is_oa': is_oa,
                    'source': 'openalex',
                    'journal_url': journal_url,
                    'journal_details': journal_details,
                    'issns': issn_list
                })
            break # Success, exit retry loop
            
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < max_retries - 1:
                import time
                wait_time = 2 ** attempt
                print(f"[WARNING] OpenAlex rate limit hit (429). Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                print(f"[WARNING] OpenAlex keyword search failed: {e}")
                break
        except Exception as e:
            print(f"[WARNING] OpenAlex keyword search failed: {e}")
            break
            
    return results

