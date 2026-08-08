import sys
import os

# Add root project directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.gui.main_window import score_and_rank_results

def test_gui_ranking():
    # Simulated search results array returned by APIs
    mock_results = [
        {
            'title': 'Recent 2026 Open Access Paper on PSO',
            'doi': '10.1000/recent.2026',
            'year': '2026',
            'journal': 'PLOS ONE',
            'is_oa': True,
            'similarity': 0.35
        },
        {
            'title': 'Particle swarm optimization with adaptive mutation for multimodal optimization',
            'doi': '10.1016/j.amc.2013.06.074',
            'year': '2013',
            'journal': 'Applied Mathematics and Computation',
            'is_oa': False,
            'similarity': 1.00
        },
        {
            'title': 'Another 2025 Frontiers Open Access Paper',
            'doi': '10.1000/frontiers.2025',
            'year': '2025',
            'journal': 'Frontiers in Computer Science',
            'is_oa': True,
            'similarity': 0.40
        }
    ]
    
    ranked = score_and_rank_results(mock_results)
    
    print("\n[TEST] Ranked Results Order:")
    for idx, r in enumerate(ranked):
        print(f"  [{idx+1}] Title: {r['title']}")
        print(f"      Similarity: {r.get('similarity', 0.0):.2f} | Year: {r['year']} | OA: {r['is_oa']}")
        
    top = ranked[0]
    assert top['doi'] == '10.1016/j.amc.2013.06.074', f"Expected exact match paper at #1, got '{top['title']}'"
    assert top['similarity'] == 1.00, "Top result similarity should be 1.00"
    print("\n[SUCCESS] GUI ranking test passed successfully! Exact match is placed at #1 on Page 1.")

if __name__ == '__main__':
    test_gui_ranking()
