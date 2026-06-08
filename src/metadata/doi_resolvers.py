import urllib.request
import urllib.parse
import json
from src.core.config import HEADERS
from src.core.utils import register_discovered_url
from src.network.client import fetch_html_resilient

def resolve_doi_via_handle_api(doi):
    """Query handle API to get the resolved URL of a DOI."""
    if not doi:
        return None
    print(f"[INFO] Resolving DOI {doi} via hdl.handle.net API...")
    url = f"https://hdl.handle.net/api/handles/{doi}"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            
        values = data.get('values', [])
        for value in values:
            if value.get('type') == 'URL':
                resolved_url = value.get('data', {}).get('value')
                if resolved_url:
                    print(f"[INFO] Handle API resolved DOI to: {resolved_url}")
                    register_discovered_url(resolved_url, "Publisher Resource Page (Handle API)")
                    return resolved_url
    except Exception as e:
        print(f"[WARNING] Handle API resolution failed: {e}")
    return None


def resolve_doi_to_url(doi):
    """Query Crossref API to find the primary resource URL of a DOI."""
    if not doi:
        return None
    print(f"[INFO] Resolving DOI {doi} via Crossref API...")
    url = f"https://api.crossref.org/works/{doi}"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
        
        resource_url = data.get('message', {}).get('resource', {}).get('primary', {}).get('URL')
        if resource_url:
            register_discovered_url(resource_url, "Publisher Resource Page")
            return resource_url
            
        # Fallback to look in 'link' array if primary resource URL is missing
        links = data.get('message', {}).get('link', [])
        for link in links:
            intended_url = link.get('URL')
            if intended_url:
                register_discovered_url(intended_url, "Publisher Resource Page")
                return intended_url
    except Exception as e:
        print(f"[WARNING] Crossref DOI resolution failed: {e}")
        
    # Backup: Query Handle REST API (never blocked by Cloudflare)
    return resolve_doi_via_handle_api(doi)


def resolve_doi_metadata(doi):
    """Query Crossref API to resolve a DOI to its title, publication year, and authors."""
    if not doi:
        return None
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
    try:
        # Use fetch_html_resilient to allow curl fallback on 403 blocks
        res_text = fetch_html_resilient(url)
        if res_text:
            data = json.loads(res_text)
            message = data.get('message', {})
            title_list = message.get('title', [])
            title = title_list[0] if title_list else None
            
            # Extract publication year
            year = None
            pub_date = message.get('published-print') or message.get('published-online') or message.get('created')
            if pub_date:
                date_parts = pub_date.get('date-parts', [])
                if date_parts and date_parts[0]:
                    year = str(date_parts[0][0])
            
            # Extract authors
            authors = []
            author_list = message.get('author', [])
            for aut in author_list:
                given = aut.get('given', '').strip()
                family = aut.get('family', '').strip()
                if given and family:
                    authors.append(f"{given} {family}")
                elif family:
                    authors.append(family)
                elif given:
                    authors.append(given)
            
            return {
                'title': title,
                'year': year,
                'doi': doi,
                'authors': authors
            }
    except Exception as e:
        print(f"[WARNING] Crossref DOI metadata resolution failed: {e}")
    return None
