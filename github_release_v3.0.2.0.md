# GitHub Release — v3.0.2.0

---

## 🏷️ Git Commit Message

```
feat: parallel race download engine (v3.0.2.0)

Replace sequential waterfall pipeline with a two-tier parallel race
architecture that cuts average download time from ~30-90 s to ~3-10 s.

Tier 1 — Fast API Race (12 sources launch simultaneously):
  Unpaywall, Semantic Scholar, arXiv, CORE, DOAJ, SSRN, Europe PMC,
  Zenodo, ASTESJ, Publisher Direct, PLOS, BioRxiv (+ T&F for known prefixes).
  First source to return a valid PDF wins; thread pool is cancelled immediately.

Tier 2 — Heavy Scraper Race (run only if Tier 1 fails):
  Sci-Hub, LibGen, ResearchGate, Taylor & Francis run in parallel with
  the same race-and-cancel logic.

Thread safety:
  - download_success_event (threading.Event): set by the first winner,
    checked by every engine before touching disk.
  - download_write_lock (threading.Lock): double-checked locking around
    the final open(filename, "wb") call prevents two engines from writing
    the same file simultaneously.

Abort improvement:
  - executor.shutdown(wait=False, cancel_futures=True) makes Stop respond
    instantly instead of waiting for slow threads to finish.

Tests:
  - New tests/test_parallel_race.py (5 tests, all passing in 1.3 s).

Files changed:
  src/core/config.py          — VERSION 3.0.1.0 → 3.0.2.0
  src/core/state.py           — add download_success_event, download_write_lock
  src/core/utils.py           — v3.0.2.0 first-run changelog
  src/network/downloader.py   — race guard + write lock around file save
  src/main.py                 — _run_race() helper + two-tier pipeline rewrite
  src/gui/main_window.py      — clear event on new download in run_pipeline_bg()
  file_version_info.txt       — filevers/prodvers/FileVersion/ProductVersion bump
  installer.iss               — MyAppVersion bump
  README.md                   — version badge, download URL, What's New section
  tests/test_parallel_race.py — NEW: 5 unit tests for the race mechanism
```

---

## 🏷️ Release Tag

```
v3.0.2.0
```

## 📌 Release Title

```
v3.0.2.0 — Parallel Race Download Engine
```

---

## 📝 Release Description (paste into GitHub "Describe this release")

```markdown
## ⚡ v3.0.2.0 — Parallel Race Download Engine

This release replaces the sequential source-by-source waterfall with a
**two-tier parallel race architecture** that dramatically cuts download wait
times.

---

### 🚀 What's New

#### ⚡ Parallel Race Download Engine
All 12 lightweight open-access sources now launch **simultaneously** in a
thread pool. The very first source that returns a valid PDF wins the race;
the remaining threads are cancelled immediately.

| Tier | Sources | Trigger |
|------|---------|---------|
| **Tier 1 — Fast APIs** | Unpaywall · Semantic Scholar · arXiv · CORE · DOAJ · SSRN · Europe PMC · Zenodo · ASTESJ · Publisher Direct · PLOS · BioRxiv (+ Taylor & Francis for matching DOI prefixes) | Always |
| **Tier 2 — Heavy Scrapers** | Sci-Hub · LibGen · ResearchGate · Taylor & Francis | Only if Tier 1 fully fails |

> **Result:** Average download time drops from **~30–90 s** (worst-case
> sequential) to **~3–10 s** (parallel winner).

---

#### 🔒 Thread-Safe File Writes
- `threading.Event` (`download_success_event`) — set by the first winning
  engine, checked by every other engine before it attempts to save a file.
- `threading.Lock` (`download_write_lock`) with **double-checked locking** —
  guarantees exactly one engine writes the PDF to disk even if two sources
  complete at the exact same millisecond.

---

#### 🛑 Instant Stop / Abort
Clicking **Stop** now calls `executor.shutdown(wait=False, cancel_futures=True)`
so the application responds immediately rather than waiting for slow HTTP
threads to time out naturally.

---

#### 🧪 New Unit Tests
`tests/test_parallel_race.py` — 5 isolated tests covering:
- Fastest source wins within time bound
- All-fail path leaves event unset
- Abort stops the race within 2 s
- Empty source list returns False safely
- Pre-set event skips all workers

---

### 📦 Files Changed
| File | Change |
|------|--------|
| `src/core/config.py` | VERSION → `3.0.2.0` |
| `src/core/state.py` | `+download_success_event`, `+download_write_lock` |
| `src/core/utils.py` | v3.0.2.0 first-run changelog |
| `src/network/downloader.py` | Race guard + write lock around file save |
| `src/main.py` | `_run_race()` helper + two-tier pipeline rewrite |
| `src/gui/main_window.py` | Reset event on every new download |
| `file_version_info.txt` | All version fields → `3.0.2.0` |
| `installer.iss` | `MyAppVersion` → `3.0.2.0` |
| `README.md` | Badge, download URL, What's New |
| `tests/test_parallel_race.py` | **NEW** — 5 race unit tests |

---

### 📥 Download

| Asset | Description |
|-------|-------------|
| **`AcademicPaperDownloader_Setup.exe`** | Windows installer (Inno Setup, no dependencies) |
| **Source code (zip / tar.gz)** | Full Python source |
```

---

## 🔖 Git Commands to Tag & Push

```powershell
# Stage all changed files
git add src/core/config.py `
        src/core/state.py `
        src/core/utils.py `
        src/network/downloader.py `
        src/main.py `
        src/gui/main_window.py `
        file_version_info.txt `
        installer.iss `
        README.md `
        tests/test_parallel_race.py

# Commit
git commit -m "feat: parallel race download engine (v3.0.2.0)"

# Tag
git tag -a v3.0.2.0 -m "v3.0.2.0 — Parallel Race Download Engine"

# Push commit + tag
git push origin main
git push origin v3.0.2.0
```
