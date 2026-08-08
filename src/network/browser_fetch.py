"""
browser_fetch.py — Tier 3 headless browser fallback for Sci-Hub verification.

Uses undetected-chromedriver to open a real Chrome instance that can
automatically pass Cloudflare Turnstile and other JS-rendered challenges.
Silently skipped if Chrome or undetected-chromedriver is not available.
"""

import time
import re

def _ensure_uc():
    """Lazily import undetected-chromedriver, installing it if missing."""
    try:
        import undetected_chromedriver as uc
        return uc
    except ImportError:
        try:
            import subprocess, sys
            print("[TIER 3] Installing undetected-chromedriver...")
            extra = {"creationflags": 0x08000000} if __import__("os").name == "nt" else {}
            subprocess.run(
                [sys.executable, "-m", "pip", "install", "undetected-chromedriver", "-q"],
                check=True, capture_output=True, **extra
            )
            import undetected_chromedriver as uc
            return uc
        except Exception as e:
            print(f"[TIER 3] Cannot install undetected-chromedriver: {e}")
            return None


def _patch_uc_rename():
    """
    Monkey-patch undetected_chromedriver's patcher module so it uses
    os.replace() instead of os.rename() when installing the chromedriver exe.

    On Windows, os.rename() raises WinError 183 if the destination already
    exists (left over from a previous unclean exit).  os.replace() overwrites
    atomically and never raises that error.

    This patch is idempotent — safe to call multiple times.
    """
    import os
    if os.name != "nt":
        return  # Only needed on Windows
    try:
        import undetected_chromedriver.patcher as _uc_patcher
        if not getattr(_uc_patcher, "_rename_patched", False):
            _uc_patcher.os.rename = _uc_patcher.os.replace
            _uc_patcher._rename_patched = True
    except Exception:
        pass  # UC not installed yet — _ensure_uc() will handle it



def fetch_html_headless(url, wait_seconds=20):
    """
    Open `url` in an undetected headless Chrome, automatically solve the
    Sci-Hub ALTCHA "Are you a robot?" challenge if present, then return
    the real paper page HTML.

    Challenge flow (observed via browser inspection):
      1. Page loads with "Are you a robot?" + a circular "No" button (div.answer)
      2. Clicking "No" triggers JavaScript ALTCHA proof-of-work (~5-8 seconds)
      3. Page auto-redirects to the real paper page containing the PDF link

    Returns
    -------
    str or None
        Real paper page HTML if successful, None on any failure.
    """
    uc = _ensure_uc()
    if uc is None:
        return None
    _patch_uc_rename()  # Fix WinError 183 on Windows before any uc.Chrome() call

    driver = None
    try:
        print(f"[TIER 3] Launching headless Chrome for: {url}")
        options = uc.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1280,900")
        options.add_argument("--disable-blink-features=AutomationControlled")

        driver = uc.Chrome(options=options, use_subprocess=True, version_main=150)
        driver.get(url)

        # Give the page time to fully render (JS challenge script loads async)
        time.sleep(3)

        # --- Auto-solve ALTCHA "Are you a robot?" challenge ---
        # Sci-Hub shows a page with a single <div class='answer'>No</div> button.
        # Clicking it triggers the background PoW computation which auto-resolves.
        page_src = driver.page_source
        if "are you" in page_src.lower() and "robot" in page_src.lower():
            print("[TIER 3] ALTCHA challenge detected — clicking 'No' button...")
            try:
                from selenium.webdriver.common.by import By
                from selenium.webdriver.support.ui import WebDriverWait
                from selenium.webdriver.support import expected_conditions as EC

                # Wait for the answer div to be present in the DOM
                answer_div = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.answer"))
                )
                
                # Execute JS click - more reliable in headless mode than standard click
                driver.execute_script("arguments[0].click();", answer_div)
                print("[TIER 3] Clicked 'No' (via JS) — waiting for PoW to complete...")

                # Wait for the real paper page: presence of .pdf or embed/iframe
                deadline = time.time() + wait_seconds
                while time.time() < deadline:
                    time.sleep(2)
                    page_src = driver.page_source
                    if re.search(r'\.pdf', page_src, re.IGNORECASE):
                        print("[TIER 3] PoW resolved — paper page loaded.")
                        break
                    if "embed" in page_src.lower() or "iframe" in page_src.lower():
                        print("[TIER 3] PoW resolved — embed/iframe detected.")
                        break
                    if "are you" not in page_src.lower():
                        # Challenge page gone, something loaded
                        break

            except Exception as click_err:
                print(f"[TIER 3] Could not click 'No' button: {click_err}")
        else:
            # No challenge — just wait for content
            deadline = time.time() + wait_seconds
            while time.time() < deadline:
                time.sleep(1.5)
                page_src = driver.page_source
                if re.search(r'\.pdf', page_src, re.IGNORECASE):
                    break
                if "sci-hub" in page_src.lower() and "embed" in page_src.lower():
                    break

        html = driver.page_source
        print(f"[TIER 3] Headless fetch complete — {len(html)} chars")
        return html

    except Exception as e:
        print(f"[TIER 3] Headless Chrome error: {e}")
        return None
    finally:
        if driver:
            try:
                driver.quit()
            except Exception:
                pass



def fetch_pdf_headless(doi_url, save_path, wait_seconds=15):
    """
    Navigate to a Sci-Hub page via headless Chrome and attempt to download
    the PDF using the browser's built-in download capability.

    Returns True if `save_path` was created and is a valid PDF.
    """
    import os
    uc = _ensure_uc()
    if uc is None:
        return False
    _patch_uc_rename()  # Fix WinError 183 on Windows before any uc.Chrome() call

    driver = None
    try:
        download_dir = os.path.dirname(os.path.abspath(save_path))
        os.makedirs(download_dir, exist_ok=True)

        options = uc.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1280,900")
        prefs = {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "plugins.always_open_pdf_externally": True,
        }
        options.add_experimental_option("prefs", prefs)

        driver = uc.Chrome(options=options, use_subprocess=True, version_main=150)
        driver.get(doi_url)

        # Wait for challenge + page load
        time.sleep(wait_seconds)

        # Check if file was downloaded
        for fname in os.listdir(download_dir):
            if fname.lower().endswith(".pdf"):
                downloaded = os.path.join(download_dir, fname)
                with open(downloaded, "rb") as f:
                    header = f.read(4)
                if header == b"%PDF":
                    if downloaded != save_path:
                        os.rename(downloaded, save_path)
                    print(f"[TIER 3] PDF downloaded via headless browser: {save_path}")
                    return True

        return False

    except Exception as e:
        print(f"[TIER 3] Headless PDF download error: {e}")
        return False
    finally:
        if driver:
            try:
                driver.quit()
            except Exception:
                pass
