import os
import re
import json
import time
import threading
import urllib.parse
import urllib.request
from src.core import state
from src.core.config import HEADERS
from src.core.utils import clean_filename, get_download_dir, get_app_dir, open_in_explorer, register_discovered_url
from src.network.downloader import download_file

def get_jpeg_size(filepath):
    """Parse JPEG SOF0-SOF3 markers to extract width and height in pure Python."""
    try:
        with open(filepath, 'rb') as f:
            data = f.read(4096)  # Read first 4KB
            if len(data) < 4 or data[0:2] != b'\xFF\xD8':
                return 800, 1000  # Default fallback if not valid JPEG
            
            i = 2
            while i < len(data) - 8:
                if data[i] == 0xFF:
                    marker = data[i+1]
                    if marker == 0xD9:  # EOI
                        break
                    is_sof = (0xC0 <= marker <= 0xC3) or (0xC5 <= marker <= 0xCB) or (0xCD <= marker <= 0xCF)
                    if is_sof and marker != 0xC4:
                        # SOF block layout: sample precision, height, width
                        height = int.from_bytes(data[i+5:i+7], byteorder='big')
                        width = int.from_bytes(data[i+7:i+9], byteorder='big')
                        if width > 0 and height > 0:
                            return width, height
                        break
                    else:
                        block_len = int.from_bytes(data[i+2:i+4], byteorder='big')
                        i += 2 + block_len
                else:
                    i += 1
    except Exception:
        pass
    return 800, 1000  # Default fallback


def compile_jpegs_to_pdf(jpeg_paths, pdf_path):
    """Compile JPEG images into a single PDF file using pure Python."""
    print(f"[INFO] Stitching {len(jpeg_paths)} page images into a single PDF...")
    
    offsets = {}
    out = bytearray()
    
    def write_line(line_bytes):
        out.extend(line_bytes + b'\n')
        
    write_line(b"%PDF-1.4")
    write_line(b"%\xFF\xFF\xFF\xFF")  # Binary marker
    
    num_pages = len(jpeg_paths)
    
    # 1. Catalog
    offsets[1] = len(out)
    write_line(b"1 0 obj")
    write_line(b"<< /Type /Catalog /Pages 2 0 R >>")
    write_line(b"endobj")
    
    # 2. Pages Parent
    kids_refs = [f"{3*p + 3} 0 R" for p in range(num_pages)]
    kids_str = " ".join(kids_refs)
    
    offsets[2] = len(out)
    write_line(b"2 0 obj")
    write_line(b"<< /Type /Pages /Kids [" + kids_str.encode() + b"] /Count " + str(num_pages).encode() + b" >>")
    write_line(b"endobj")
    
    # Write Page, Content, and Image stream objects
    for p, jpeg_path in enumerate(jpeg_paths):
        page_obj_id = 3 * p + 3
        content_obj_id = 3 * p + 4
        image_obj_id = 3 * p + 5
        
        width, height = get_jpeg_size(jpeg_path)
        
        # A. Page Object
        offsets[page_obj_id] = len(out)
        write_line(f"{page_obj_id} 0 obj".encode())
        write_line(f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {width} {height}] /Contents {content_obj_id} 0 R /Resources << /XObject << /Im0 {image_obj_id} 0 R >> >> >>".encode())
        write_line(b"endobj")
        
        # B. Content Stream Object (drawing the XObject at full size)
        content_stream = f"q\n{width} 0 0 {height} 0 0 cm\n/Im0 Do\nQ\n".encode()
        offsets[content_obj_id] = len(out)
        write_line(f"{content_obj_id} 0 obj".encode())
        write_line(f"<< /Length {len(content_stream)} >>".encode())
        write_line(b"stream")
        write_line(content_stream)
        write_line(b"endstream")
        write_line(b"endobj")
        
        # C. Image Object
        try:
            with open(jpeg_path, 'rb') as img_f:
                img_data = img_f.read()
        except Exception as err:
            img_data = b""
            print(f"[WARNING] Failed to read {jpeg_path}: {err}")
            
        offsets[image_obj_id] = len(out)
        write_line(f"{image_obj_id} 0 obj".encode())
        write_line(f"<< /Type /XObject /Subtype /Image /Width {width} /Height {height} /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length {len(img_data)} >>".encode())
        write_line(b"stream")
        out.extend(img_data)
        out.extend(b'\n')
        write_line(b"endstream")
        write_line(b"endobj")
        
    # Write xref table
    xref_offset = len(out)
    write_line(b"xref")
    total_objects = 3 * num_pages + 3
    write_line(f"0 {total_objects}".encode())
    write_line(b"0000000000 65535 f ")
    
    for obj_id in range(1, total_objects):
        offset = offsets.get(obj_id, 0)
        write_line(f"{offset:010d} 00000 n ".encode())
        
    # Write trailer
    write_line(b"trailer")
    write_line(f"<< /Size {total_objects} /Root 1 0 R >>".encode())
    write_line(b"startxref")
    write_line(str(xref_offset).encode())
    write_line(b"%%EOF")
    
    # Save PDF
    with open(pdf_path, 'wb') as pdf_f:
        pdf_f.write(out)
    print(f"[SUCCESS] Compiled PDF saved inside Downloads: '{os.path.basename(pdf_path)}'")


def get_book_pages_count(ia_id):
    """Retrieve total page count from Internet Archive metadata API."""
    url = f"https://archive.org/metadata/{ia_id}"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
        meta = data.get('metadata', {})
        count = meta.get('imagecount') or meta.get('item_pages') or meta.get('pages')
        if count:
            return int(count)
    except Exception as e:
        print(f"[WARNING] Could not resolve page count via metadata: {e}")
    return 350  # Dynamic default fallback


def deobfuscate_image(image_data, link, obf_header):
    """Decrypts the first 1024 bytes of image_data using AES-CTR and pycryptodome."""
    try:
        from Crypto.Cipher import AES
        from Crypto.Util import Counter
        import hashlib
        import base64
        import re
        
        version, counter_b64 = obf_header.split('|')
        if version != '1':
            raise ValueError("Unsupported obfuscation version: " + version)
            
        # Derive AES key: replace protocol/host in link with '/'
        aesKey = re.sub(r"^https?:\/\/.*?\/", "/", link)
        sha1_digest = hashlib.sha1(aesKey.encode('utf-8')).digest()
        key = sha1_digest[:16]
        
        # Decode the counter (should be 16 bytes)
        counter_bytes = base64.b64decode(counter_b64)
        if len(counter_bytes) != 16:
            raise ValueError(f"Expected counter to be 16 bytes, got {len(counter_bytes)}")
            
        prefix = counter_bytes[:8]
        initial_value = int.from_bytes(counter_bytes[8:], byteorder='big')
        
        # Create AES-CTR cipher with a 64-bit counter length
        ctr = Counter.new(64, prefix=prefix, initial_value=initial_value, little_endian=False)
        cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
        
        decrypted_part = cipher.decrypt(image_data[:1024])
        return decrypted_part + image_data[1024:]
    except Exception as e:
        print(f"[WARNING] Deobfuscation error: {e}")
        return image_data


def try_download_ia_pages(ia_id, pdf_path, title, status_label=None, root_widget=None):
    """Interactively prompts for authentication cookie, calls grant_access to searchInside.php,
    fetches high-resolution page URIs from BookReaderJSIA.php, downloads concurrently,
    deobfuscates pages, and compiles them into a single PDF using pure Python."""
    
    print("\n--- [BOOK PAGE COMPILER STRATEGY] Querying page count and CDL status ---")
    
    # 1. Prompt for Cookie securely on the main thread
    cookie = None
    if root_widget:
        cookie_res = []
        evt = threading.Event()
        
        def prompt():
            try:
                import tkinter.simpledialog
                val = tkinter.simpledialog.askstring(
                    "Archive.org Authentication Required",
                    f"This book ('{title if title else ia_id}') is locked under Controlled Digital Lending.\n\n"
                    "To download it page-by-page as a compiled PDF, please:\n"
                    "1. Log in and Borrow this book in your web browser.\n"
                    "2. Open DevTools (F12) -> Network -> Copy any request's 'Cookie' header.\n"
                    "3. Paste your Archive.org Cookie below:\n\n"
                    "Leave blank or click Cancel to skip and fallback to browser viewing.",
                    parent=root_widget
                )
                cookie_res.append(val)
            except Exception as err:
                print(f"[WARNING] Main thread dialog failed: {err}")
            finally:
                evt.set()
                
        root_widget.after(0, prompt)
        evt.wait()
        cookie = cookie_res[0] if cookie_res else None
        
    if not cookie:
        print("[INFO] No cookie credentials provided. Skipping CDL image compilation.")
        return False
        
    # 2. Establish requests Session and populate cookies
    import requests
    session = requests.Session()
    # Parse cookie string and set in session
    for part in cookie.split(";"):
        part = part.strip()
        if not part:
            continue
        if "=" in part:
            c_name, c_val = part.split("=", 1)
            session.cookies.set(c_name, c_val, domain=".archive.org")
            
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    })
    
    # 3. Perform grant_access handshake against searchInside.php
    print("[INFO] Performing grant_access handshake against searchInside.php...")
    if status_label:
        status_label.config(text="Performing access handshake...", fg="#00ADB5")
    try:
        handshake_url = "https://archive.org/services/loans/loan/searchInside.php"
        data = {
            "action": "grant_access",
            "identifier": ia_id
        }
        resp = session.post(handshake_url, data=data, timeout=15)
        if resp.status_code == 200:
            print("[SUCCESS] grant_access handshake succeeded.")
        else:
            print(f"[WARNING] Handshake returned status {resp.status_code}.")
    except Exception as e:
        print(f"[WARNING] Handshake failed: {e}")
        
    # 4. Fetch the details page to locate the BookReaderJSIA.php URL
    print("[INFO] Resolving BookReaderJSIA metadata URL...")
    if status_label:
        status_label.config(text="Resolving book metadata...", fg="#00ADB5")
    jsia_url = None
    try:
        details_url = f"https://archive.org/details/{ia_id}"
        resp_details = session.get(details_url, timeout=20)
        html = resp_details.text
        if '"url":"' in html:
            raw_jsia = html.split('"url":"')[1].split('"')[0]
            jsia_url = "https:" + raw_jsia.replace("\\u0026", "&").replace("\\/", "/")
            # Force JSON format instead of JSONP for clean parsing
            jsia_url = jsia_url.replace("format=jsonp", "format=json")
            print(f"[INFO] Discovered metadata URL: {jsia_url}")
    except Exception as e:
        print(f"[WARNING] Failed to extract BookReaderJSIA URL: {e}")
        
    if not jsia_url:
        print("[ERROR] Could not resolve BookReaderJSIA metadata page. Skipping.")
        return False
        
    # 5. Fetch and parse pages from JSIA JSON
    print("[INFO] Fetching page lists from BookReader...")
    try:
        resp_jsia = session.get(jsia_url, timeout=20)
        jsia_data = resp_jsia.json()
        br_options = jsia_data.get("data", {}).get("brOptions", {})
        pages_list = br_options.get("data", [])
        
        flat_links = []
        for item in pages_list:
            for page in item:
                flat_links.append(page.get("uri"))
    except Exception as e:
        print(f"[ERROR] Failed to fetch or parse book pages JSON: {e}")
        return False
        
    if not flat_links:
        print("[ERROR] Resolved page link list is empty.")
        return False
        
    # Check if we got restricted preview links or direct images
    is_preview = any("BookReaderPreview.php" in l for l in flat_links)
    if is_preview:
        print("\n==============================================")
        print("[WARNING] The server served restricted preview image links.")
        print("[TIP] You must first Borrow this book in your web browser using your account")
        print("      before running this tool to access the high-resolution pages.")
        print("==============================================\n")
        if status_label:
            status_label.config(text="CDL Loan Missing. Borrow book first!", fg="#F44336")
        return False
        
    total_pages = len(flat_links)
    print(f"[INFO] Total Pages resolved: {total_pages}")
    
    downloads_dir = os.path.dirname(pdf_path)
    temp_dir = os.path.join(downloads_dir, f"temp_{ia_id}")
    os.makedirs(temp_dir, exist_ok=True)
    
    # 6. Concurrently download pages using ThreadPoolExecutor
    print(f"[INFO] Pulling {total_pages} pages concurrently. Please wait...")
    if status_label:
        status_label.config(text=f"Pulling pages (0/{total_pages})...", fg="#A855F7")
        
    jpeg_paths = [None] * total_pages
    downloaded_count = [0]
    download_lock = threading.Lock()
    
    high_res_links = [f"{link}&rotate=0&scale=3" for link in flat_links]
    
    def download_worker(index, link):
        if state.abort_requested:
            return
            
        page_file = os.path.join(temp_dir, f"page_{index:04d}.jpg")
        success = False
        headers = {
            "Referer": "https://archive.org/",
            "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Dest": "image",
        }
        
        # Retry up to 3 times
        for attempt in range(3):
            if state.abort_requested:
                return
            try:
                resp = session.get(link, headers=headers, timeout=20)
                if resp.status_code == 200:
                    image_content = resp.content
                    obf_header = resp.headers.get("X-Obfuscate")
                    if obf_header:
                        image_content = deobfuscate_image(image_content, link, obf_header)
                        
                    with open(page_file, "wb") as f:
                        f.write(image_content)
                    
                    success = True
                    break
                elif resp.status_code == 403:
                    session.post("https://archive.org/services/loans/loan/searchInside.php", data={"action": "grant_access", "identifier": ia_id}, timeout=10)
            except Exception:
                time.sleep(1)
                
        if success:
            with download_lock:
                jpeg_paths[index] = page_file
                downloaded_count[0] += 1
                progress = downloaded_count[0]
                if progress % 5 == 0 or progress == total_pages:
                    print(f"[INFO] Pulled page {progress}/{total_pages}...")
                    if status_label:
                        status_label.config(text=f"Pulling page {progress}/{total_pages}...", fg="#A855F7")
                        
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=8) as executor:
        for idx, link in enumerate(high_res_links):
            executor.submit(download_worker, idx, link)
            
    success_compiled = False
    valid_jpegs = [path for path in jpeg_paths if path is not None]
    
    if len(valid_jpegs) == total_pages and not state.abort_requested:
        print("[INFO] All pages successfully fetched and decrypted.")
        if status_label:
            status_label.config(text="Stitching page images into PDF...", fg="#00ADB5")
        compile_jpegs_to_pdf(valid_jpegs, pdf_path)
        success_compiled = True
        if state.GUI_MODE:
            open_in_explorer(pdf_path)
    elif state.abort_requested:
        print("[INFO] Download aborted by user.")
    else:
        print(f"[ERROR] Page pulling failed. Only {len(valid_jpegs)}/{total_pages} pages were retrieved.")
        if status_label:
            status_label.config(text="Download failed. Some pages missing.", fg="#F44336")
            
    # Clean up temporary images
    print("[INFO] Cleaning up temporary image cache...")
    for path in valid_jpegs:
        try:
            os.remove(path)
        except:
            pass
    try:
        os.rmdir(temp_dir)
    except:
        pass
        
    return success_compiled


def try_download_book(identifier, title, status_label=None, root_widget=None):
    """Strategy for downloading free public domain books from Open Library / Internet Archive and Project Gutenberg."""
    if not identifier and not title:
        print("\n--- [BOOK STRATEGY] Skipped (No ID or Title available) ---")
        return False
        
    print("\n--- [BOOK STRATEGY] Querying Free Book Repositories ---")
    
    # Extract prefix and key
    key = ""
    prefix = ""
    if identifier and ":" in identifier:
        prefix, key = identifier.split(":", 1)
        prefix = prefix.strip().lower()
        key = key.strip()
        
    success = False
    
    # 1. If prefix is 'ia' (Internet Archive ID), download from archive.org directly!
    if prefix == "ia" and key:
        print(f"[INFO] Found Internet Archive ID: {key}")
        ia_url = f"https://archive.org/download/{key}/{key}.pdf"
        filename = f"{clean_filename(title if title else key)}.pdf"
        register_discovered_url(f"https://archive.org/details/{key}", "Internet Archive Details / Borrow Page")
        print(f"[INFO] Downloading direct PDF from Internet Archive: {ia_url}")
        success = download_file(ia_url, filename, category="book")
        if success:
            return True
        else:
            print("[TIP] This book is copyrighted or locked under Controlled Digital Lending (CDL).")
            print("      Archive.org blocks direct PDF pulls and serves them as protected online reader images.")
            
            # Fallback: Interactively scrape and compile images!
            success = try_download_ia_pages(key, filename, title, status_label=status_label, root_widget=root_widget)
            if success:
                return True
            
    # 2. Try Project Gutenberg search via Gutendex API (Title search)
    if not success and title:
        print(f"[INFO] Querying Project Gutenberg (Gutendex) for '{title}'...")
        try:
            gutendex_url = f"https://gutendex.com/books/?search={urllib.parse.quote(title)}"
            req = urllib.request.Request(gutendex_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
                
            results = data.get('results', [])
            if results:
                best_match = results[0]
                guten_id = best_match.get('id')
                formats = best_match.get('formats', {})
                
                # Check for PDF or EPUB formats
                pdf_url = formats.get('application/pdf') or formats.get('application/x-mobipocket-ebook')
                epub_url = formats.get('application/epub+zip')
                html_url = formats.get('text/html')
                
                # Prefer PDF, fallback to EPUB
                target_url = pdf_url if pdf_url else epub_url
                if not target_url and html_url:
                    target_url = html_url
                    
                if target_url:
                    ext = ".pdf" if "pdf" in target_url else (".epub" if "epub" in target_url else ".html")
                    print(f"[INFO] Found Gutenberg Book: '{best_match.get('title')}' (ID: {guten_id})")
                    register_discovered_url(f"https://www.gutenberg.org/ebooks/{guten_id}", "Project Gutenberg Details Page")
                    register_discovered_url(target_url, "Project Gutenberg Book File")
                    print(f"[INFO] Downloading book file: {target_url}")
                    filename = f"Gutenberg_{clean_filename(title)}{ext}"
                    success = download_file(target_url, filename, category="book")
                    if success:
                        return True
        except Exception as e:
            print(f"[WARNING] Project Gutenberg query failed: {e}")
            
    # 3. If we only have ISBN or OL Key, query Open Library's Edition API to resolve Internet Archive ID
    if not success and (prefix in ("isbn", "ol") or key):
        print(f"[INFO] Querying Open Library API to resolve Internet Archive ID...")
        try:
            ol_url = ""
            if prefix == "isbn":
                ol_url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{key}&format=json&jscmd=data"
                register_discovered_url(f"https://openlibrary.org/isbn/{key}", "OpenLibrary Book Page")
            elif prefix == "ol":
                ol_url = f"https://openlibrary.org/works/{key}.json"
                register_discovered_url(f"https://openlibrary.org/works/{key}", "OpenLibrary Work Page")
                
            if ol_url:
                req = urllib.request.Request(ol_url, headers=HEADERS)
                with urllib.request.urlopen(req, timeout=10) as response:
                    res_data = json.loads(response.read().decode())
                    
                ia_id = None
                if prefix == "isbn":
                    book_data = res_data.get(f"ISBN:{key}", {})
                    ia_id = book_data.get('identifiers', {}).get('archive', [None])[0] or book_data.get('ocaid')
                
                if ia_id:
                    ia_url = f"https://archive.org/download/{ia_id}/{ia_id}.pdf"
                    filename = f"{clean_filename(title if title else ia_id)}.pdf"
                    register_discovered_url(f"https://archive.org/details/{ia_id}", "Internet Archive Details / Borrow Page")
                    print(f"[INFO] Resolved Internet Archive ID: {ia_id}")
                    print(f"[INFO] Downloading direct PDF from Internet Archive: {ia_url}")
                    success = download_file(ia_url, filename, category="book")
                    if success:
                        return True
                    else:
                        print("[TIP] This resolved book is copyrighted or locked under CDL on Archive.org.")
                        print("      Archive.org blocks direct PDF pulls and serves them as protected online reader images.")
                        
                        # Fallback: Interactively scrape and compile images!
                        success = try_download_ia_pages(ia_id, filename, title, status_label=status_label, root_widget=root_widget)
                        if success:
                            return True
        except Exception as e:
            print(f"[WARNING] Open Library resolving failed: {e}")
            
    # 4. Fallback: Search Open Library by Title to get another matching copy with Internet Archive ID
    if not success and title:
        print(f"[INFO] Searching Open Library by Title to find alternate open editions...")
        try:
            search_url = f"https://openlibrary.org/search.json?title={urllib.parse.quote(title)}&fields=ia&limit=3"
            req = urllib.request.Request(search_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
                
            docs = data.get('docs', [])
            for doc in docs:
                ia_list = doc.get('ia', [])
                if ia_list:
                    ia_id = ia_list[0]
                    ia_url = f"https://archive.org/download/{ia_id}/{ia_id}.pdf"
                    filename = f"{clean_filename(title)}.pdf"
                    register_discovered_url(f"https://archive.org/details/{ia_id}", "Internet Archive Details / Borrow Page")
                    print(f"[INFO] Found alternate edition Internet Archive ID: {ia_id}")
                    print(f"[INFO] Downloading direct PDF from Internet Archive: {ia_url}")
                    success = download_file(ia_url, filename, category="book")
                    if success:
                        return True
                    else:
                        print("[TIP] This alternate edition is copyrighted or locked under CDL on Archive.org.")
                        print("      Archive.org blocks direct PDF pulls and serves them as protected online reader images.")
                        
                        # Fallback: Interactively scrape and compile images!
                        success = try_download_ia_pages(ia_id, filename, title, status_label=status_label, root_widget=root_widget)
                        if success:
                            return True
        except Exception as e:
            print(f"[WARNING] Alternate Open Library search failed: {e}")
            
    return False
