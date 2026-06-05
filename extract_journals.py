import pypdf
import re
import json
import os

def standardize_issn(raw):
    if not raw:
        return None
    clean = raw.replace('-', '').strip()
    if len(clean) == 7:
        clean = '0' + clean
    if len(clean) != 8:
        return None
    return f"{clean[:4]}-{clean[4:]}".upper()

def extract_journals_from_a(pdf_path):
    print(f"Extracting journals from A.pdf ({pdf_path})...")
    reader = pypdf.PdfReader(pdf_path)
    entries = []
    current_entry = []
    
    entry_start_re = re.compile(r'^\s*(\d{1,5})\s+')
    issn_pattern = re.compile(r'\b\d{3,4}-?\d{3}[\dXx]\b')
    
    total_pages = len(reader.pages)
    # Start from page 1 (skipping title page 0)
    for page_idx in range(1, total_pages):
        text = reader.pages[page_idx].extract_text()
        if not text:
            continue
        lines = text.split('\n')
        for line in lines:
            if "Journal title" in line or "Publisher name" in line or "Direction Générale" in line:
                continue
            
            m = entry_start_re.match(line)
            if m:
                if current_entry:
                    entries.append(current_entry)
                current_entry = [line]
            else:
                if current_entry:
                    current_entry.append(line)
                    
    if current_entry:
        entries.append(current_entry)
        
    print(f"Parsed {len(entries)} raw entries from A.pdf")
    
    journals = {}
    for entry in entries:
        full_text = " ".join(entry)
        raw_issns = issn_pattern.findall(full_text)
        if not raw_issns:
            continue
        
        issns = [standardize_issn(x) for x in raw_issns]
        issns = [x for x in issns if x]
        if not issns:
            continue
            
        first_raw_issn = raw_issns[0]
        last_raw_issn = raw_issns[-1]
        
        parts_before = full_text.split(first_raw_issn, 1)
        title_part = parts_before[0]
        title_part = entry_start_re.sub('', title_part).strip()
        
        parts_after = full_text.rsplit(last_raw_issn, 1)
        publisher_part = parts_after[1].strip() if len(parts_after) > 1 else ""
        
        issn = issns[0]
        eissn = issns[-1] if len(issns) > 1 else ""
        
        journal_info = {
            "title": title_part,
            "publisher": publisher_part,
            "issn": issn,
            "eissn": eissn,
            "source": "A.pdf"
        }
        
        journals[issn] = journal_info
        if eissn:
            journals[eissn] = journal_info
            
    print(f"Extracted {len(journals)} unique ISSN mappings from A.pdf")
    return journals

def extract_journals_from_scopus(pdf_path):
    print(f"Extracting journals from SCOPUS.pdf ({pdf_path})...")
    reader = pypdf.PdfReader(pdf_path)
    entries = []
    current_entry = []
    
    entry_start_re = re.compile(r'^\s*(\d{1,5})\s+')
    issn_pattern = re.compile(r'\b\d{3,4}-?\d{3}[\dXx]\b')
    
    total_pages = len(reader.pages)
    # Start from page 1 (skipping title page 0)
    for page_idx in range(1, total_pages):
        text = reader.pages[page_idx].extract_text()
        if not text:
            continue
        lines = text.split('\n')
        for line in lines:
            if "Journal Title" in line or "Publisher" in line or "Direction Générale" in line:
                continue
            
            m = entry_start_re.match(line)
            if m:
                if current_entry:
                    entries.append(current_entry)
                current_entry = [line]
            else:
                if current_entry:
                    current_entry.append(line)
                    
    if current_entry:
        entries.append(current_entry)
        
    print(f"Parsed {len(entries)} raw entries from SCOPUS.pdf")
    
    journals = {}
    for entry in entries:
        full_text = " ".join(entry)
        raw_issns = issn_pattern.findall(full_text)
        if not raw_issns:
            continue
        
        issns = [standardize_issn(x) for x in raw_issns]
        issns = [x for x in issns if x]
        if not issns:
            continue
            
        first_raw_issn = raw_issns[0]
        last_raw_issn = raw_issns[-1]
        
        parts_before = full_text.split(first_raw_issn, 1)
        title_part = parts_before[0]
        title_part = entry_start_re.sub('', title_part).strip()
        
        parts_after = full_text.rsplit(last_raw_issn, 1)
        publisher_part = parts_after[1].strip() if len(parts_after) > 1 else ""
        
        issn = issns[0]
        eissn = issns[-1] if len(issns) > 1 else ""
        
        journal_info = {
            "title": title_part,
            "publisher": publisher_part,
            "issn": issn,
            "eissn": eissn,
            "source": "SCOPUS.pdf"
        }
        
        journals[issn] = journal_info
        if eissn:
            journals[eissn] = journal_info
            
    print(f"Extracted {len(journals)} unique ISSN mappings from SCOPUS.pdf")
    return journals

def main():
    a_journals = extract_journals_from_a("A.pdf")
    scopus_journals = extract_journals_from_scopus("SCOPUS.pdf")
    
    # Merge journals
    merged_journals = {}
    # A.pdf has higher priority/newer or different info, we combine both
    merged_journals.update(scopus_journals)
    merged_journals.update(a_journals)
    
    print(f"Total merged unique ISSN mappings: {len(merged_journals)}")
    
    # Write to extracted_journals.json
    output_path = "extracted_journals.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(merged_journals, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully saved extracted journal metadata to {output_path}")

if __name__ == "__main__":
    main()
