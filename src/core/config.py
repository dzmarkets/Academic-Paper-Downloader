# Configuration constants

VERSION = "3.0.1.0"

UNPAYWALL_EMAIL = "researcher@domain.com"

SCIHUB_DOMAINS = [
    # Primary mirrors (user-requested)
    "https://sci-hub.ru",
    "https://sci-hub.st",
    "https://sci-hub.su",
    "https://sci-hub.box",
    "https://sci-hub.red",
    "https://sci-hub.al",
    "https://sci-hub.mk",
    "https://sci-hub.ee",
    "https://sci-hub.africa",
    "https://sci-hub.sidesgame.com",
    "https://sci-hub.mobi",
    "https://sci-hub.sh",
    # Fallback mirrors
    "https://sci-hub.se",
    "https://sci-hub.ren",
    "https://www.sci-hub.pub",
]

# Bypass tier preference order: "curl_cffi" → "cloudscraper" → "selenium"
SCIHUB_BYPASS_TIER = "curl_cffi"

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
