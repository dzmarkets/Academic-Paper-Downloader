"""
verify_journal_links.py
-----------------------
Tests homepage_url availability for journals tracked in items 2001-10000
of journal_integration_status.md.

For each journal:
  1. Looks up its ISSN in resolved_journal_links.json
  2. Tests the homepage_url with a HEAD request (timeout=8s)
  3. Categorises as: WORKING / REDIRECT / BROKEN / NO_URL
  4. Saves results to journal_link_verification.csv
"""

import json
import re
import csv
import urllib.request
import urllib.error
import time
import os

# ── Config ──────────────────────────────────────────────────────────────────
START_ITEM  = 2001
END_ITEM    = 10000
TIMEOUT     = 8        # seconds per request
DELAY       = 0.15     # polite delay between requests (seconds)
# ─────────────────────────────────────────────────────────────────────────────

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0 Safari/537.36"
    )
}

def check_url(url):
    """Return (status_code, final_url) or ('ERROR', reason)."""
    try:
        req = urllib.request.Request(url, headers=HEADERS, method="HEAD")
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.status, resp.url
    except urllib.error.HTTPError as e:
        return e.code, url
    except urllib.error.URLError as e:
        return "ERROR", str(e.reason)
    except Exception as e:
        return "ERROR", str(e)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.abspath(os.path.join(script_dir, "..", "data"))
    docs_dir = os.path.abspath(os.path.join(script_dir, "..", "docs"))
    
    resolved_path = os.path.join(data_dir, "resolved_journal_links.json")
    status_path = os.path.join(docs_dir, "journal_integration_status.md")
    output_csv = os.path.join(docs_dir, "journal_link_verification.csv")
    
    print("Loading data files...")
    with open(resolved_path, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    with open(status_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Parse tracking rows within the desired item range
    rows = []
    for line in md_content.split("\n"):
        m = re.match(r"^\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*(\S+)\s*\(ISSN\)", line)
        if m:
            item_num = int(m.group(1))
            if START_ITEM <= item_num <= END_ITEM:
                issn = m.group(3).strip()
                label = m.group(2).strip()
                rows.append((item_num, issn, label))

    print(f"Found {len(rows)} entries to test (items {START_ITEM}-{END_ITEM})")

    results = []
    working = 0
    broken  = 0
    no_url  = 0

    for i, (item_num, issn, label) in enumerate(rows, 1):
        info     = json_data.get(issn) or {}
        url      = (info.get("homepage_url") or "").strip()
        publisher = (info.get("publisher") or "Unknown")

        if not url:
            status, final_url = "NO_URL", ""
            category = "NO_URL"
            no_url += 1
        else:
            status, final_url = check_url(url)
            if isinstance(status, int):
                if status < 400:
                    category = "WORKING"
                    working += 1
                elif status in (301, 302, 303, 307, 308):
                    category = "REDIRECT"
                    working += 1
                else:
                    category = f"BROKEN_{status}"
                    broken += 1
            else:
                category = "BROKEN_NET"
                broken += 1
            time.sleep(DELAY)

        results.append({
            "item":      item_num,
            "issn":      issn,
            "label":     label[:80],
            "publisher": publisher[:60],
            "homepage_url": url,
            "http_status": status,
            "final_url": final_url,
            "category":  category,
        })

        if i % 200 == 0 or i == len(rows):
            pct = i / len(rows) * 100
            print(f"  [{i}/{len(rows)} {pct:.0f}%] working={working} broken={broken} no_url={no_url}")

    # Write CSV
    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print(f"\n{'='*60}")
    print(f"Results saved to: {output_csv}")
    print(f"Total tested:  {len(results)}")
    print(f"WORKING:       {working} ({working/len(results)*100:.1f}%)")
    print(f"BROKEN/ERROR:  {broken} ({broken/len(results)*100:.1f}%)")
    print(f"NO URL:        {no_url} ({no_url/len(results)*100:.1f}%)")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
