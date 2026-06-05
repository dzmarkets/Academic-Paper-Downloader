# GitHub Release Notes
# =====================
# Usage: For each new release, fill in the section below.
#        Copy the TITLE and BODY into GitHub's "Create a new release" form:
#          → https://github.com/dzmarkets/Academic-Paper-Downloader/releases/new
#
# Tag convention : v{VERSION}   (e.g. v2.3.7)
# Asset to upload: Academic_Paper_Downloader_v{VERSION}_Setup.exe
# ─────────────────────────────────────────────────────────────────────────────


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
