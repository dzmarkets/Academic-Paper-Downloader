import json
import os
import time
import requests
import sys

def load_json(path):
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {path}: {e}")
    return {}

def save_json(data, path):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving {path}: {e}")

def main():
    extracted_path = "extracted_journals.json"
    resolved_path = "resolved_journal_links.json"
    
    if not os.path.exists(extracted_path):
        print(f"Error: {extracted_path} not found. Please run extract_journals.py first.")
        sys.exit(1)
        
    with open(extracted_path, 'r', encoding='utf-8') as f:
        extracted_data = json.load(f)
        
    # Loaded existing resolved links if they exist, for resuming
    resolved_data = load_json(resolved_path)
    print(f"Loaded {len(resolved_data)} already resolved ISSN mappings.")
    
    # Identify unresolved ISSNs
    all_issns = set(extracted_data.keys())
    resolved_issns = set(resolved_data.keys())
    unresolved_issns = list(all_issns - resolved_issns)
    
    total_to_resolve = len(unresolved_issns)
    print(f"Total ISSNs to resolve: {total_to_resolve}")
    
    if total_to_resolve == 0:
        print("All ISSNs are already resolved!")
        build_lightweight_map(resolved_data)
        return

    headers = {
        "User-Agent": "AcademicPaperDownloader/2.4.1.0 (https://github.com/dzmarkets/Academic-Paper-Downloader; mailto:yazid.academic@example.com)"
    }
    
    batch_size = 50
    batches = [unresolved_issns[i:i + batch_size] for i in range(0, len(unresolved_issns), batch_size)]
    
    print(f"Processing in {len(batches)} batches of {batch_size}...")
    
    success_count = 0
    failure_count = 0
    start_time = time.time()
    
    try:
        for idx, batch in enumerate(batches):
            # To handle cases where some ISSNs in this batch were resolved in a previous iteration of the loop 
            # (e.g. because they were returned as part of another journal's response)
            batch = [issn for issn in batch if issn not in resolved_data]
            if not batch:
                continue
                
            issn_filter = "|".join(batch)
            url = f"https://api.openalex.org/sources?filter=issn:{issn_filter}&per_page=100&select=display_name,homepage_url,issn"
            
            # Simple retry mechanism
            retries = 3
            response = None
            for attempt in range(retries):
                try:
                    response = requests.get(url, headers=headers, timeout=15)
                    if response.status_code == 200:
                        break
                    elif response.status_code == 429:
                        print(f"\nRate limited (429). Sleeping 10s... (Attempt {attempt+1}/{retries})")
                        time.sleep(10)
                    else:
                        print(f"\nHTTP {response.status_code} received. Sleeping 2s... (Attempt {attempt+1}/{retries})")
                        time.sleep(2)
                except Exception as e:
                    print(f"\nRequest exception: {e}. Sleeping 2s... (Attempt {attempt+1}/{retries})")
                    time.sleep(2)
            
            if response is None or response.status_code != 200:
                print(f"\nFailed to query batch {idx+1}/{len(batches)} after {retries} attempts.")
                # We skip this batch's resolution this time so we don't mark them as checked
                failure_count += len(batch)
                continue
                
            # Process results
            res_json = response.json()
            results = res_json.get("results", [])
            
            # Map of which ISSNs we found in this batch query's results
            found_issns = set()
            
            for src in results:
                homepage = src.get("homepage_url")
                src_issns = src.get("issn", [])
                
                # We map all ISSNs of this source to its homepage
                for s_issn in src_issns:
                    # Clean and format the returned ISSN
                    s_issn = s_issn.strip().upper()
                    if '-' not in s_issn and len(s_issn) == 8:
                        s_issn = f"{s_issn[:4]}-{s_issn[4:]}"
                    
                    found_issns.add(s_issn)
                    
                    # Store resolved info
                    original_info = extracted_data.get(s_issn, {})
                    resolved_data[s_issn] = {
                        "title": original_info.get("title") or src.get("display_name"),
                        "publisher": original_info.get("publisher"),
                        "homepage_url": homepage,
                        "issn_list": src_issns,
                        "source": original_info.get("source") or "OpenAlex"
                    }
                    
            # For the ISSNs in the query batch that weren't found in the results,
            # mark them as checked but having no homepage URL (to prevent re-querying)
            for issn in batch:
                if issn not in found_issns:
                    original_info = extracted_data.get(issn, {})
                    resolved_data[issn] = {
                        "title": original_info.get("title"),
                        "publisher": original_info.get("publisher"),
                        "homepage_url": None,
                        "issn_list": [issn],
                        "source": original_info.get("source")
                    }
            
            success_count += len(batch)
            
            # Print progress
            elapsed = time.time() - start_time
            avg_time = elapsed / (idx + 1)
            est_remaining = avg_time * (len(batches) - (idx + 1))
            sys.stdout.write(
                f"\rBatch {idx+1}/{len(batches)} | Resolved: {len(resolved_data)} total | "
                f"Progress: {idx+1/len(batches)*100:.1f}% | Est. Remaining: {est_remaining/60:.1f}m"
            )
            sys.stdout.flush()
            
            # Save progress every 20 batches
            if (idx + 1) % 20 == 0:
                save_json(resolved_data, resolved_path)
                
            # Polite sleep
            time.sleep(0.15)
            
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Saving current progress...")
        save_json(resolved_data, resolved_path)
        sys.exit(0)
        
    # Final save
    save_json(resolved_data, resolved_path)
    print(f"\n\nResolution complete! Total resolved mappings: {len(resolved_data)}")
    print(f"Successes: {success_count}, Failures (skipped): {failure_count}")
    
    # Build lightweight map
    build_lightweight_map(resolved_data)

def build_lightweight_map(resolved_data):
    # Create a light map of ISSN -> Homepage URL (skipping None/null values)
    issn_to_url = {}
    for issn, info in resolved_data.items():
        url = info.get("homepage_url")
        if url:
            issn_to_url[issn] = url
            
    light_path = "journal_issn_to_url.json"
    save_json(issn_to_url, light_path)
    print(f"Lightweight lookup map saved to {light_path} (contains {len(issn_to_url)} homepages)")

if __name__ == "__main__":
    main()
