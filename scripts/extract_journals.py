import pypdf
import re
import json
import os

def standardize_issn(raw):
    if not raw:
        return None
    clean = raw.replace('-', '').replace(' ', '').strip()
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

def extract_journals_from_cnrs(pdf_path):
    print(f"Extracting journals from CNRS.pdf ({pdf_path})...")
    reader = pypdf.PdfReader(pdf_path)
    entries = []
    current_entry = []
    
    entry_start_re = re.compile(r'^\s*(\d{1,5})\s+')
    issn_pattern = re.compile(r'\b\d{3,4}-?\d{3}[\dXx]\b')
    
    total_pages = len(reader.pages)
    for page_idx in range(total_pages):
        text = reader.pages[page_idx].extract_text()
        if not text:
            continue
        lines = text.split('\n')
        for line in lines:
            if "Titre" in line or "ISSN" in line or "Direction" in line:
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
        
    print(f"Parsed {len(entries)} raw entries from CNRS.pdf")
    
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
        parts_before = full_text.split(first_raw_issn, 1)
        title_part = parts_before[0]
        title_part = entry_start_re.sub('', title_part).strip()
        
        issn = issns[0]
        journal_info = {
            "title": title_part,
            "publisher": "",
            "issn": issn,
            "eissn": "",
            "source": "CNRS.pdf"
        }
        
        journals[issn] = journal_info
            
    print(f"Extracted {len(journals)} unique ISSN mappings from CNRS.pdf")
    return journals

def extract_journals_from_aeres(pdf_path):
    print(f"Extracting journals from AERES.pdf ({pdf_path})...")
    reader = pypdf.PdfReader(pdf_path)
    entries = []
    current_entry = []
    
    entry_start_re = re.compile(r'^\s*(\d{1,5})\s+')
    issn_pattern = re.compile(r'\b\d{3,4}-?\d{3}[\dXx]\b')
    
    total_pages = len(reader.pages)
    for page_idx in range(total_pages):
        text = reader.pages[page_idx].extract_text()
        if not text:
            continue
        lines = text.split('\n')
        for line in lines:
            if "Journal Name" in line or "ISSN" in line or "ESSN" in line or "Direction" in line:
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
        
    print(f"Parsed {len(entries)} raw entries from AERES.pdf")
    
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
        
        issn = issns[0]
        eissn = issns[-1] if len(issns) > 1 else ""
        
        journal_info = {
            "title": title_part,
            "publisher": "",
            "issn": issn,
            "eissn": eissn,
            "source": "AERES.pdf"
        }
        
        journals[issn] = journal_info
        if eissn:
            journals[eissn] = journal_info
            
    print(f"Extracted {len(journals)} unique ISSN mappings from AERES.pdf")
    return journals

def extract_journals_from_degruyter(pdf_path):
    print(f"Extracting journals from De_Gruyter.pdf ({pdf_path})...")
    reader = pypdf.PdfReader(pdf_path)
    entries = []
    current_entry = []
    
    entry_start_re = re.compile(r'^\s*(\d{1,5})\s+')
    issn_pattern = re.compile(r'\b\d{3,4}-?\d{3}[\dXx]\b')
    
    total_pages = len(reader.pages)
    for page_idx in range(total_pages):
        text = reader.pages[page_idx].extract_text()
        if not text:
            continue
        lines = text.split('\n')
        for line in lines:
            if "Journal Title" in line or "E-ISSN" in line:
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
        
    print(f"Parsed {len(entries)} raw entries from De_Gruyter.pdf")
    
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
        parts_before = full_text.split(first_raw_issn, 1)
        title_part = parts_before[0]
        title_part = entry_start_re.sub('', title_part).strip()
        
        issn = issns[0]
        journal_info = {
            "title": title_part,
            "publisher": "",
            "issn": issn,
            "eissn": "",
            "source": "De_Gruyter.pdf"
        }
        
        journals[issn] = journal_info
            
    print(f"Extracted {len(journals)} unique ISSN mappings from De_Gruyter.pdf")
    return journals

def extract_journals_from_erihplus(pdf_path):
    print(f"Extracting journals from Erih_plus.pdf ({pdf_path})...")
    reader = pypdf.PdfReader(pdf_path)
    entries = []
    current_entry = []
    
    entry_start_re = re.compile(r'^\s*(\d{1,6})\s+')
    issn_pattern = re.compile(r'\b\d{3,4}-?\d{3}[\dXx]\b')
    
    total_pages = len(reader.pages)
    for page_idx in range(total_pages):
        text = reader.pages[page_idx].extract_text()
        if not text:
            continue
        lines = text.split('\n')
        for line in lines:
            if "International Title" in line or "Print ISSN" in line:
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
        
    print(f"Parsed {len(entries)} raw entries from Erih_plus.pdf")
    
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
        
        issn = issns[0]
        eissn = issns[-1] if len(issns) > 1 else ""
        
        journal_info = {
            "title": title_part,
            "publisher": "",
            "issn": issn,
            "eissn": eissn,
            "source": "Erih_plus.pdf"
        }
        
        journals[issn] = journal_info
        if eissn:
            journals[eissn] = journal_info
            
    print(f"Extracted {len(journals)} unique ISSN mappings from Erih_plus.pdf")
    return journals

def extract_journals_from_quality(pdf_path):
    print(f"Extracting journals from Journal_quality.pdf ({pdf_path})...")
    reader = pypdf.PdfReader(pdf_path)
    entries = []
    current_entry = []
    
    entry_start_re = re.compile(r'^\s*(\d{1,5})\s+')
    issn_pattern = re.compile(r'\b\d{3,4}-?\d{3}[\dXx]\b')
    
    total_pages = len(reader.pages)
    for page_idx in range(total_pages):
        text = reader.pages[page_idx].extract_text()
        if not text:
            continue
        lines = text.split('\n')
        for line in lines:
            if "Journal ISSN" in line:
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
        
    print(f"Parsed {len(entries)} raw entries from Journal_quality.pdf")
    
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
        parts_before = full_text.split(first_raw_issn, 1)
        title_part = parts_before[0]
        title_part = entry_start_re.sub('', title_part).strip()
        
        issn = issns[0]
        journal_info = {
            "title": title_part,
            "publisher": "",
            "issn": issn,
            "eissn": "",
            "source": "Journal_quality.pdf"
        }
        
        journals[issn] = journal_info
            
    print(f"Extracted {len(journals)} unique ISSN mappings from Journal_quality.pdf")
    return journals

def extract_journals_from_scopus_lt(pdf_path):
    print(f"Extracting journals from SCOPUS_LT.pdf ({pdf_path})...")
    reader = pypdf.PdfReader(pdf_path)
    entries = []
    current_entry = []
    
    entry_start_re = re.compile(r'^\s*(\d{1,6})\s+')
    issn_pattern = re.compile(r'\b\d{3,4}-?\d{3}[\dXx]\b')
    
    total_pages = len(reader.pages)
    for page_idx in range(1, total_pages):
        text = reader.pages[page_idx].extract_text()
        if not text:
            continue
        lines = text.split('\n')
        for line in lines:
            if "Journal Title" in line or "Publisher" in line:
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
        
    print(f"Parsed {len(entries)} raw entries from SCOPUS_LT.pdf")
    
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
        
        issn = issns[0]
        eissn = issns[-1] if len(issns) > 1 else ""
        
        journal_info = {
            "title": title_part,
            "publisher": "",
            "issn": issn,
            "eissn": eissn,
            "source": "SCOPUS_LT.pdf"
        }
        
        journals[issn] = journal_info
        if eissn:
            journals[eissn] = journal_info
            
    print(f"Extracted {len(journals)} unique ISSN mappings from SCOPUS_LT.pdf")
    return journals

FT_OFFLINE_DATA = {
    "Academy of Management Journal": {
        "title": "Academy of Management Journal",
        "publisher": "Academy of Management",
        "issn": "0001-4273",
        "eissn": "1948-0989",
        "source": "Finacial_Times.pdf"
    },
    "Academy of Management Review": {
        "title": "Academy of Management Review",
        "publisher": "Academy of Management",
        "issn": "0363-7425",
        "eissn": "1930-3807",
        "source": "Finacial_Times.pdf"
    },
    "Administrative Science Quarterly": {
        "title": "Administrative Science Quarterly",
        "publisher": "Cornell University",
        "issn": "0001-8392",
        "eissn": "1930-3815",
        "source": "Finacial_Times.pdf"
    },
    "American Economic Review": {
        "title": "American Economic Review",
        "publisher": "American Economic Association",
        "issn": "0002-8282",
        "eissn": "1944-7981",
        "source": "Finacial_Times.pdf"
    },
    "Contemporary Accounting Research": {
        "title": "Contemporary Accounting Research",
        "publisher": "Wiley",
        "issn": "0823-9150",
        "eissn": "1911-3846",
        "source": "Finacial_Times.pdf"
    },
    "Human Relations": {
        "title": "Human Relations",
        "publisher": "",
        "issn": "0018-7267",
        "eissn": "1741-282X",
        "source": "Finacial_Times.pdf"
    },
    "Harvard Business Review": {
        "title": "Harvard business review",
        "publisher": "Harvard Business School Publishing",
        "issn": "0017-8012",
        "eissn": "",
        "source": "Finacial_Times.pdf"
    },
    "Human Resource Management": {
        "title": "Human Resource Management",
        "publisher": "Wiley",
        "issn": "0090-4848",
        "eissn": "1099-050X",
        "source": "Finacial_Times.pdf"
    },
    "Information Systems Research": {
        "title": "Information Systems Research",
        "publisher": "Informs",
        "issn": "1047-7047",
        "eissn": "1526-5536",
        "source": "Finacial_Times.pdf"
    },
    "Journal of Accounting and Economics": {
        "title": "Journal of Accounting and Economics",
        "publisher": "Elsevier",
        "issn": "0165-4101",
        "eissn": "1879-1980",
        "source": "Finacial_Times.pdf"
    },
    "Journal of Business Ethics": {
        "title": "Journal of Business Ethics",
        "publisher": "Kluwer Academic",
        "issn": "0167-4544",
        "eissn": "1573-0697",
        "source": "Finacial_Times.pdf"
    },
    "Journal of Business Venturing": {
        "title": "Journal of Business Venturing",
        "publisher": "Elsevier",
        "issn": "0883-9026",
        "eissn": "1873-2003",
        "source": "Finacial_Times.pdf"
    },
    "Journal of Consumer Psychology": {
        "title": "Journal of Consumer Psychology",
        "publisher": "Elsevier",
        "issn": "1057-7408",
        "eissn": "1532-7663",
        "source": "Finacial_Times.pdf"
    },
    "Journal of Consumer Research": {
        "title": "Journal of Consumer Research",
        "publisher": "University of Chicago",
        "issn": "0093-5301",
        "eissn": "1537-5277",
        "source": "Finacial_Times.pdf"
    },
    "Journal of Finance": {
        "title": "The Journal of Finance",
        "publisher": "Wiley",
        "issn": "0022-1082",
        "eissn": "1540-6261",
        "source": "Finacial_Times.pdf"
    },
    "Journal of Financial and Quantitative  Analysis": {
        "title": "Journal of Financial and Quantitative Analysis",
        "publisher": "Cambridge University Press",
        "issn": "0022-1090",
        "eissn": "1756-6916",
        "source": "Finacial_Times.pdf"
    },
    "Journal of Financial Economics": {
        "title": "Journal of Financial Economics",
        "publisher": "Elsevier",
        "issn": "0304-405X",
        "eissn": "1879-2774",
        "source": "Finacial_Times.pdf"
    },
    "Journal of International Business Studies": {
        "title": "Journal of International Business Studies",
        "publisher": "Academy of International Business",
        "issn": "0047-2506",
        "eissn": "1478-6990",
        "source": "Finacial_Times.pdf"
    },
    "Journal of Management": {
        "title": "Journal of Management",
        "publisher": "",
        "issn": "0149-2063",
        "eissn": "1557-1211",
        "source": "Finacial_Times.pdf"
    },
    "Journal of Management Information Systems": {
        "title": "Journal of Management Information Systems",
        "publisher": "",
        "issn": "0742-1222",
        "eissn": "1557-928X",
        "source": "Finacial_Times.pdf"
    },
    "Journal of Management Studies": {
        "title": "Journal of Management Studies",
        "publisher": "Wiley",
        "issn": "0022-2380",
        "eissn": "1467-6486",
        "source": "Finacial_Times.pdf"
    },
    "Journal of Marketing": {
        "title": "Journal of Marketing",
        "publisher": "American Marketing Association",
        "issn": "0022-2429",
        "eissn": "1547-7185",
        "source": "Finacial_Times.pdf"
    },
    "Journal of Marketing Research": {
        "title": "Journal of Marketing Research",
        "publisher": "American Marketing Association",
        "issn": "0022-2437",
        "eissn": "1547-7193",
        "source": "Finacial_Times.pdf"
    },
    "Journal of Operations Management": {
        "title": "Journal of Operations Management",
        "publisher": "Elsevier",
        "issn": "0272-6963",
        "eissn": "1873-1317",
        "source": "Finacial_Times.pdf"
    },
    "Journal of Political Economy": {
        "title": "Journal of Political Economy",
        "publisher": "University of Chicago",
        "issn": "0022-3808",
        "eissn": "1537-534X",
        "source": "Finacial_Times.pdf"
    },
    "Journal of the Academy of Marketing  Science": {
        "title": "Journal of the Academy of Marketing Science",
        "publisher": "",
        "issn": "0092-0703",
        "eissn": "1552-7824",
        "source": "Finacial_Times.pdf"
    },
    "Management Science": {
        "title": "Management Science",
        "publisher": "Informs",
        "issn": "0025-1909",
        "eissn": "1526-5501",
        "source": "Finacial_Times.pdf"
    },
    "Manufacturing and Service Operations  Management": {
        "title": "Manufacturing & Service Operations Management",
        "publisher": "",
        "issn": "1523-4614",
        "eissn": "1526-5498",
        "source": "Finacial_Times.pdf"
    },
    "Marketing Science": {
        "title": "Marketing Science",
        "publisher": "Informs",
        "issn": "0732-2399",
        "eissn": "1526-548X",
        "source": "Finacial_Times.pdf"
    },
    "Operations Research": {
        "title": "Operations Research",
        "publisher": "Informs",
        "issn": "0030-364X",
        "eissn": "1526-5463",
        "source": "Finacial_Times.pdf"
    },
    "Organization Science": {
        "title": "Organization Science",
        "publisher": "Informs",
        "issn": "1047-7039",
        "eissn": "1526-5455",
        "source": "Finacial_Times.pdf"
    },
    "Organization Studies": {
        "title": "Organization Studies",
        "publisher": "SAGE",
        "issn": "0170-8406",
        "eissn": "1741-3044",
        "source": "Finacial_Times.pdf"
    },
    "Production and Operations Management": {
        "title": "Production and Operations Management",
        "publisher": "Wiley",
        "issn": "1059-1478",
        "eissn": "1937-5956",
        "source": "Finacial_Times.pdf"
    },
    "Quarterly Journal of Economics": {
        "title": "The Quarterly Journal of Economics",
        "publisher": "MIT",
        "issn": "0033-5533",
        "eissn": "1531-4650",
        "source": "Finacial_Times.pdf"
    },
    "Research Policy": {
        "title": "Research Policy",
        "publisher": "",
        "issn": "0048-7333",
        "eissn": "1873-7625",
        "source": "Finacial_Times.pdf"
    },
    "Review of Accounting Studies": {
        "title": "Review of Accounting Studies",
        "publisher": "Springer",
        "issn": "1380-6653",
        "eissn": "1573-7136",
        "source": "Finacial_Times.pdf"
    },
    "Review of Economic Studies": {
        "title": "The Review of Economic Studies",
        "publisher": "The Review of Economic Studies Ltd",
        "issn": "0034-6527",
        "eissn": "1467-937X",
        "source": "Finacial_Times.pdf"
    },
    "Review of Finance": {
        "title": "International Review of Finance",
        "publisher": "",
        "issn": "1369-412X",
        "eissn": "1468-2443",
        "source": "Finacial_Times.pdf"
    },
    "Review of Financial Studies": {
        "title": "Review of Financial Studies",
        "publisher": "Oxford University Press",
        "issn": "0893-9454",
        "eissn": "1465-7368",
        "source": "Finacial_Times.pdf"
    },
    "Sloan Management Review": {
        "title": "MIT Sloan management review",
        "publisher": "MIT",
        "issn": "1532-8937",
        "eissn": "",
        "source": "Finacial_Times.pdf"
    },
    "Strategic Entrepreneurship Journal": {
        "title": "Strategic Entrepreneurship Journal",
        "publisher": "",
        "issn": "1932-4391",
        "eissn": "1932-443X",
        "source": "Finacial_Times.pdf"
    },
    "Strategic Management Journal": {
        "title": "Strategic Management Journal",
        "publisher": "Wiley",
        "issn": "0143-2095",
        "eissn": "1097-0266",
        "source": "Finacial_Times.pdf"
    },
    "The Accounting Review": {
        "title": "The Accounting Review",
        "publisher": "American Accounting Association",
        "issn": "0001-4826",
        "eissn": "1558-7967",
        "source": "Finacial_Times.pdf"
    },
    "Accounting, Organisations and Society": {
        "title": "Accounting, Organizations and Society",
        "publisher": "Elsevier",
        "issn": "0361-3682",
        "eissn": "1873-6114",
        "source": "Finacial_Times.pdf"
    },
    "Econometrica": {
        "title": "Econometrica",
        "publisher": "Econometric Society, Wiley",
        "issn": "0012-9682",
        "eissn": "1468-0262",
        "source": "Finacial_Times.pdf"
    },
    "Entrepreneurship Theory and Practice": {
        "title": "Entrepreneurship Theory and Practice",
        "publisher": "Baylor University, Wiley",
        "issn": "1042-2587",
        "eissn": "1540-6520",
        "source": "Finacial_Times.pdf"
    },
    "Journal of Accounting Research": {
        "title": "Journal of Accounting Research",
        "publisher": "University of Chicago, Wiley",
        "issn": "0021-8456",
        "eissn": "1475-679X",
        "source": "Finacial_Times.pdf"
    },
    "Journal of AppliedPsychology": {
        "title": "Journal of Applied Psychology",
        "publisher": "American Psychological Association",
        "issn": "0021-9010",
        "eissn": "1939-1854",
        "source": "Finacial_Times.pdf"
    },
    "MIS Quarterly": {
        "title": "MIS Quarterly",
        "publisher": "Management Information Systems Research Centre, University of Minnesota",
        "issn": "0276-7783",
        "eissn": "2162-9730",
        "source": "Finacial_Times.pdf"
    },
    "Organizational Behaviour and Human  Decision Processes": {
        "title": "Organizational Behavior and Human Decision Processes",
        "publisher": "Academic Press",
        "issn": "0749-5978",
        "eissn": "1095-9920",
        "source": "Finacial_Times.pdf"
    }
}

def extract_financial_times():
    print(f"Loading hardcoded resolved entries for Finacial_Times.pdf...")
    journals = {}
    for k, v in FT_OFFLINE_DATA.items():
        issn = v["issn"]
        eissn = v["eissn"]
        journals[issn] = v
        if eissn:
            journals[eissn] = v
    print(f"Extracted {len(journals)} unique ISSN mappings for Finacial_Times.pdf")
    return journals

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.abspath(os.path.join(script_dir, "..", "data"))
    
    a_pdf = os.path.join(data_dir, "A.pdf")
    scopus_pdf = os.path.join(data_dir, "SCOPUS.pdf")
    cnrs_pdf = os.path.join(data_dir, "CNRS.pdf")
    aeres_pdf = os.path.join(data_dir, "AERES.pdf")
    degruyter_pdf = os.path.join(data_dir, "De_Gruyter.pdf")
    erihplus_pdf = os.path.join(data_dir, "Erih_plus.pdf")
    quality_pdf = os.path.join(data_dir, "Journal_quality.pdf")
    scopus_lt_pdf = os.path.join(data_dir, "SCOPUS_LT.pdf")
    
    # Run all extractions
    merged_journals = {}
    
    # SCOPUS is Category B (lower priority)
    if os.path.exists(scopus_pdf):
        merged_journals.update(extract_journals_from_scopus(scopus_pdf))
        
    if os.path.exists(scopus_lt_pdf):
        merged_journals.update(extract_journals_from_scopus_lt(scopus_lt_pdf))
        
    if os.path.exists(degruyter_pdf):
        merged_journals.update(extract_journals_from_degruyter(degruyter_pdf))
        
    if os.path.exists(erihplus_pdf):
        merged_journals.update(extract_journals_from_erihplus(erihplus_pdf))
        
    if os.path.exists(quality_pdf):
        merged_journals.update(extract_journals_from_quality(quality_pdf))
        
    # Financial Times
    merged_journals.update(extract_financial_times())
    
    # Category A lists have higher priority, overlaying their classifications
    if os.path.exists(cnrs_pdf):
        merged_journals.update(extract_journals_from_cnrs(cnrs_pdf))
        
    if os.path.exists(aeres_pdf):
        merged_journals.update(extract_journals_from_aeres(aeres_pdf))
        
    if os.path.exists(a_pdf):
        merged_journals.update(extract_journals_from_a(a_pdf))
        
    print(f"Total merged unique ISSN mappings: {len(merged_journals)}")
    
    # Write to extracted_journals.json
    output_path = os.path.join(data_dir, "extracted_journals.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(merged_journals, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully saved extracted journal metadata to {output_path}")

if __name__ == "__main__":
    main()
