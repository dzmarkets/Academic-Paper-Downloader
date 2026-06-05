# GitHub Release Notes
# =====================
# Usage: For each new release, fill in the section below.
#        Copy the TITLE and BODY into GitHub's "Create a new release" form:
#          → https://github.com/dzmarkets/Academic-Paper-Downloader/releases/new
#
# Tag convention : v{VERSION}   (e.g. v2.3.7)
# Asset to upload: Academic_Paper_Downloader_v{VERSION}_Setup.exe
# ─────────────────────────────────────────────────────────────────────────────


## v2.4.0.1
### Release Title
Academic Paper Downloader v2.4.0.1 — 50 New Publisher Integrations & Enhanced OA Heuristics

### Release Body
```
## What's New in v2.4.0.1

### 🚀 Expanded Direct Open-Access Resolvers (Items 51-100)
- **De Gruyter (`10.1515`)**: Direct-path construction for De Gruyter publications (`https://www.degruyter.com/document/doi/{doi}/pdf`).
- **World Scientific (`10.1142`)**: Direct-path resolution for World Scientific publishing (`https://www.worldscientific.com/doi/pdf/{doi}`).
- **Mary Ann Liebert (`10.1089`)**: Direct-path resolution for Mary Ann Liebert publications (`https://www.liebertpub.com/doi/pdf/{doi}`).
- **Georg Thieme (`10.1055`)**: Direct-path resolution for Georg Thieme e-journals (`https://www.thieme-connect.com/products/ejournals/pdf/{doi}.pdf`).
- **ACM (`10.1145`)**: Direct-path resolution for Association for Computing Machinery articles (`https://dl.acm.org/doi/pdf/{doi}`).
- **CSIRO (`10.1071`)**: Direct-path resolution for CSIRO Publishing (`https://www.publish.csiro.au/pdf/{doi}`).
- **American Physiological Society (`10.1152`)**: Direct-path resolution for APS journals (`https://journals.physiology.org/doi/pdf/{doi}`).
- **American Society for Microbiology (`10.1128`)**: Direct-path resolution for ASM publications (`https://journals.asm.org/doi/pdf/{doi}`).
- **Edinburgh University Press (`10.3366`)**: Direct-path resolution for EUP journals (`https://www.euppublishing.com/doi/pdf/{doi}`).
- **Palgrave Macmillan (`10.1057`)**: Integrated under the Springer Open template rules.

### 🛡️ Pipeline & Fallback Validation
- **Unified Trackings**: Mapped and verified 40 additional publisher sub-journals and prefixes (LWW, Brill, Bentham, Cell Press, Duke Press, Wolters Kluwer, Sciendo, etc.) to fallback to Zenodo, Unpaywall, Sci-Hub, PMC, and other mirrors.

### 📦 Metadata & Build Updates
- Incremented application version to `v2.4.0.1` inside all codebase, installer, user-agent, and git tag definitions.

---
**Full Changelog**: https://github.com/dzmarkets/Academic-Paper-Downloader/commits/main
```

## v2.4.0
### Release Title
Academic Paper Downloader v2.4.0 — 25 New Publisher Integrations & Broadened OA Resolution

### Release Body
```
## What's New in v2.4.0

### 🚀 Direct Open-Access Resolvers (Items 26-50)
- **Annual Reviews (`10.1146`)**: Direct-path construction for Annual Reviews publications (`https://www.annualreviews.org/doi/pdf/...`).
- **American Physical Society (APS) (`10.1103`)**: Direct-path resolution for APS journals (`https://journals.aps.org/prl/pdf/...`).
- **University of Chicago Press (`10.1086`)**: Direct-path resolution for Chicago Press journals (`https://www.journals.uchicago.edu/doi/pdf/...`).
- **Royal Society (`10.1098`)**: Direct-path resolution for Royal Society publishing (`https://royalsocietypublishing.org/doi/pdf/...`).
- **ASCE (`10.1061`)**: Direct-path resolution for ASCE library (`https://ascelibrary.org/doi/pdf/...`).
- **Emerald (`10.1108`)**: Direct-path resolution for Emerald Insight (`https://www.emerald.com/insight/content/doi/.../pdf`).
- **SIAM (`10.1137`)**: Direct-path resolution for SIAM publications (`https://epubs.siam.org/doi/pdf/...`).
- **Pleiades Publishing (`10.1134`)**: Integrated under Springer Open rule mappings to query Pleiades publications directly.

### 🛡️ Smart Fallbacks & Loop Prevention
- **Grouped DOI Rules**: Grouped sub-journals (MDPI, Frontiers, Nature, PLOS) under their parent DOI prefixes for maximum code efficiency.
- **Resilient Fallback Pipeline**: Enabled auto-fallbacks to Zenodo, Unpaywall, Sci-Hub, PMC, and other repositories when publishers challenge requests with anti-bot/cookie wall measures.

### 📦 Metadata & Release Management
- Bumped application version to `v2.4.0` in `paper.py`, installer scripts (`installer.iss`, `file_version_info.txt`), User-Agent string, and development tools.

---
**Full Changelog**: https://github.com/dzmarkets/Academic-Paper-Downloader/commits/main
```

## v2.3.9
### Release Title
Academic Paper Downloader v2.3.9 — Stop Action Improvements & GUI Responsiveness

### Release Body
```
## What's New in v2.3.9

### ⚡ Responsive & Instant Cancel State
- **Chunked File Downloading**: Replaced blocking direct downloads with 64KB chunk-based reads, checking the cancel state during download loops to allow immediate abortion of active downloads.
- **Cancel checks in search API calls**: Integrated early cancel hooks inside `fetch_html_resilient`, `search_crossref`, and `search_google_scholar` network requests to prevent UI hangs during slow search queries.

### 🎨 Stop Button Styling & Label Adjustments
- Changed stop button label to `"Stop Downloading"` (instead of `"Stop"`) when the download begins.
- Ensured button text color remains white (`#FFFFFF`) across all Stop modes and states.
- Enabled the Stop functionality for **individual result card downloads**, keeping the main button clickable/normal instead of disabled.
- Properly restored all default values (purple background, white text, `"Search / Download"`) when resetting GUI states.

---
**Full Changelog**: https://github.com/dzmarkets/Academic-Paper-Downloader/commits/main
```

## v2.3.8
### Release Title
Academic Paper Downloader v2.3.8 — Search Quality & Non-Academic Filter

### Release Body
```
## What's New in v2.3.8

### 🔍 Smarter Search Results
- **Non-academic domain filter**: Search results now exclusively return academic papers.
  Links from GitHub, ReadTheDocs, PyPI, StackOverflow, Reddit, Wikipedia, GitLab,
  Bitbucket, Conda, Bioconductor, and other software/documentation sites are
  automatically excluded.
- Fixes an issue where searching for software citations like `deeptools/deepTools: 3.3.1`
  would surface GitHub repository pages and documentation instead of the actual paper.

### 🛠 Bug Fixes
- Scholar results (via DuckDuckGo proxy) are now correctly filtered before being
  displayed alongside Crossref results.

---
**Full Changelog**: https://github.com/dzmarkets/Academic-Paper-Downloader/commits/main
```

---
## v2.3.7
### Release Title
Academic Paper Downloader v2.3.7 - Integrated New Open-Access Resolvers & Explorer Highlight

### Release Body
We are pleased to release **v2.3.7**, featuring a major expansion of our open-access paper resolution network, robust API resilient fallbacks, and a smoother download-to-view user workflow.

### 🚀 What's New

* **5 New Direct PDF Resolvers** 📄
  Added dedicated, direct-path resolvers for:
  * **PLOS Journals**: Instant construction of high-speed printable PDF pathways.
  * **BioRxiv & MedRxiv**: Direct preprint retrieval via the bioRxiv server API.
  * **Zenodo**: Clean record parsing for self-archived datasets and papers.
  * **DOAJ**: Index-based query matching for thousands of peer-reviewed open journals.
  * **Semantic Scholar**: Query optimization using Semantic Scholar's Graph API.

* **Resilient WAF & Cloudflare Bypassing** 🛡️
  Enhanced our JSON API crawler to use system `curl` fallbacks when standard Python requests are blocked by TLS fingerprinting or web application firewalls.

* **Windows Explorer Auto-Highlighting** 📂
  Once a download completes, the application now automatically opens the destination folder in Windows Explorer and highlights/selects the newly downloaded file.

* **Zero-Freeze Background Threading** ⚡
  The explorer launcher runs on dedicated background threads to ensure the Tkinter GUI remains perfectly responsive and never stutters.

* **Automated Integration Test Suite** 🧪
  Created `test_resolvers.py` to continuously validate resolver health, confirm proper `%PDF-` file signatures, and check for rate-limiting.

---

### 📦 Assets
Download the pre-compiled setup installer (`AcademicPaperDownloader_Setup.exe`) below for a seamless, prompt-free Windows installation.

```

---
## v2.3.6
### Release Title
Academic Paper Downloader v2.3.6 — Instant Startup (onedir build)

### Release Body
```
## What's New in v2.3.6

### ⚡ Performance
- Switched to **onedir** PyInstaller build for near-instant application startup.
  No more extraction delay on first launch.

---
**Full Changelog**: https://github.com/dzmarkets/Academic-Paper-Downloader/commits/main
```

---
# ─────────────────────────────────────────────────────────────────────────────
# TEMPLATE — copy this block when preparing a new release
# ─────────────────────────────────────────────────────────────────────────────
#
# ## v{VERSION}
# ### Release Title
# Academic Paper Downloader v{VERSION} — {short description}
#
# ### Release Body
# ```
# ## What's New in v{VERSION}
#
# ### ✨ New Features
# - ...
#
# ### 🔍 Improvements
# - ...
#
# ### 🛠 Bug Fixes
# - ...
#
# ---
# **Full Changelog**: https://github.com/dzmarkets/Academic-Paper-Downloader/commits/main
# ```
