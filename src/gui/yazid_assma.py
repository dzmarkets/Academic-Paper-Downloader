import re
from src.network.client import fetch_html_resilient

def fetch_yazid_rg_publications():
    """Retrieve Yazid Youcef's publications, attempting live scraping with a guaranteed local fallback."""
    profile_url = "https://www.researchgate.net/profile/Yazid-Youcef"
    
    # 1. Guaranteed robust fallback list of Yazid Youcef's high-quality publications
    local_works = [
        {
            'title': "Intelligent and Secure Homes: IoT Solutions for Advanced Monitoring and Communication",
            'doi': "https://www.researchgate.net/profile/Yazid-Youcef",
            'authors': "Yazid Youcef",
            'year': "2025",
            'journal': "University of Batna 2 (Thesis)",
            'is_oa': True,
            'source': 'yazid_profile'
        },
        {
            'title': "Design and Build IoT Smart Home System with Blocks Based App Inventor Programming",
            'doi': "https://www.researchgate.net/profile/Yazid-Youcef",
            'authors': "Yazid Youcef",
            'year': "2025",
            'journal': "ResearchGate (Technical Report)",
            'is_oa': True,
            'source': 'yazid_profile'
        }
    ]
    
    # 2. Attempt live parse from his ResearchGate profile
    try:
        page_html = fetch_html_resilient(profile_url)
        if page_html and "gtm-research-item" in page_html:
            parts = page_html.split('gtm-research-item')
            parsed_results = []
            for part in parts[1:]:
                link_match = re.search(r'href="([^"]*researchgate\.net/publication/[^"]*)"[^>]*>(.*?)</a>', part)
                if not link_match:
                    link_match = re.search(r'href="(/publication/[^"]+)"[^>]*>(.*?)</a>', part)
                if not link_match:
                    continue
                    
                pub_url = link_match.group(1)
                if pub_url.startswith('/'):
                    pub_url = "https://www.researchgate.net" + pub_url
                title = re.sub('<[^<]+?>', '', link_match.group(2)).strip()
                
                type_match = re.search(r'class="[^"]*nova-legacy-v-entity-item__badge[^"]*"[^>]*>(.*?)</span>', part)
                pub_type = type_match.group(1).strip() if type_match else ""
                
                date_match = re.search(r'class="[^"]*nova-legacy-v-entity-item__meta-data-item[^"]*"[^>]*>\s*<span[^>]*>(.*?)</span>', part)
                if not date_match:
                    date_match = re.search(r'<span[^>]*>\s*([A-Za-z]{3}\s+\d{4}|\d{4})\s*</span>', part)
                pub_date = date_match.group(1).strip() if date_match else "n.d."
                year = "n.d."
                year_match = re.search(r'\b(19\d{2}|20\d{2})\b', pub_date)
                if year_match:
                    year = year_match.group(1)
                    
                is_oa = "Full-text available" in part or "Download" in part
                
                parsed_results.append({
                    'title': title,
                    'doi': pub_url,
                    'authors': "Yazid Youcef",
                    'year': year,
                    'journal': f"ResearchGate ({pub_type})" if pub_type else "ResearchGate",
                    'is_oa': is_oa,
                    'source': 'yazid_profile'
                })
            if parsed_results:
                seen_titles = set()
                deduped = []
                for p in parsed_results:
                    t_low = p['title'].lower().strip()
                    if t_low not in seen_titles:
                        seen_titles.add(t_low)
                        deduped.append(p)
                print(f"[INFO] Successfully retrieved {len(deduped)} publications dynamically from Yazid Youcef's profile.")
                return deduped
    except Exception as e:
        print(f"[WARNING] Live ResearchGate profile query bypassed/failed: {e}")
        
    print("[INFO] Utilizing guaranteed local profile publications fallback.")
    return local_works


def fetch_assma_publications():
    """Retrieve Assma Derdoukh's publications using a guaranteed local fallback."""
    local_works = [
        {
            'title': "On the Robust Stability of Positive Delay Systems Under Time-varying Perturbations",
            'doi': "http://bmathaa.org/repository/docs/BMAA17-1-7.pdf",
            'authors': "Assma Derdoukh, Maissa Kada",
            'year': "2025",
            'journal': "Bulletin of Mathematical Analysis and Applications",
            'is_oa': True,
            'source': 'assma_profile'
        },
        {
            'title': "Sur la méthode de Fourier pour l'étude d'une classe d'équations opératorielles",
            'doi': "https://bu.umc.edu.dz/md/index.php?lvl=more_results&mode=keyword&user_query=Indices+de+d%C3%A9faut&tags=ok",
            'authors': "Assma Derdoukh",
            'year': "2023",
            'journal': "Université Constantine 1 (Thesis)",
            'is_oa': False,
            'source': 'assma_profile'
        }
    ]
    return local_works
