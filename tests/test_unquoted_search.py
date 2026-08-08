import sys
import os

# Add root project directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.utils import parse_search_query
from src.metadata.crossref import search_crossref

def test_unquoted_search():
    unquoted_query = "Particle swarm optimization with adaptive mutation for multimodal optimization Hui Wang, Wenjun Wang, Zhijian Wu, 2013"
    print(f"\n[TEST] Testing UNQUOTED Query:\n'{unquoted_query}'")
    
    parsed = parse_search_query(unquoted_query)
    
    assert parsed['year'] == "2013", f"Expected year '2013', got '{parsed['year']}'"
    print(f"[VERIFIED] Year correctly extracted: {parsed['year']}")
    
    results = search_crossref(unquoted_query, rows=5)
    
    assert len(results) > 0, "No results returned for unquoted search!"
    top = results[0]
    
    print("\n" + "="*70)
    print(f"[STEP 3/3] VERIFYING SEARCH RESULTS & CANDIDATE RANKING")
    print(f"  - Top Match Title   : {top['title']}")
    print(f"  - Top Match DOI     : {top['doi']}")
    print(f"  - Top Match Year    : {top['year']}")
    print(f"  - Top Match Authors : {top['authors']}")
    print(f"  - Similarity Score  : {top.get('similarity', 0.0):.2f}")
    print("="*70)
    
    assert top['year'] == "2013", f"Expected top match year 2013, got {top['year']}"
    assert top.get('similarity', 0.0) >= 0.70, "Similarity score too low!"
    print("\n[SUCCESS] Unquoted 2-stage exact search test passed successfully!")

if __name__ == '__main__':
    test_unquoted_search()
