"""
scihub.py — Strategy 2: Sci-Hub Shadow Library download engine.

Uses a 3-tier bypass stack to defeat Cloudflare Turnstile and other
human-verification gates used by all major Sci-Hub mirrors:

  Tier 1 — curl_cffi   : Chrome TLS fingerprint spoofing (fast, no browser)
  Tier 2 — cloudscraper: Cloudflare JS-challenge cookie solver (medium)
  Tier 3 — selenium UC : Real headless Chrome (slow, last resort)
"""

import re
import os
import sys
import subprocess
import urllib.request
import urllib.error

from src.core import state
from src.core.config import SCIHUB_DOMAINS, HEADERS
from src.core.utils import register_discovered_url, get_download_dir
from src.network.downloader import download_file


# ---------------------------------------------------------------------------
# Dependency helpers — lazy-install packages without crashing the whole app
# ---------------------------------------------------------------------------

def _install_pkg(pkg_name, import_name=None):
    """Silently pip-install a package and return True on success."""
    import_name = import_name or pkg_name
    try:
        __import__(import_name)
        return True
    except ImportError:
        pass
    try:
        print(f"[SCI-HUB] Installing {pkg_name} ...")
        extra = {"creationflags": 0x08000000} if os.name == "nt" else {}
        subprocess.run(
            [sys.executable, "-m", "pip", "install", pkg_name, "-q"],
            check=True, capture_output=True, **extra
        )
        __import__(import_name)
        print(f"[SCI-HUB] {pkg_name} installed successfully.")
        return True
    except Exception as e:
        print(f"[SCI-HUB] Could not install {pkg_name}: {e}")
        return False


# ---------------------------------------------------------------------------
# Mirror health check — quickly probe which mirrors are reachable
# ---------------------------------------------------------------------------

def _mirror_alive(domain, timeout=5):
    """Return True if the mirror responds with HTTP 200/301/302 within timeout."""
    try:
        req = urllib.request.Request(
            domain,
            headers={"User-Agent": HEADERS["User-Agent"]},
            method="HEAD"
        )
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status in (200, 301, 302, 403)
    except Exception:
        # 403 might still mean the server is live — curl_cffi can handle it
        try:
            req2 = urllib.request.Request(domain, headers={"User-Agent": HEADERS["User-Agent"]})
            with urllib.request.urlopen(req2, timeout=timeout) as r2:
                return True
        except Exception:
            return False


# ---------------------------------------------------------------------------
# Tier 1 — curl_cffi (Chrome TLS fingerprint spoofing)
# ---------------------------------------------------------------------------

def _fetch_tier1(url):
    """Fetch URL impersonating Chrome 124 at the TLS layer. Returns HTML or None."""
    if not _install_pkg("curl_cffi", "curl_cffi"):
        return None
    try:
        from curl_cffi import requests as cffi_requests
        resp = cffi_requests.get(
            url,
            impersonate="chrome124",
            timeout=30,
            allow_redirects=True,
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
            }
        )
        if resp.status_code in (200, 206):
            return resp.text
        print(f"[TIER 1] HTTP {resp.status_code} for {url}")
        return None
    except Exception as e:
        err_str = str(e)
        if "28" in err_str or "timed out" in err_str.lower() or "timeout" in err_str.lower():
            print(f"[TIER 1] Timeout after 30s for {url} — skipping.")
        else:
            print(f"[TIER 1] curl_cffi error: {e}")
        return None



def _fetch_pdf_tier1(pdf_url):
    """Download PDF bytes via curl_cffi. Returns bytes or None."""
    if not _install_pkg("curl_cffi", "curl_cffi"):
        return None
    try:
        from curl_cffi import requests as cffi_requests
        resp = cffi_requests.get(
            pdf_url,
            impersonate="chrome124",
            timeout=60,
            allow_redirects=True,
            headers={"Accept": "application/pdf,*/*;q=0.8"}
        )
        if resp.status_code == 200 and resp.content[:4] == b"%PDF":
            return resp.content
        return None
    except Exception as e:
        print(f"[TIER 1] PDF download error: {e}")
        return None


# ---------------------------------------------------------------------------
# Tier 2 — cloudscraper (JS-challenge cookie bypass)
# ---------------------------------------------------------------------------

def _fetch_tier2(url):
    """Fetch URL using cloudscraper to bypass JS challenges. Returns HTML or None."""
    if not _install_pkg("cloudscraper"):
        return None
    try:
        import cloudscraper
        scraper = cloudscraper.create_scraper(browser={
            "browser": "chrome",
            "platform": "windows",
            "mobile": False
        })
        resp = scraper.get(url, timeout=20, allow_redirects=True)
        if resp.status_code == 200:
            return resp.text
        print(f"[TIER 2] HTTP {resp.status_code} for {url}")
        return None
    except Exception as e:
        print(f"[TIER 2] cloudscraper error: {e}")
        return None


def _fetch_pdf_tier2(pdf_url):
    """Download PDF bytes via cloudscraper. Returns bytes or None."""
    if not _install_pkg("cloudscraper"):
        return None
    try:
        import cloudscraper
        scraper = cloudscraper.create_scraper()
        resp = scraper.get(pdf_url, timeout=30, allow_redirects=True)
        if resp.status_code == 200 and resp.content[:4] == b"%PDF":
            return resp.content
        return None
    except Exception as e:
        print(f"[TIER 2] PDF download error: {e}")
        return None


# ---------------------------------------------------------------------------
# Tier 3 — Headless Chrome (full JS execution)
# ---------------------------------------------------------------------------

def _fetch_tier3(url):
    """Fetch URL via real headless Chrome. Returns HTML or None."""
    try:
        from src.network.browser_fetch import fetch_html_headless
        return fetch_html_headless(url, wait_seconds=12)
    except Exception as e:
        print(f"[TIER 3] Error: {e}")
        return None


# ---------------------------------------------------------------------------
# PDF URL extractor — works on all known Sci-Hub page layouts
# ---------------------------------------------------------------------------

def _extract_pdf_url(html, domain):
    """
    Parse HTML from a Sci-Hub page and return the most likely PDF URL.
    Handles all known Sci-Hub embed layouts.
    """
    candidates = []

    # Pattern 1: <embed src="...pdf...">  or  <iframe src="...">
    candidates += re.findall(r'<(?:embed|iframe)[^>]+src=["\']([^"\']+)["\']', html, re.IGNORECASE)

    # Pattern 2: location.href = '...'  or  window.location = '...'
    candidates += re.findall(r'(?:location\.href|window\.location)\s*=\s*["\']([^"\']+)["\']', html)

    # Pattern 3: Quoted .pdf paths in JS strings or attributes
    candidates += re.findall(r'["\']([^"\']*\.pdf[^"\']*)["\']', html)

    # Pattern 4: href/src attributes containing .pdf
    candidates += re.findall(r'(?:href|src)=["\']([^"\']*\.pdf[^"\']*)["\']', html, re.IGNORECASE)

    # Pattern 5: <a href="..."> links containing /pdf/ or .pdf
    candidates += re.findall(r'href=["\']([^"\']*(?:/pdf/|download)[^"\']*)["\']', html, re.IGNORECASE)

    # Pattern 6: Newer Sci-Hub layout — data-src attributes
    candidates += re.findall(r'data-src=["\']([^"\']+)["\']', html, re.IGNORECASE)

    # Normalise, deduplicate, and filter
    filtered_candidates = []
    seen = set()
    for path in candidates:
        path = path.strip().replace("\\", "")
        if not path or len(path) < 5:
            continue
        
        # Skip garbage matches (e.g. large CSS blocks matched by greedy regex)
        if any(bad in path for bad in ['\n', '\r', '<', '>', '{', '}']):
            continue

        if path.startswith("//"):
            path = "https:" + path
        elif path.startswith("/"):
            path = domain.rstrip("/") + path
        elif not path.startswith("http"):
            path = domain.rstrip("/") + "/" + path

        # Skip obvious non-PDFs
        if any(x in path.lower() for x in [".js", ".css", ".png", ".jpg", ".gif", "javascript:"]):
            continue

        if path not in seen:
            seen.add(path)
            filtered_candidates.append(path)

    # Prefer paths that explicitly contain .pdf or /pdf/
    pdf_candidates = [p for p in filtered_candidates if ".pdf" in p.lower() or "/pdf/" in p.lower()]
    other_candidates = [p for p in filtered_candidates if p not in pdf_candidates]

    return (pdf_candidates + other_candidates) or None


# ---------------------------------------------------------------------------
# Save PDF bytes to disk
# ---------------------------------------------------------------------------

def _save_pdf(content, doi):
    """Write PDF bytes to the Papers downloads folder. Returns path or None."""
    downloads_dir = get_download_dir("paper")
    os.makedirs(downloads_dir, exist_ok=True)
    filename = re.sub(r'[<>:"/\\|?*]', "_", doi) + ".pdf"
    filepath = os.path.join(downloads_dir, filename)
    try:
        with open(filepath, "wb") as f:
            f.write(content)
        print(f"[SUCCESS] Saved: '{filename}'")
        print(f"[INFO] Location: {filepath}")
        return filepath
    except Exception as e:
        print(f"[ERROR] Could not save PDF: {e}")
        return None


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def try_scihub(doi):
    """
    Strategy 2: Download a paper via Sci-Hub using a 3-tier bypass stack.

    Parameters
    ----------
    doi : str
        Clean DOI string, e.g. '10.1016/j.amc.2013.06.074'

    Returns
    -------
    bool
        True if the PDF was downloaded successfully.
    """
    if not doi:
        print("\n--- [STRATEGY 2] Skipped (No DOI available) ---")
        return False
    if doi.startswith("http://") or doi.startswith("https://"):
        print("\n--- [STRATEGY 2] Skipped (DOI looks like a URL, not a clean DOI) ---")
        return False

    print("\n--- [STRATEGY 2] Querying Sci-Hub Shadow Library Mirrors ---")
    print(f"[SCI-HUB] Target DOI: {doi}")
    print(f"[SCI-HUB] Bypass stack: Tier 1 (curl_cffi) -> Tier 2 (cloudscraper) -> Tier 3 (headless Chrome)")

    tiers = [
        ("TIER 1 [curl_cffi]",    _fetch_tier1,    _fetch_pdf_tier1),
        ("TIER 2 [cloudscraper]", _fetch_tier2,    _fetch_pdf_tier2),
        ("TIER 3 [headless]",     _fetch_tier3,    None),
    ]

    for domain in SCIHUB_DOMAINS:
        if state.abort_requested:
            print("[INFO] Sci-Hub strategy aborted by user.")
            return False

        print(f"\n[SCI-HUB] >> Mirror: {domain}")

        # Quick liveness probe — skip obviously dead mirrors fast
        print(f"[SCI-HUB]   Probing mirror...", end=" ", flush=True)
        alive = _mirror_alive(domain, timeout=4)
        print("alive [OK]" if alive else "unreachable [X]")
        if not alive:
            continue

        page_url = f"{domain}/{doi}"

        for tier_label, fetch_html_fn, fetch_pdf_fn in tiers:
            if state.abort_requested:
                return False

            print(f"[{tier_label}] Fetching: {page_url}")
            html = fetch_html_fn(page_url)

            if not html:
                print(f"[{tier_label}] No HTML returned — trying next tier.")
                continue

            # Detect hard verification walls
            # For Tier 3, ALTCHA is handled internally (auto-click + wait),
            # so only treat it as a hard block if it's still present after
            # the headless session completed.
            if _is_hard_blocked(html, is_tier3=tier_label.startswith("TIER 3")):
                print(f"[{tier_label}] Verification wall detected — escalating to next tier.")
                continue

            # Extract PDF URL(s) from the page
            pdf_urls = _extract_pdf_url(html, domain)
            if not pdf_urls:
                print(f"[{tier_label}] No PDF link found in page HTML.")
                continue

            # Try to download each candidate PDF URL
            for pdf_url in pdf_urls[:3]:
                if state.abort_requested:
                    return False

                print(f"[{tier_label}] Attempting PDF: {pdf_url}")
                register_discovered_url(pdf_url, f"Sci-Hub ({domain})")

                # Try tier-specific PDF fetch first (preserves TLS fingerprint)
                pdf_bytes = None
                if fetch_pdf_fn:
                    pdf_bytes = fetch_pdf_fn(pdf_url)

                # Fall back to generic downloader if tier-specific failed
                if not pdf_bytes:
                    filename = re.sub(r'[<>:"/\\|?*]', "_", doi) + ".pdf"
                    if download_file(pdf_url, filename, referer=page_url):
                        return True
                    continue

                # Validate and save
                if pdf_bytes and pdf_bytes[:4] == b"%PDF":
                    saved = _save_pdf(pdf_bytes, doi)
                    if saved:
                        if state.GUI_MODE:
                            from src.core.utils import open_in_explorer
                            open_in_explorer(saved)
                        return True
                else:
                    print(f"[{tier_label}] Response is not a valid PDF ({len(pdf_bytes) if pdf_bytes else 0} bytes).")

            # If Tier 3 and no PDF URL found, attempt headless direct PDF download
            if tier_label.startswith("TIER 3") and not pdf_urls:
                print("[TIER 3] Attempting direct headless PDF download...")
                try:
                    from src.network.browser_fetch import fetch_pdf_headless
                    downloads_dir = get_download_dir("paper")
                    save_path = os.path.join(downloads_dir, re.sub(r'[<>:"/\\|?*]', "_", doi) + ".pdf")
                    if fetch_pdf_headless(page_url, save_path, wait_seconds=20):
                        if state.GUI_MODE:
                            from src.core.utils import open_in_explorer
                            open_in_explorer(save_path)
                        return True
                except Exception as e:
                    print(f"[TIER 3] Direct PDF download failed: {e}")

            # If a tier succeeded in fetching HTML with content, don't try lower tiers for same mirror
            if html and not _is_hard_blocked(html):
                break

    print("\n[STRATEGY 2] All Sci-Hub mirrors exhausted without success.")
    return False


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _is_hard_blocked(html, is_tier3=False):
    """
    Detect pages that require verification that the current tier cannot solve.

    For Tiers 1 & 2: ALTCHA (and all challenges) are hard blocks.
    For Tier 3:      ALTCHA is handled internally by clicking 'No' + waiting
                     for PoW, so it is NOT a hard block — only return True
                     if the ALTCHA page is *still* present after Tier 3 ran
                     (meaning the auto-click failed for some reason).
    """
    if not html:
        return True
    html_lower = html.lower()

    altcha_indicators = [
        "altcha",
        "are you are robot",
        "altcha.min.js",
    ]
    other_indicators = [
        "verify you are human",
        "checking your browser",
        "ddos-guard",
        "one more step",
        "please complete the security check",
        "enable javascript and cookies",
        "cf-browser-verification",
        "please turn javascript on",
        "recaptcha",
    ]

    has_paper_content = any(x in html_lower for x in [
        "embed", ".pdf", "citation", "doi"
    ])

    is_altcha = any(x in html_lower for x in altcha_indicators)
    is_other_challenge = any(x in html_lower for x in other_indicators)

    if is_tier3:
        # Tier 3 auto-solves ALTCHA — only block if it didn't solve it
        # (ALTCHA page still present) or if there's a non-ALTCHA challenge
        if is_altcha and not has_paper_content:
            return True   # Auto-solve failed, still on ALTCHA page
        return is_other_challenge and not has_paper_content
    else:
        # Tiers 1 & 2: treat ALL challenges as hard blocks
        is_challenge = is_altcha or is_other_challenge
        return is_challenge and not has_paper_content
