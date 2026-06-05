# 📚 Academic Paper Downloader

> **Version 2.3.6**

[![Download Setup Installer](https://img.shields.io/badge/Download-Setup%20Installer-8B5CF6?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/dzmarkets/Academic-Paper-Downloader/releases/download/v2.3.6/AcademicPaperDownloader_Setup.exe)

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
- **📂 Smart Download Folders** *(v2.2.0)*: Downloaded files are automatically organized into named subfolders beside the `.exe` / script:

  | Document Type | Folder |
  |---|---|
  | Academic Paper | `Papers\` |
  | Book | `Books\` |
  | Thesis | `Theses\` |
  | Other / Unknown | `Others\` |

  Folders are created automatically on first use if they do not already exist.

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

### Building a standalone executable

```bash
python -m PyInstaller --onefile --windowed --icon=app_icon.png paper.py
```

The compiled `.exe` will be placed in the `dist\` folder. All downloaded files will be saved in subfolders (`Papers\`, `Books\`, `Theses\`, `Others\`) **next to the `.exe`**, not in the system temp directory.

---

## 🏗️ Technical Architecture

- **Thread-Safe Architecture**: All HTTP calls, scraping pipelines, and network requests are executed on background worker threads (`threading.Thread`) to ensure the desktop GUI remains perfectly responsive and never freezes.
- **Resilient Fallback Parsing**: When Python's native `urllib.request` triggers Cloudflare filters, the scraping engine spawns system `curl` subprocesses to guarantee a 100% profile lookup and thesis retrieval rate.
- **Deduplication Engine**: Combines OpenAlex JSON API entries and raw scraped HTML elements from ResearchGate in parallel, dynamically sorting and deduplicating records by title similarity.
- **PyInstaller-Aware Path Resolution** *(v2.2.0)*: Detects whether the app is running as a frozen bundle (`sys.frozen`) and uses `sys.executable` to resolve the correct application directory, preventing files from being saved to the temporary `_MEI...` extraction folder.

---

## 📋 Changelog

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
