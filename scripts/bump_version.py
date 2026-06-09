import os
import re

OLD = "2.4.1.0"
NEW = "3.0.0.0"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))

files = [
    os.path.join(ROOT_DIR, "file_version_info.txt"),
    os.path.join(ROOT_DIR, "installer.iss"),
    os.path.join(SCRIPT_DIR, "resolve_journal_links.py"),
    os.path.join(ROOT_DIR, "docs", "Important.txt"),
    os.path.join(ROOT_DIR, "src", "core", "config.py"),
]

for fname in files:
    try:
        with open(fname, "r", encoding="utf-8") as f:
            content = f.read()
        updated = content.replace(OLD, NEW)
        if updated != content:
            with open(fname, "w", encoding="utf-8") as f:
                f.write(updated)
            count = content.count(OLD)
            print(f"Updated {os.path.basename(fname)}: {count} replacement(s)")
        else:
            print(f"No occurrences of {OLD!r} found in: {os.path.basename(fname)}")
    except FileNotFoundError:
        print(f"File not found: {fname}")

print("Done.")
