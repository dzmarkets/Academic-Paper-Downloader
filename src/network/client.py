import urllib.request
import urllib.parse
import urllib.error
import json
import os
from src.core.config import HEADERS
from src.core import state

# Set up a cookie processor to maintain sessions across redirects (crucial for ResearchGate)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
opener.addheaders = [(k, v) for k, v in HEADERS.items()]
urllib.request.install_opener(opener)

def get_user_country():
    """Detect the user's country via IP geolocation (ipapi.co). Returns ISO 3166-1 alpha-2 code."""
    try:
        req = urllib.request.Request('https://ipapi.co/json/', headers=HEADERS)
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = json.loads(resp.read().decode())
        return data.get('country_code', '').upper()
    except Exception:
        pass
    # Fallback: ip-api.com
    try:
        req = urllib.request.Request('http://ip-api.com/json/?fields=countryCode', headers=HEADERS)
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = json.loads(resp.read().decode())
        return data.get('countryCode', '').upper()
    except Exception:
        return ''


def fetch_html_resilient(url):
    """Fetch HTML content from a URL using urllib first, falling back to native system curl on block/failure."""
    if state.abort_requested:
        return ""
    try:
        if state.abort_requested:
            return ""
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=12) as response:
            if state.abort_requested:
                return ""
            return response.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"[WARNING] urllib fetch failed: {e}. Trying native system curl fallback...")
        try:
            import subprocess
            cmd = ["curl", "-s", "-L", "-H", f"User-Agent: {HEADERS['User-Agent']}", "-H", f"Accept: {HEADERS['Accept']}", url]
            extra_kwargs = {'creationflags': 0x08000000} if os.name == 'nt' else {}
            res = subprocess.run(cmd, capture_output=True, **extra_kwargs)
            if res.returncode == 0:
                return res.stdout.decode('utf-8', errors='ignore')
            else:
                print(f"[WARNING] curl returned error code: {res.returncode}")
        except Exception as curl_err:
            print(f"[ERROR] Native curl fallback failed: {curl_err}")
    return ""
