# Parallel "Race" Download Architecture

## Overview

Replace the sequential waterfall in `run_download_pipeline()` with a two-tier parallel race engine:
- **Tier 1 (Fast API race):** Lightweight sources launched in parallel simultaneously. First to return a valid PDF wins and cancels the rest.
- **Tier 2 (Heavy scrapers fallback):** Slow/subprocess-heavy engines (Sci-Hub, ResearchGate, LibGen) run only if Tier 1 completely fails. Still run in parallel among themselves with the same race logic.

This reduces average download time from **~30–90s** (worst case sequential) to **~3–10s** (fastest parallel winner).

---

## Architecture Diagram

```
Download Button Clicked
        │
        ▼
[Pre-flight: DOI Resolution, URL Registration]
        │
        ▼
┌──────────────── TIER 1: Fast API Race (parallel) ─────────────────┐
│  Unpaywall ──┐                                                      │
│  PLOS ───────┤                                                      │
│  BioRxiv ────┤── threading.Event ──► FIRST WINNER ──► cancel ──► ✅│
│  Semantic Scholar ──┤                                               │
│  arXiv ──────┤                                                      │
│  CORE ───────┤                                                      │
│  DOAJ ───────┤                                                      │
│  SSRN ───────┤                                                      │
│  Zenodo ─────┤                                                      │
│  Europe PMC ─┤                                                      │
│  Publisher Direct ─┤                                                │
│  ASTESJ ─────┘                                                      │
└────────────────────────────────────────────────────────────────────┘
        │ (all failed)
        ▼
┌──────────────── TIER 2: Heavy Scraper Race (parallel) ─────────────┐
│  Sci-Hub ────┐                                                       │
│  ResearchGate ── threading.Event ──► FIRST WINNER ──► cancel ──► ✅│
│  LibGen ─────┤                                                       │
│  Taylor & Francis ─┘                                                 │
└─────────────────────────────────────────────────────────────────────┘
        │ (all failed)
        ▼
[FAILED: show discovered_urls fallback links]
```

---

## Open Questions

> [!IMPORTANT]
> Before executing, please confirm the following design decisions:
>
> 1. **Max workers per tier**: Tier 1 has 12 sources. Running all 12 simultaneously may spike CPU/memory. Recommended: `max_workers=8` for Tier 1, `max_workers=4` for Tier 2. Should I cap this?
> 2. **Taylor & Francis placement**: It uses a DOI prefix check. Should it stay in Tier 2 (heavy) or be promoted to Tier 1 (it is HTTP-based, not subprocess-heavy)?
> 3. **Status label behavior during race**: Currently shows one source at a time. During parallel race, should the label show `"Searching all sources..."` (static), or cycle between active sources (animated)?
> 4. **`open_in_explorer` concurrency**: Currently called from `downloader.py` when a file saves. If two sources finish simultaneously, this could open the folder twice. Should I add a flag to only do it once?

---

## Proposed Changes

---

### Component 1: `src/core/state.py`

#### [MODIFY] state.py

Add a new `threading.Event` object for the race signal, and a lock to protect file writes.

```python
# Shared dynamic run-time state
import threading

abort_requested = False
discovered_urls = []
dl_link_lbl = None
GUI_MODE = False
status_label = None
first_run_changelog = None

# --- NEW: Parallel race state ---
download_success_event = threading.Event()   # Set by the first winning engine
download_write_lock    = threading.Lock()    # Prevents two threads from writing the same file
```

**Rationale:** `threading.Event` is thread-safe, supports `wait(timeout)`, and `is_set()` is O(1). The write lock prevents the rare case of two engines completing at the exact same millisecond.

---

### Component 2: `src/network/downloader.py`

#### [MODIFY] downloader.py

Modify `download_file()` to check `state.download_success_event` before saving and use `state.download_write_lock` around the file write.

**Key changes:**
1. Add early-exit at the top: if `state.download_success_event.is_set()`, return `False` immediately.
2. Wrap the final `open(filename, "wb")` block inside `with state.download_write_lock`.
3. Re-check `is_set()` inside the lock (double-checked locking) to handle the race-to-lock scenario.
4. After a successful write, call `state.download_success_event.set()`.

```python
# In download_file(), before saving (replacing line ~126):

# Parallel race guard: bail out if another engine already won
if state.download_success_event.is_set():
    print(f"[RACE] Another source already won. Discarding result.")
    return False

with state.download_write_lock:
    # Double-check inside the lock (handles simultaneous finishers)
    if state.download_success_event.is_set():
        return False
    # Write file
    with open(filename, "wb") as out_file:
        out_file.write(content)
    state.download_success_event.set()  # Signal: we won the race

print(f"[SUCCESS] Saved: '{os.path.basename(filename)}'")
if state.GUI_MODE:
    open_in_explorer(filename)
return True
```

---

### Component 3: `src/main.py`

#### [MODIFY] main.py

This is the **core change**. Introduce a private `_run_race()` helper and rewrite `run_download_pipeline()` to use the two-tier model.

**New `_run_race()` helper:**

```python
def _run_race(sources, update_status, label_text):
    """
    Run a list of (name, fn, *args) download sources in parallel.
    Returns True as soon as one callable returns True.

    Parameters
    ----------
    sources     : list of (name: str, fn: callable, *args)
    update_status : callable(text, fg)
    label_text  : str — status bar message shown during the race
    """
    if not sources:
        return False

    update_status(label_text)

    def _worker(name, fn, args):
        if state.abort_requested or state.download_success_event.is_set():
            return False
        print(f"[RACE] Starting: {name}")
        try:
            result = fn(*args)
        except Exception as e:
            print(f"[RACE] {name} raised: {e}")
            result = False
        if result:
            print(f"[RACE] Winner: {name}")
        return result

    max_workers = min(len(sources), 8)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(_worker, name, fn, args): name
            for name, fn, *args in sources
        }
        # Poll every 200ms for success or abort
        while not state.download_success_event.is_set() and not state.abort_requested:
            done, _ = concurrent.futures.wait(
                futures, timeout=0.2,
                return_when=concurrent.futures.ALL_COMPLETED
            )
            if len(done) == len(futures):
                break  # All done, none succeeded

    return state.download_success_event.is_set()
```

**New `run_download_pipeline()` structure:**

```python
def run_download_pipeline(target_doi, target_title, status_label=None, root_widget=None):
    def update_status(text, fg="#00ADB5"):
        if status_label and root_widget:
            root_widget.after(0, lambda: status_label.config(text=text, fg=fg))

    # Reset race state
    state.download_success_event.clear()

    if state.abort_requested:
        raise InterruptedError("Cancelled by user")

    # Pre-flight URL registration + book identifier shortcut (unchanged)
    ...

    # TIER 1 source list (built dynamically based on target_doi)
    tier1_sources = [...]

    success = _run_race(tier1_sources, update_status, "Searching all open sources...")
    if success:
        return True

    if state.abort_requested:
        raise InterruptedError("Cancelled by user")

    # TIER 2 source list
    tier2_sources = [
        ("Sci-Hub",      try_scihub,       target_doi),
        ("LibGen",       try_libgen,       target_doi, target_title),
        ("ResearchGate", try_researchgate, target_doi, target_title),
        ("Taylor & Francis", try_download_taylorfrancis, target_doi, target_title),
    ]

    success = _run_race(tier2_sources, update_status, "Bypassing paywalls...")
    if success:
        return True

    if state.abort_requested:
        raise InterruptedError("Cancelled by user")

    # Final fallback: book repositories
    update_status("Querying Book Repositories...")
    return try_download_book(target_doi, target_title,
                             status_label=status_label, root_widget=root_widget)
```

---

### Component 4: `src/gui/main_window.py`

#### [MODIFY] main_window.py

**Change 1 — Reset `download_success_event` on new download:**

In `start_individual_download()` (around line 809), add one line before calling `run_download_pipeline`:
```python
state.download_success_event.clear()
```

**Change 2 — Thread-safe `print` during race:**

The existing `RedirectText` stdout redirector already uses `root.after(0, ...)`. It correctly handles concurrent writes from multiple threads. ✅ **No change needed.**

**Change 3 — Status label during race:**

All existing `update_status()` calls already use `root.after(0, lambda: ...)`, which is thread-safe for Tkinter. ✅ **No change needed.**

---

### Component 5: `tests/test_parallel_race.py`

#### [NEW] test_parallel_race.py

New test file to validate the race mechanism in isolation with mocked engines:

```python
import time, threading
from unittest.mock import patch
from src.core import state
from src.main import _run_race

def test_fastest_wins():
    """The fastest source should win, and the event should be set."""
    state.download_success_event.clear()
    state.abort_requested = False

    def slow_source(doi, title):
        time.sleep(2.0)
        return True  # Too late, will be blocked by lock

    def fast_source(doi, title):
        time.sleep(0.3)
        return True  # Wins

    def medium_source(doi, title):
        time.sleep(1.0)
        return True  # Too late

    sources = [
        ("Slow",   slow_source,   "10.0/test", "Test Paper"),
        ("Fast",   fast_source,   "10.0/test", "Test Paper"),
        ("Medium", medium_source, "10.0/test", "Test Paper"),
    ]

    start = time.time()
    success = _run_race(sources, lambda t, fg=None: None, "Testing...")
    elapsed = time.time() - start

    assert success is True
    assert state.download_success_event.is_set()
    assert elapsed < 1.0, f"Race took too long: {elapsed:.2f}s"

def test_all_fail():
    """If all sources fail, the event should not be set."""
    state.download_success_event.clear()
    state.abort_requested = False

    sources = [
        ("Fail1", lambda doi, t: False, "10.0/test", "Test"),
        ("Fail2", lambda doi, t: False, "10.0/test", "Test"),
    ]

    success = _run_race(sources, lambda t, fg=None: None, "Testing...")
    assert success is False
    assert not state.download_success_event.is_set()

def test_abort_stops_race():
    """Setting abort_requested should stop the race cleanly."""
    state.download_success_event.clear()
    state.abort_requested = False

    def blocking_source(doi, title):
        time.sleep(5.0)
        return True

    sources = [("Blocking", blocking_source, "10.0/test", "Test")]

    # Set abort after 0.2s
    def abort_after_delay():
        time.sleep(0.2)
        state.abort_requested = True
    threading.Thread(target=abort_after_delay, daemon=True).start()

    start = time.time()
    _run_race(sources, lambda t, fg=None: None, "Testing...")
    elapsed = time.time() - start

    assert elapsed < 2.0, "Abort should have stopped the race quickly"
```

---

## Risk Assessment

| Risk | Likelihood | Mitigation |
|---|---|---|
| Two threads write the same file simultaneously | Low | `download_write_lock` + double-check inside lock |
| `open_in_explorer` called twice | Low | `download_success_event.set()` is called before `open_in_explorer`, so only the winner reaches it |
| Thread pool exhaustion (12+ workers) | Low | `max_workers = min(len(sources), 8)` cap enforced |
| Slow scraper blocking thread pool slots | Medium | Tier 2 isolation; heavy engines only start after Tier 1 fully finishes |
| `download_success_event` not reset between downloads | Medium | Explicitly cleared at the top of `run_download_pipeline()` and in `start_individual_download()` |
| GUI status label spam from multiple threads | Low | All status updates use `root.after(0, ...)` — already thread-safe |
| Existing `state.abort_requested` checks in engines | None | All engines already check this flag natively — they will self-terminate |

---

## Verification Plan

### Automated Tests
```powershell
python -m pytest tests/ -v
python -m pytest tests/test_parallel_race.py -v
```

### Manual Verification Steps
1. Run `python paper.py` and search for a paper with a DOI.
2. Click **Download** — status bar should show `"🔍 Searching all open sources..."`.
3. Verify download completes significantly faster than before.
4. Verify the log window shows: `[RACE] ✅ Winner: <source_name>`.
5. Click **Download** a second time — verify the race resets cleanly.
6. Click **Stop** mid-download — verify `abort_requested` stops all threads gracefully.

---

## Files Changed Summary

| File | Change | Scope |
|---|---|---|
| `src/core/state.py` | MODIFY | +2 lines: `download_success_event`, `download_write_lock` |
| `src/network/downloader.py` | MODIFY | ~10 lines: race guard + write lock around file save |
| `src/main.py` | MODIFY | Full rewrite of `run_download_pipeline()` + new `_run_race()` helper |
| `src/gui/main_window.py` | MODIFY | +1 line: `state.download_success_event.clear()` in `start_individual_download()` |
| `tests/test_parallel_race.py` | NEW | ~60 lines: 3 test cases for the race mechanism |
