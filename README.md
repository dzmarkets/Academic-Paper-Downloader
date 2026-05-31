# 📚 Academic Paper Downloader

> **Version 2.3.0**

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
- **📖 Beautiful In-App Help & About Documentation**: Standard top menu bar offering dedicated styled popups explaining direct download inputs, search mechanics, and smart folder structures.
- **🚀 Background Update Checker**: Detects new software releases directly from the GitHub repository, displays dynamic changelogs, and offers secure, one-click `.exe` download triggers.
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

### v2.3.0
- Added **Help dropdown menu** with detailed **How to Use** and **About** dialogs matching the premium dark theme.
- Integrated a **GitHub Update Checker** running silently on startup (and manually from Help) to notify users if a newer `.exe` release is available on GitHub.
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
