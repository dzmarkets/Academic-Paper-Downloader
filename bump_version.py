import re

OLD = "2.4.0.3"
NEW = "2.4.0.9"

files = [
    "file_version_info.txt",
    "installer.iss",
    "resolve_journal_links.py",
    "Important.txt",
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
            print(f"Updated {fname}: {count} replacement(s)")
        else:
            print(f"No occurrences of {OLD!r} found in: {fname}")
    except FileNotFoundError:
        print(f"File not found: {fname}")

print("Done.")
