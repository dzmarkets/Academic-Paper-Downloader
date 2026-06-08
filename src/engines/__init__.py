# Download strategies package

from src.engines.unpaywall import try_unpaywall
from src.engines.scihub import try_scihub
from src.engines.taylorfrancis import try_download_taylorfrancis
from src.engines.book import try_download_book
from src.engines.arxiv import try_arxiv
from src.engines.europe_pmc import try_europe_pmc
from src.engines.ssrn import try_ssrn
from src.engines.astesj import try_astesj
from src.engines.core_ac import try_core
from src.engines.libgen import try_libgen
from src.engines.plos import try_plos
from src.engines.biorxiv import try_biorxiv
from src.engines.publisher import try_publisher_direct
from src.engines.zenodo import try_zenodo
from src.engines.doaj import try_doaj
from src.engines.semantic_scholar import try_semantic_scholar
from src.engines.researchgate import try_researchgate

