# Sci-Hub Human Verification Bypass — Implementation Plan

## Problem

All major Sci-Hub mirrors now use **Cloudflare Turnstile** or redirect-based human verification that blocks plain `urllib`/`curl` requests:
- `sci-hub.ru`, `sci-hub.st`, `sci-hub.su`, `sci-hub.box`, `sci-hub.red`, `sci-hub.al`, `sci-hub.mk`, `sci-hub.ee`, `sci-hub.africa`, `sci-hub.sidesgame.com`, `sci-hub.mobi`, `sci-hub.sh`

The current `scihub.py` uses plain `urllib.request` and `curl`, both of which are instantly detected and blocked.

---

## Strategy

A **3-tier fallback** approach — fastest first, no external services required:

### Tier 1 — `curl_cffi` TLS Fingerprint Spoofing (no browser, fast)
- Installs `curl_cffi` if missing via `pip`
- Impersonates Chrome 124 TLS fingerprint at the network level
- Handles redirect chains, cookies, and compression automatically
- **Covers:** mirrors that use Cloudflare WAF/DDos-GUARD without JS challenge
- **Limitation:** Cannot solve JS-rendered Turnstile "I am human" checkbox

### Tier 2 — `cloudscraper` with Rotate User-Agents (lightweight fallback)
- Installs `cloudscraper` if missing
- Handles older Cloudflare JS challenges (cf_clearance cookies)
- Faster than a headless browser

### Tier 3 — Headless Browser via `selenium` + `undetected-chromedriver` (last resort)
- Only triggered if Tiers 1 & 2 fail
- Opens a headless Chrome with anti-detection patches
- Waits for PDF/download link to appear after challenge is solved automatically
- Automatically dismissed via `undetected-chromedriver`'s UC mode

### Mirror Health Check
- Before each download, quickly probe which mirrors respond (< 5s timeout)
- Skip dead/redirecting-to-verification mirrors
- Cache live mirrors for the session

---

## Files Changed

### [MODIFY] [config.py](file:///f:/Projects/SoftWares/Academic-Paper-Downloader/src/core/config.py)
- Update `SCIHUB_DOMAINS` list with all 12 requested mirrors (remove dead ones, add new ones)
- Add `SCIHUB_BYPASS_TIER` setting (default: `"curl_cffi"`)

### [MODIFY] [scihub.py](file:///f:/Projects/SoftWares/Academic-Paper-Downloader/src/engines/scihub.py)
- Full rewrite of `try_scihub(doi)` with:
  - `_mirror_health_check()` — quick 3s probe of each mirror
  - `_fetch_html_tier1(url)` — `curl_cffi` with Chrome fingerprint
  - `_fetch_html_tier2(url)` — `cloudscraper` fallback
  - `_fetch_html_tier3(url, doi)` — headless selenium fallback
  - `_extract_pdf_url(html, domain)` — robust regex extraction (existing, improved)
  - PDF direct-link detection (many mirrors serve PDF directly at `/{doi}`)

### [NEW] [src/network/browser_fetch.py](file:///f:/Projects/SoftWares/Academic-Paper-Downloader/src/network/browser_fetch.py)
- Isolated headless browser helper (Tier 3)
- Keeps selenium import optional/lazy so app doesn't break if Chrome isn't installed

---

## Open Questions

> [!IMPORTANT]
> **Is Chrome / Chromium installed on this machine?**
> Tier 3 (undetected-chromedriver) requires Chrome. If not installed, Tier 3 will be silently skipped.

> [!NOTE]
> **No Gemini API / paid services used.** All tiers use free, locally-run open-source tools.

---

## Verification Plan

1. Run `python -c "from src.engines.scihub import try_scihub; try_scihub('10.1016/j.amc.2013.06.074')"` from project root
2. Confirm PDF downloaded to `Downloads/Papers/`
3. Confirm console shows which tier succeeded (e.g., `[TIER 1] curl_cffi — OK`)
