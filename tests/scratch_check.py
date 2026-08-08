import urllib.request
import urllib.parse
import json

title = "Particle swarm optimization with adaptive mutation for multimodal optimization"
url = f"https://api.crossref.org/works?query.title={urllib.parse.quote(title)}&rows=5"
headers = {'User-Agent': 'PaperDownloader/3.0 (mailto:test@example.com)'}

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode())

items = data['message']['items']
print(f"Items found: {len(items)}")
for it in items:
    print("Title:", it.get('title'))
    print("DOI:", it.get('DOI'))
    print("Published:", it.get('published-print') or it.get('published-online'))
