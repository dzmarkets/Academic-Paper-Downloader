import urllib.request
import urllib.parse
import json
import concurrent.futures
from src.core import state
from src.core.config import HEADERS, UNPAYWALL_EMAIL
from src.core.journals import resolve_journal_url, get_journal_details, get_journal_details_by_title

def resolve_title_to_doi(title):
    """Query Crossref API to resolve a title to a DOI."""
    if not title:
        return None
    print(f"\n--- [RESOLVING] Searching Crossref for DOI of '{title}' ---")
    url = f"https://api.crossref.org/works?query={urllib.parse.quote(title)}&rows=1"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            
        items = data.get('message', {}).get('items', [])
        if items:
            best_match = items[0]
            resolved_doi = best_match.get('DOI')
            resolved_title = best_match.get('title', [title])[0]
            print(f"[INFO] Closest match on Crossref: '{resolved_title}'")
            print(f"[INFO] Resolved DOI: {resolved_doi}")
            return resolved_doi
    except Exception as e:
        print(f"[WARNING] Crossref resolution failed: {e}")
    return None


from src.core.utils import calculate_title_similarity, parse_search_query

def search_crossref(query, offset=0, rows=5, type_filter="All", author="", year=None):
    """Query Crossref API for title+author+year keywords, return paginated list with OA check."""
    if state.abort_requested:
        return []
    if not query:
        return []
        
    # Auto-parse title, author, year if full structured query is passed
    parsed = parse_search_query(query)
    clean_query = parsed['title'] if parsed['title'] else query.strip()
    clean_author = (author or parsed['author']).strip().strip('"').strip("'")
    target_year = str(year or parsed['year']).strip() if (year or parsed['year']) else None
    
    # Detect exact match phrase in quotes
    stripped = query.strip()
    is_exact = (stripped.startswith('"') and stripped.endswith('"')) or (stripped.startswith("'") and stripped.endswith("'")) or bool(parsed['title'])
    exact_phrase = parsed['title'] if parsed['title'] else (stripped.strip('"').strip("'").strip() if is_exact else None)
    
    print(f"[STEP 2/3] EXACT PHRASE SEARCH (Crossref API)")
    print(f"  - Target Title : '{clean_query}'")
    if clean_author:
        print(f"  - Target Author: '{clean_author}'")
    if target_year:
        print(f"  - Target Year  : {target_year}")
        
    crossref_rows = 40 + offset
    
    # Helper to execute Crossref API call
    def execute_query(query_param_str):
        filters = []
        if type_filter == "Papers":
            filters.append("type:journal-article,type:proceedings-article,type:posted-content")
        elif type_filter == "Books":
            filters.append("type:book")
        if target_year and target_year.isdigit() and len(target_year) == 4:
            y = int(target_year)
            filters.append(f"from-pub-date:{y-1}-01-01,until-pub-date:{y+1}-12-31")
        filter_str = f"&filter={','.join(filters)}" if filters else ""
        req_url = f"https://api.crossref.org/works?{query_param_str}{filter_str}&rows={crossref_rows}&offset=0"
        try:
            req = urllib.request.Request(req_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=8) as response:
                return json.loads(response.read().decode()).get('message', {}).get('items', [])
        except Exception as e:
            print(f"[WARNING] Crossref stage failed ({req_url}): {e}")
            return []

    # Stage 1: Try exact title search first
    print(f"[STEP 2/3] PRIORITY 1: EXACT TITLE PHRASE SEARCH")
    print(f"  - Target Title : '{clean_query}'")
    if target_year:
        print(f"  - Target Year  : {target_year}")
        
    items = execute_query(f"query.title={urllib.parse.quote(clean_query)}")
    
    # Stage 2: Fallback to general keyword query if Stage 1 yields 0 items
    if not items:
        print(f"[STEP 3/3] PRIORITY 2: KEYWORD SEARCH FALLBACK")
        print(f"  - Query Keywords: '{clean_query}'")
        items = execute_query(f"query={urllib.parse.quote(clean_query)}")



    try:
        if state.abort_requested:
            return []
            
        filtered_items = []

        for item in items:
            # If type_filter is Papers, only keep journal-article, proceedings-article, and posted-content (preprints)
            if type_filter == "Papers":
                allowed = ("journal-article", "proceedings-article", "posted-content")
                if item.get('type') not in allowed:
                    continue

            doi = item.get('DOI', '')
            if not doi:
                continue
                
            # Check authors - strictly exclude if empty or missing
            authors_list = item.get('author', [])
            if not authors_list:
                continue
                
            authors = []
            for a in authors_list:
                family = a.get('family', '')
                given = a.get('given', '')
                if family:
                    authors.append(f"{given} {family}".strip())
            if not authors:
                continue
            authors_str = ", ".join(authors)
            
            title = item.get('title', ['No Title'])[0]
            
            # Exact phrase check (Google-like intelligent search)
            if exact_phrase:
                phrase = exact_phrase.lower()
                if (phrase not in title.lower()) and (phrase not in authors_str.lower()):
                    continue
            
            # Journal/publisher name
            journal = "Unknown Publisher"
            container_title = item.get('container-title')
            publisher = item.get('publisher', '')
            if container_title and len(container_title) > 0 and container_title[0]:
                journal = container_title[0]
            elif publisher:
                journal = publisher
                
            # Format year
            year = "n.d."
            published = item.get('published-print') or item.get('published-online') or item.get('created')
            if published:
                date_parts = published.get('date-parts', [[]])[0]
                if date_parts:
                    year = str(date_parts[0])
                    
            issn_list = item.get('ISSN', [])
            journal_url = resolve_journal_url(issn_list, doi=doi)
            
            journal_details = None
            for issn in issn_list:
                jd = get_journal_details(issn)
                if jd:
                    journal_details = jd
                    break
            
            if not journal_details:
                journal_details = get_journal_details_by_title(journal)

            sim_score = calculate_title_similarity(clean_query, title) if clean_query else 1.0

            filtered_items.append({
                'title': title,
                'doi': doi,
                'authors': authors_str,
                'year': year,
                'journal': journal,
                'is_oa': False,
                'journal_url': journal_url,
                'journal_details': journal_details,
                'issns': issn_list,
                'similarity': sim_score
            })
            
        # Sort items by similarity score descending if a query title was given
        if clean_query:
            filtered_items.sort(key=lambda x: x.get('similarity', 0.0), reverse=True)
            
        # Page the filtered items
        page_items = filtered_items[offset : offset + rows]

        
        for idx, item in enumerate(page_items):
            item['original_index'] = idx
            
        def check_oa(res_item):
            item_doi = res_item['doi']
            up_url = f"https://api.unpaywall.org/v2/{item_doi}?email={UNPAYWALL_EMAIL}"
            try:
                up_req = urllib.request.Request(up_url, headers=HEADERS)
                with urllib.request.urlopen(up_req, timeout=3) as up_res:
                     up_data = json.loads(up_res.read().decode())
                     if up_data.get('is_oa') or up_data.get('best_oa_location'):
                          res_item['is_oa'] = True
            except Exception:
                pass
            return res_item
            
        final_page_items = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(check_oa, pi) for pi in page_items]
            for fut in concurrent.futures.as_completed(futures):
                try:
                    final_page_items.append(fut.result())
                except Exception:
                    pass
                    
        final_page_items.sort(key=lambda x: x.get('original_index', 99))
        return final_page_items
    except Exception as e:
        print(f"[ERROR] Crossref search failed: {e}")
        return []
