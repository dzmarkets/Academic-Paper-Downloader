import sys
import os

# Add root project directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.utils import parse_search_query
from src.metadata.crossref import search_crossref

def test_exact_search():
    raw_query = '"Particle swarm optimization with adaptive mutation for multimodal optimization" Hui Wang, Wenjun Wang, Zhijian Wu, 2013'
    print(f"[TEST] Testing query: {raw_query}")
    
    parsed = parse_search_query(raw_query)
    print(f"[PARSED] Title: '{parsed['title']}'")
    print(f"[PARSED] Author: '{parsed['author']}'")
    print(f"[PARSED] Year: '{parsed['year']}'")
    
    assert parsed['title'] == "Particle swarm optimization with adaptive mutation for multimodal optimization"
    assert parsed['year'] == "2013"
    assert "Hui Wang" in parsed['author']
    
    results = search_crossref(raw_query, rows=5)
    print(f"[RESULTS] Found {len(results)} matches on Crossref:")
    for res in results:
        print(f"  - Title: {res['title']}")
        print(f"    DOI: {res['doi']}")
        print(f"    Year: {res['year']}")
        print(f"    Authors: {res['authors']}")
        print(f"    Similarity Score: {res.get('similarity', 0):.2f}\n")
        
    assert len(results) > 0, "No results returned!"
    top_result = results[0]
    assert "Particle swarm optimization with adaptive mutation" in top_result['title'], "Title mismatch!"
    assert top_result['year'] == "2013", f"Expected year 2013, got {top_result['year']}"
    print("[SUCCESS] Exact search test passed successfully!")

if __name__ == '__main__':
    test_exact_search()
