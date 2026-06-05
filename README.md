# 📚 Academic Paper Downloader

> **Version 2.4.0.3**

[![Download Setup Installer](https://img.shields.io/badge/Download-Setup%20Installer-8B5CF6?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/dzmarkets/Academic-Paper-Downloader/releases/download/v2.4.0.3/AcademicPaperDownloader_Setup.exe)

A premium, high-performance desktop application built in Python/Tkinter designed to search, resolve, and download academic papers directly from multiple sources (including ResearchGate and OpenAlex) using advanced crawling pipelines, Cloudflare bypass mechanisms, and a modern user interface.

---

## ✨ Features

- **🚀 Resilient ResearchGate Integration**: Uses a dual-stage search crawler (Yahoo Search + direct publication scraping) with a built-in native `curl` fallback engine to seamlessly bypass Cloudflare and 403 Forbidden blocks.
- **⚡ Direct PDF Link Resolver**: Automatically extracts `/link/.../download` raw PDF URLs from description pages, opening PDFs directly in the web browser instead of profile pages.
- **🎯 Intelligent Identifier Routing**: Detects raw HTTP/HTTPS links instantly, completely bypassing slow metadata queries (Crossref, Unpaywall, Sci-Hub) to trigger immediate direct downloads.
- **🎨 Premium Deep Purple Aesthetic**: Styled under the `clam` theme with a curated, harmonious dark palette, matching customized elements including custom-designed scrollbars.
- **📱 Fully Responsive Auto-Wrapping**: A dynamic `<Configure>` scaling callback automatically handles label `wraplength` configurations based on window width to utilize 100% of the horizontal screen.
- **📬 Algeria-only Support Panel**: Dynamically reveals an elegant horizontal 3-column support card for Algerian IP addresses structured as:
  - **Left: Services** (Highlighting custom freelance web/IoT offerings).
  - **Center: Contact** (Featuring instant WhatsApp, Email, and Location metrics aligned with pixel-perfect accuracy).
  - **Right: Buy Me a Coffee** (Inspiring support action for local innovation 🇩🇿).
- **🚀 Background Update Checker**: Integrates an interactive update trigger (`🔄`) directly in the main header and runs a background query on startup to detect newer releases on GitHub, display release notes, and offer one-click download of the latest `.exe` file.
- **🧹 Clear Results Button**: An instant reset utility built directly into the search results navigation bar to clear results and input fields cleanly.
- **📦 Zero Third-Party Dependencies**: Runs purely on the native Python standard library and Tkinter framework—no bulky package installations required!
- **📂 Smart Download Folders** *(v2.3.6)*: Downloaded files are automatically organized into named subfolders under the user's local `Documents\Academic Paper Downloader\` folder:

  | Document Type | Folder |
  |---|---|
  | Academic Paper | `Papers\` |
  | Book | `Books\` |
  | Thesis | `Theses\` |
  | Other / Unknown | `Others\` |

  Folders are created automatically on first use if they do not already exist.

---

## 🌐 Supported Download Sources

The application features a multi-tiered search and resolution pipeline that queries the following open science repositories, search indices, and archives to find direct download links:

### 📄 Academic Paper Sources
- **Sci-Hub**: Accesses global research mirror networks for paywalled academic papers.
- **ResearchGate**: Native crawler that extracts self-archived publications and preprints directly from researcher profiles.
- **Semantic Scholar**: Utilizes the Semantic Scholar Graph API to retrieve open-access PDF targets.
- **Unpaywall**: Queries the Unpaywall open science database containing millions of free journal articles.
- **CORE (core.ac.uk)**: Searches the world's largest aggregator of open access research papers.
- **DOAJ (Directory of Open Access Journals)**: Direct index searches for peer-reviewed open access papers.
- **PLOS Journals**: Direct, fast-path printable PDF link construction for Public Library of Science articles.
- **BioRxiv & MedRxiv**: Directly queries bioRxiv details API to download medical and biological preprint PDFs.
- **arXiv**: Direct PDF fetch from the arXiv repository for physics, mathematics, and computer science papers.
- **SSRN (Social Science Research Network)**: Native abstract crawling to download social science preprints.
- **Europe PMC**: Queries PubMed Central and Europe PMC mirrors to access free biomedical publications.
- **Annual Reviews / APS / University of Chicago Press / Royal Society / ASCE / Emerald / SIAM / Pleiades**: Expanded direct open-access resolution support for 25 additional publishers.
- **De Gruyter / World Scientific / Mary Ann Liebert / Thieme / ACM / CSIRO / American Physiological Society / ASM / Edinburgh University Press**: Expanded direct open-access resolution support for 50 additional publishers (items 51-100).
- **AIAA / INFORMS**: Expanded direct open-access resolution support for AIAA and INFORMS publications (supporting items 101-2000).

### 📚 Book & Large Document Sources
- **Library Genesis (LibGen)**: Queries Library Genesis mirrors to resolve and download textbook and monograph files.
- **Internet Archive**: Native book deobfuscator that downloads public-domain books page-by-page and compiles them into a single PDF.
- **OpenLibrary**: Provides structural metadata for book lookup and title-to-author matching.

---

## 🛠️ Installation & Setup

Since this application is built entirely using the Python standard library, there are **no external library dependencies** to install. Simply clone the repository and run:

```bash
# Clone the repository
git clone https://github.com/dzmarkets/Academic-Paper-Downloader.git

# Navigate into the project folder
cd Academic-Paper-Downloader

# Run the application
python paper.py
```

### Building the application and setup installer

1. **Compile with PyInstaller** (Directory-based compilation):
   ```bash
   python -m PyInstaller --noconfirm paper.spec
   ```
   This compiles the project into a folder-based distribution in `dist\paper\` (incorporating all Python binaries and `paper.exe`). This directory-based layout eliminates startup delays by avoiding runtime extraction.

2. **Compile the Installer with Inno Setup**:
   Open Inno Setup and compile `installer.iss`, or compile it via the command line:
   ```bash
   "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer.iss
   ```
   This generates the setup executable `AcademicPaperDownloader_Setup.exe` in the `Output\` folder.

All downloaded files are saved in subfolders under the user's `Documents\Academic Paper Downloader\` directory (e.g., `Papers\`, `Books\`, `Theses\`, `Others\`), keeping the installation directory clean.

---

## 🏗️ Technical Architecture

- **Thread-Safe Architecture**: All HTTP calls, scraping pipelines, and network requests are executed on background worker threads (`threading.Thread`) to ensure the desktop GUI remains perfectly responsive and never freezes.
- **Resilient Fallback Parsing**: When Python's native `urllib.request` triggers Cloudflare filters, the scraping engine spawns system `curl` subprocesses to guarantee a 100% profile lookup and thesis retrieval rate.
- **Deduplication Engine**: Combines OpenAlex JSON API entries and raw scraped HTML elements from ResearchGate in parallel, dynamically sorting and deduplicating records by title similarity.
- **Safe Windows Path Resolution**: Dynamically retrieves the user's standard Windows Documents folder using the Windows Shell API (`SHGetFolderPathW`), ensuring downloads are safely written to `Documents\Academic Paper Downloader\` rather than the temporary `_MEI...` extraction folder or protected system directories.

---

## 📋 Changelog

### v2.4.0.3
- Extended the tracked journal list by 1400 candidate journals (items 601-2000) resolved via the open-access pipeline and direct publisher heuristics.
- Bumped application version to `v2.4.0.3` in package, installers, configuration, and user-agent string.

### v2.4.0.2
- Added direct open-access resolvers for AIAA and INFORMS publications.
- Extended the tracked journal list by 500 candidate journals (items 101-600) resolved via standard pipeline and best-effort heuristics.
- Bumped application version to `v2.4.0.2` in package, installers, configuration, and user-agent string.

### v2.4.0.1
- Added direct open-access resolvers for 50 new publishers/journals (items 51-100) including De Gruyter, World Scientific, Mary Ann Liebert, Georg Thieme, ACM, CSIRO, American Physiological Society, American Society for Microbiology (ASM), and Edinburgh University Press.
- Added Palgrave Macmillan prefix to Springer template mappings.
- Bumped application version to `v2.4.0.1` in package, installers, configuration, and user-agent string.

### v2.4.0
- Added direct open-access resolvers for 25 new publishers/journals including Annual Reviews, APS, Chicago Press, Royal Society, ASCE, Emerald, SIAM, and Pleiades Publishing (via Springer).
- Grouped DOI prefix rules for MDPI, Frontiers, Nature, and PLOS to optimize mapping code.
- Bumped application version to `v2.4.0` in package, installers, configuration, and user-agent string.

### v2.3.9
- Replaced blocking direct downloads with 64KB chunk-based reads, checking the cancel state during download loops to allow immediate abortion of active downloads.
- Integrated early cancel hooks inside network request functions to prevent UI hangs.
- Redesigned Stop button styling, state-handling, and foreground text colors.

### v2.3.8
- Implemented non-academic search results filtering (ignoring software repository/documentation sites like GitHub, PyPI, Wikipedia, etc.).
- Fixed DuckDuckGo search result deduplication/filtering logic.

### v2.3.7
- Integrated 5 new direct open-access paper download resolvers: PLOS, BioRxiv, Zenodo, DOAJ, and Semantic Scholar.
- Implemented robust Cloudflare and WAF bypassing for JSON APIs by utilizing `fetch_html_resilient` to fallback to system `curl` on blocks.
- Synchronized GUI and CLI pipelines to run the new resolvers.
- Created an automated integration test suite (`test_resolvers.py`) to verify all download strategies against live repositories.
- Improved UX by automatically highlighting newly downloaded papers in Windows Explorer.

### v2.3.6
- Switched from single-file compilation (`--onefile`) to directory-based compilation (`--onedir`) and packaged it via Inno Setup. This removes the runtime self-extraction delay and makes the application start instantaneously (under 0.5s).

### v2.3.5
- Fixed subprocess argument escaping for setup installer launching by passing the execution command as a single string.

### v2.3.4
- Added `MZ` PE executable signature validation to the background update downloader to prevent corrupt downloads.
- Prioritized `_Setup.exe` files in the GitHub release checker asset loop.

### v2.3.3
- Configured professional setup installer using Inno Setup (supporting user-level installations without UAC admin prompts).
- Integrated premium inline auto-updater directly in the application header replacing popups, with real-time download progress.
- Implemented Windows mutex locks in Python to prevent active installer lock errors.
- Configured GitHub Actions CI/CD release workflow to build executables and compile installers automatically on version tag push.

### v2.3.2
- Integrated direct, clickable releases and updates gateway link directly in the app’s main header (`🌐 Get Latest Releases & Updates`).
- Configured dynamic hover states and mouse pointer hand cursors for the releases label.
- Refactored build procedures and deployed automatic asset replacement scripts to securely push compiled binaries to GitHub.

### v2.3.1
- Incremented version to `v2.3.1` for release testing.

### v2.3.0
- Integrated a **GitHub Update Checker** running silently on startup and manually via an interactive header icon (`🔄`) to notify users and provide an interactive dialog with release notes and a direct `.exe` download option if a newer update is available.
- Added a **🧹 Clear Results** button in the search pagination bar to instantly reset keyword results and restore default input states.
- Refactored header and title version outputs to dynamically load from the central `VERSION` constant.

### v2.2.0
- Fixed download output path when running as a PyInstaller `.exe` (files were incorrectly saved to `%TEMP%\_MEI...\`).
- Downloads are now organized into smart named subfolders (`Papers\`, `Books\`, `Theses\`, `Others\`) beside the executable.
- Added `Others\` as a fallback folder for any unrecognized document type.
- Added `VERSION` constant to source for release tracking.

---

## 👥 Credits

Developed by **Yazid YOUCEF**.  
Feel free to open an issue or pull request to contribute features!
