import json
import os
import sys
from src.core.utils import get_data_filepath

_journal_map = None

def get_journal_homepage(issn):
    """Return the homepage URL for a given ISSN if resolved, else None."""
    global _journal_map
    if _journal_map is None:
        _journal_map = {}
        try:
            path = get_data_filepath("journal_issn_to_url.json")
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    _journal_map = json.load(f)
                print(f"[INFO] Loaded {len(_journal_map)} journal homepage mappings from: {path}")
            else:
                print(f"[WARNING] Journal lookup map not found at: {path}")
        except Exception as e:
            print(f"[WARNING] Failed to load journal lookup map: {e}")
            
    if not issn:
        return None
        
    # Standardize ISSN lookup (trim, remove spaces and hyphens, and uppercase)
    issn_clean = issn.strip().replace(" ", "").replace("-", "").upper()
    if len(issn_clean) == 8:
        issn_hyphen = f"{issn_clean[:4]}-{issn_clean[4:]}"
    else:
        issn_hyphen = issn.strip().upper()
        
    return _journal_map.get(issn_hyphen) or _journal_map.get(issn_clean)


_PUBLISHER_HOMEPAGES = {
    "10.1109": "https://ieeexplore.ieee.org",
    "10.1063": "https://pubs.aip.org",
    "10.1007": "https://link.springer.com",
    "10.1186": "https://link.springer.com",
    "10.1134": "https://link.springer.com",
    "10.1057": "https://link.springer.com",
    "10.1016": "https://www.sciencedirect.com",
    "10.1002": "https://onlinelibrary.wiley.com",
    "10.1111": "https://onlinelibrary.wiley.com",
    "10.1093": "https://academic.oup.com",
    "10.1177": "https://journals.sagepub.com",
    "10.3390": "https://www.mdpi.com",
    "10.3389": "https://www.frontiersin.org",
    "10.1145": "https://dl.acm.org",
    "10.1088": "https://iopscience.iop.org",
    "10.3847": "https://iopscience.iop.org",
    "10.1021": "https://pubs.acs.org",
    "10.1371": "https://plos.org",
    "10.5281": "https://zenodo.org",
    "10.1103": "https://journals.aps.org",
    "10.20906": "https://www.sba.org.br",
}

def get_doi_prefix(doi):
    if not doi:
        return None
    clean_doi = doi
    if clean_doi.startswith("http://") or clean_doi.startswith("https://"):
        if "doi.org/" in clean_doi:
            clean_doi = clean_doi.split("doi.org/", 1)[1]
    
    if clean_doi.startswith("10."):
        parts = clean_doi.split("/")
        if parts:
            return parts[0]
    return None

def resolve_journal_url(issns, doi=None):
    """Resolve journal homepage URL from ISSN list or fallback to DOI publisher homepage."""
    if issns:
        if isinstance(issns, str):
            issns = [issns]
        for issn in issns:
            url = get_journal_homepage(issn)
            if url:
                return url
                
    prefix = get_doi_prefix(doi)
    if prefix:
        if prefix in _PUBLISHER_HOMEPAGES:
            return _PUBLISHER_HOMEPAGES[prefix]
        for k, v in _PUBLISHER_HOMEPAGES.items():
            if prefix.startswith(k):
                return v
    return None


_journal_details_map = None
_journal_title_map = None

def is_category_a(source):
    if not source:
        return False
    src_lower = source.strip().lower()
    return src_lower in ["a.pdf", "cnrs.pdf", "aeres.pdf"]

def get_journal_details(issn):
    """Return a dictionary of journal details (ISSN, EISSN, Category, Rank) if found."""
    global _journal_details_map, _journal_title_map
    if _journal_details_map is None:
        _journal_details_map = {}
        _journal_title_map = {}
        try:
            path_a = get_data_filepath("resolved_journal_links.json")
            path_b = get_data_filepath("extracted_journals.json")
            
            # Load all extracted journals to get their original source lists
            if os.path.exists(path_b):
                with open(path_b, "r", encoding="utf-8") as f:
                    b_data = json.load(f)
                for k, v in b_data.items():
                    if isinstance(v, dict):
                        source = v.get("source", "SCOPUS.pdf")
                        is_a = is_category_a(source)
                        details = {
                            "issn": v.get("issn", k),
                            "eissn": v.get("eissn", ""),
                            "category": "A" if is_a else "B",
                            "rank": "High" if is_a else "Medium"
                        }
                        _journal_details_map[k.strip().upper()] = details
                        eissn_val = v.get("eissn")
                        if eissn_val:
                            _journal_details_map[eissn_val.strip().upper()] = details
                        
                        title_val = v.get("title")
                        if title_val:
                            _journal_title_map[title_val.strip().lower()] = details
            
            # Overlay resolved URLs and alternate ISSNs, respecting original source tags
            if os.path.exists(path_a):
                with open(path_a, "r", encoding="utf-8") as f:
                    a_data = json.load(f)
                for k, v in a_data.items():
                    if isinstance(v, dict):
                        issns = v.get("issn_list", [k])
                        source = v.get("source", "A.pdf")
                        
                        # Determine Category / Rank correctly
                        if is_category_a(source):
                            category = "A"
                            rank = "High"
                        elif source in ["SCOPUS.pdf", "SCOPUS_LT.pdf", "De_Gruyter.pdf", "Erih_plus.pdf", "Journal_quality.pdf", "Finacial_Times.pdf"]:
                            category = "B"
                            rank = "Medium"
                        else:  # OpenAlex or other
                            # Try to find existing category from _journal_details_map
                            existing_category = None
                            for issn_val in issns:
                                existing = _journal_details_map.get(issn_val.strip().upper())
                                if existing:
                                    existing_category = existing["category"]
                                    break
                            category = existing_category if existing_category else "B"
                            rank = "High" if category == "A" else "Medium"

                        details = {
                            "issn": issns[0] if issns else k,
                            "eissn": issns[1] if len(issns) > 1 else "",
                            "category": category,
                            "rank": rank
                        }
                        for issn_val in issns:
                            _journal_details_map[issn_val.strip().upper()] = details
                        
                        title_val = v.get("title")
                        if title_val:
                            _journal_title_map[title_val.strip().lower()] = details
                            
            print(f"[INFO] Loaded {len(_journal_details_map)} journal details records and {len(_journal_title_map)} titles.")
        except Exception as e:
            print(f"[WARNING] Failed to load journal details: {e}")
            
    if not issn:
        return None
        
    issn_clean = issn.strip().replace(" ", "").replace("-", "").upper()
    if len(issn_clean) == 8:
        issn_hyphen = f"{issn_clean[:4]}-{issn_clean[4:]}"
    else:
        issn_hyphen = issn.strip().upper()
        
    return _journal_details_map.get(issn_hyphen) or _journal_details_map.get(issn_clean)

def get_journal_details_by_title(title):
    """Return a dictionary of journal details by title if found."""
    global _journal_title_map
    if _journal_title_map is None:
        get_journal_details("dummy")
    if not title:
        return None
    return _journal_title_map.get(title.strip().lower())

