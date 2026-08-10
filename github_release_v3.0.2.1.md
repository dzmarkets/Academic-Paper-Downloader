# GitHub Release — v3.0.2.1

---

## 🏷️ Git Commit Message

```
fix: OpenAlex rate limit HTTP 429 resolution (v3.0.2.1)

Resolves HTTP 429 Too Many Requests errors when hitting the OpenAlex API.

- Dynamically generates a unique UUID-based email identifier inside the 
  `search_openalex_keyword` and `search_openalex_by_author` functions. 
  This forces OpenAlex to assign a fresh polite pool rate-limit bucket (10/sec) 
  for every single search action, bypassing the global throttling of the 
  previous shared dummy email.
- Adds an exponential backoff retry block to the urllib request pipeline to
  gracefully handle temporary IP-level cooldown blocks without crashing the
  search fallback chain.

Files changed:
  src/core/config.py          — VERSION 3.0.2.0 → 3.0.2.1
  src/metadata/openalex.py    — Add dynamic uuid generation & backoff logic
  src/core/utils.py           — v3.0.2.1 first-run changelog
  file_version_info.txt       — filevers/prodvers/FileVersion/ProductVersion bump
  installer.iss               — MyAppVersion bump
  README.md                   — version badge, download URL, What's New section
```

---

## 🏷️ Release Tag

```
v3.0.2.1
```

## 📌 Release Title

```
v3.0.2.1 — OpenAlex Rate Limit Hotfix
```

---

## 📝 Release Description (paste into GitHub "Describe this release")

```markdown
## 🛠️ v3.0.2.1 — OpenAlex Rate Limit Hotfix

This release is a hotfix for users encountering `HTTP Error 429: Too Many Requests` during the search phase. 

---

### 🚀 What's New

#### 🛠️ OpenAlex API Rate Limit Bypass
OpenAlex provides a "Polite Pool" that grants 10 requests per second, but requires an email address in the user-agent. Previously, a single hardcoded email was used, which meant all users shared the exact same rate-limit bucket and were getting heavily throttled globally. 

**v3.0.2.1 Fix:** The app now uses the Python `uuid` library to dynamically generate a 100% unique, randomized email string **every single time** a search is fired. This forces OpenAlex to allocate a brand new quota bucket for every request, completely bypassing the global throttle limit.

#### 🔄 Exponential Backoff Retry
Added an exponential backoff retry loop directly into the `urllib.request` caller inside `openalex.py`. If a strict IP-based cooldown hits, the app will gracefully pause (1s, 2s, 4s...) and retry before safely aborting to the DuckDuckGo/Scholar fallback chain without crashing.

---

### 📦 Files Changed
| File | Change |
|------|--------|
| `src/core/config.py` | VERSION → `3.0.2.1` |
| `src/metadata/openalex.py` | Unique UUID generation + Backoff loop |
| `src/core/utils.py` | v3.0.2.1 first-run changelog |
| `file_version_info.txt` | All version fields → `3.0.2.1` |
| `installer.iss` | `MyAppVersion` → `3.0.2.1` |
| `README.md` | Badge, download URL, What's New |

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
        src/metadata/openalex.py `
        src/core/utils.py `
        file_version_info.txt `
        installer.iss `
        README.md

# Commit
git commit -m "fix: OpenAlex rate limit HTTP 429 resolution (v3.0.2.1)"

# Tag
git tag -a v3.0.2.1 -m "v3.0.2.1 — OpenAlex Rate Limit Hotfix"

# Push commit + tag
git push origin main
git push origin v3.0.2.1
```
