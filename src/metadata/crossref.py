import urllib.request
import urllib.parse
import json
import concurrent.futures
from src.core import state
from src.core.config import HEADERS, UNPAYWALL_EMAIL

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


def search_crossref(query, offset=0, rows=5, type_filter="All", author=""):
    """Query Crossref API for title+author keywords, return paginated list with OA check."""
    if state.abort_requested:
        return []
    if not query:
        return []
    # Detect exact match phrase in quotes (Google-like intelligent search)
    stripped = query.strip()
    is_exact = (stripped.startswith('"') and stripped.endswith('"')) or (stripped.startswith("'") and stripped.endswith("'"))
    exact_phrase = stripped.strip('"').strip("'").strip() if is_exact else None
    
    clean_query = stripped
    clean_author = author.strip().strip('"').strip("'") if author else ""
    # Retrieve more rows to ensure we have enough valid ones after filtering
    crossref_rows = 30 + offset
    # Build URL: use query.title when title given, query.author when author given
    url = "https://api.crossref.org/works?"
    if clean_query and clean_author:
        url += f"query={urllib.parse.quote(clean_query)}&query.author={urllib.parse.quote(clean_author)}"
    elif clean_query:
        url += f"query={urllib.parse.quote(clean_query)}"
    elif clean_author:
        url += f"query.author={urllib.parse.quote(clean_author)}"
    else:
        return []
    url += f"&rows={crossref_rows}&offset=0"
    if type_filter == "Papers":
        url += "&filter=type:journal-article,type:proceedings-article,type:posted-content"
    elif type_filter == "Books":
        url += "&filter=type:book"
    try:
        if state.abort_requested:
            return []
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as response:
            if state.abort_requested:
                return []
            data = json.loads(response.read().decode())
        
        items = data.get('message', {}).get('items', [])
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
                    
            filtered_items.append({
                'title': title,
                'doi': doi,
                'authors': authors_str,
                'year': year,
                'journal': journal,
                'is_oa': False
            })
            
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
