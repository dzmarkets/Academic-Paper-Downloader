# 📚 Academic Paper Downloader

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
- **📦 Zero Third-Party Dependencies**: Runs purely on the native Python standard library and Tkinter framework—no bulky package installations required!

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

---

## 🏗️ Technical Architecture

- **Thread-Safe Architecture**: All HTTP calls, scraping pipelines, and network requests are executed on background worker threads (`threading.Thread`) to ensure the desktop GUI remains perfectly responsive and never freezes.
- **Resilient Fallback Parsing**: When Python's native `urllib.request` triggers Cloudflare filters, the scraping engine spawns system `curl` subprocesses to guarantee a 100% profile lookup and thesis retrieval rate.
- **Deduplication Engine**: Combines OpenAlex JSON API entries and raw scraped HTML elements from ResearchGate in parallel, dynamically sorting and deduplicating records by title similarity.

---

## 👥 Credits

Developed by **Yazid YOUCEF**.  
Feel free to open an issue or pull request to contribute features!
