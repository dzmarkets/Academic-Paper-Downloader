# Configuration constants

VERSION = "3.0.0.0"

UNPAYWALL_EMAIL = "researcher@domain.com"

SCIHUB_DOMAINS = [
    "https://sci-hub.se",
    "https://sci-hub.st",
    "https://sci-hub.ru",
    "https://sci-hub.africa",
    "https://sci-net.xyz",
    "https://sci-hubse.com",
    "https://www.sci-hub.pub"
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5'
}

# Mapping from document category → descriptive folder name
_FOLDER_FOR_CATEGORY = {
    "book":   "Books",
    "thesis": "Theses",
    "paper":  "Papers",
    "others": "Others",
}

# Known Taylor & Francis / CRC Press / Routledge DOI prefixes
_TF_DOI_PREFIXES = (
    "10.1201/",  # CRC Press / Taylor & Francis books
    "10.4324/",  # Routledge books
    "10.1080/",  # T&F journals
    "10.3109/",  # Informa Healthcare
    "10.3390/",  # MDPI (not T&F, but shares API pattern)
)
