import urllib.request
import urllib.parse
import json
from src.core import state
from src.core.config import HEADERS

def search_openlibrary(query, author="", offset=0, rows=5):
    """Query OpenLibrary API for books — much more accurate than Crossref for book searches.
    
    Returns books with a `can_download` field: True only when we have a viable
    programmatic download path (Internet Archive ID → direct PDF or CDL image scrape,
    or a known Taylor & Francis DOI prefix → T&F API). Books with only isbn:/ol:
    identifiers cannot be downloaded automatically and are excluded from results.
    """
    if not query:
        return []
    clean_query = query.strip().strip('"').strip("'").strip('[').strip(']').strip()
    clean_author = author.strip().strip('"').strip("'") if author else ""
    
    params = f"title={urllib.parse.quote(clean_query)}"
    if clean_author:
        params += f"&author={urllib.parse.quote(clean_author)}"
    params += "&fields=title,author_name,first_publish_year,isbn,publisher,key,ia&limit=100"
    url = f"https://openlibrary.org/search.json?{params}"
    
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=12) as response:
            data = json.loads(response.read().decode())
        
        docs = data.get('docs', [])
        filtered = []
        for doc in docs:
            title = doc.get('title', '')
            if not title:
                continue
            author_names = doc.get('author_name', [])
            if not author_names:
                continue
            authors_str = ", ".join(author_names[:4])  # cap at 4 authors
            year = str(doc.get('first_publish_year', 'n.d.'))
            publishers = doc.get('publisher', [])
            publisher_str = publishers[0] if publishers else "OpenLibrary"
            
            # Retrieve identifiers to build a pseudo-DOI for the pipeline
            ol_key = doc.get('key', '')  # e.g. /works/OL12345W
            isbns = doc.get('isbn', [])
            ia_ids = doc.get('ia', [])
            
            doi = ""
            can_download = False
            if ia_ids:
                doi = f"ia:{ia_ids[0]}"
                can_download = True   # Internet Archive: direct PDF or CDL image scrape
            elif isbns:
                doi = f"isbn:{isbns[0]}"
                can_download = False  # No direct programmatic download path
            elif ol_key:
                doi = f"ol:{ol_key.replace('/works/', '')}"
                can_download = False  # No direct programmatic download path
            
            # Skip entries with no identifier at all
            if not doi:
                continue
                
            # Only include books we can actually download
            if not can_download:
                continue
                
            filtered.append({
                'title': title,
                'doi': doi,
                'ol_key': ol_key,
                'authors': authors_str,
                'year': year,
                'journal': publisher_str,
                'is_oa': can_download,
                'can_download': can_download,
                'source': 'openlibrary'
            })
        
        page_items = filtered[offset: offset + rows]
        for idx, item in enumerate(page_items):
            item['original_index'] = idx
        return page_items
    except Exception as e:
        print(f"[ERROR] OpenLibrary search failed: {e}")
        return []
