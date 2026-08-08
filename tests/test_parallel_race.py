"""
Unit tests for the parallel race download architecture.

These tests validate _run_race() in isolation using mock engines and no
real network calls.  They check three invariants:

1. The fastest source wins; the total elapsed time is bounded by the
   winner's sleep, not the sum of all sources' sleeps.
2. If all sources fail, download_success_event remains unset.
3. Setting abort_requested mid-race causes _run_race() to return quickly.
"""

import time
import threading

from src.core import state
from src.main import _run_race


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _noop_status(text, fg=None):  # noqa: D401
    """Dummy status-label callback used in all tests."""


def _reset():
    """Restore module-level race state before each test."""
    state.download_success_event.clear()
    state.abort_requested = False


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_fastest_wins():
    """The fastest source should win; elapsed time < 1 s despite a 2 s slow source."""
    _reset()

    def slow_source(doi, title):
        time.sleep(2.0)
        return True  # Too late — blocked by lock / event check

    def fast_source(doi, title):
        time.sleep(0.3)
        return True  # Wins the race

    def medium_source(doi, title):
        time.sleep(1.0)
        return True  # Too late

    sources = [
        ("Slow",   slow_source,   "10.0/test", "Test Paper"),
        ("Fast",   fast_source,   "10.0/test", "Test Paper"),
        ("Medium", medium_source, "10.0/test", "Test Paper"),
    ]

    start = time.time()
    success = _run_race(sources, _noop_status, "Testing...")
    elapsed = time.time() - start

    assert success is True, "Race should have returned True"
    assert state.download_success_event.is_set(), "Event should be set after a win"
    assert elapsed < 1.5, f"Race took too long: {elapsed:.2f}s (expected < 1.5 s)"


def test_all_fail():
    """If every source returns False, the event must not be set."""
    _reset()

    sources = [
        ("Fail1", lambda doi, t: False, "10.0/test", "Test"),
        ("Fail2", lambda doi, t: False, "10.0/test", "Test"),
        ("Fail3", lambda doi, t: False, "10.0/test", "Test"),
    ]

    success = _run_race(sources, _noop_status, "Testing...")

    assert success is False, "Race should return False when all sources fail"
    assert not state.download_success_event.is_set(), "Event must not be set when all fail"


def test_abort_stops_race():
    """Setting abort_requested while the race is running should exit quickly."""
    _reset()

    def blocking_source(doi, title):
        time.sleep(10.0)
        return True

    sources = [("Blocking", blocking_source, "10.0/test", "Test")]

    # Trigger abort after a short delay from a daemon thread
    def _abort_after():
        time.sleep(0.3)
        state.abort_requested = True

    threading.Thread(target=_abort_after, daemon=True).start()

    start = time.time()
    _run_race(sources, _noop_status, "Testing...")
    elapsed = time.time() - start

    assert elapsed < 2.0, f"Abort should have stopped the race in < 2 s, got {elapsed:.2f}s"


def test_empty_sources():
    """An empty source list should return False immediately without error."""
    _reset()

    success = _run_race([], _noop_status, "Testing...")

    assert success is False, "Empty source list should return False"
    assert not state.download_success_event.is_set()


def test_event_already_set_skips_all():
    """If download_success_event is pre-set, no worker should execute."""
    _reset()
    state.download_success_event.set()

    executed = []

    def tracking_source(doi, title):
        executed.append(True)
        return True

    sources = [("Tracker", tracking_source, "10.0/test", "Test")]
    success = _run_race(sources, _noop_status, "Testing...")

    # Workers check the event flag and exit early; none should have run
    assert success is True  # event is already set → _run_race returns True
    assert executed == [], "No worker should execute if event is pre-set"
