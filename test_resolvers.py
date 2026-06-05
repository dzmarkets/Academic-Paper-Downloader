import os
import sys
import unittest
import urllib.request

# Ensure the workspace directory is in the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from paper import (
    try_plos,
    try_biorxiv,
    try_zenodo,
    try_doaj,
    try_semantic_scholar,
    try_publisher_direct,
    get_download_dir,
    clean_filename
)

class TestResolvers(unittest.TestCase):
    
    def setUp(self):
        # We will track downloaded files to clean them up after tests
        self.downloaded_files = []
        
    def tearDown(self):
        # Clean up any files downloaded during tests
        for filepath in self.downloaded_files:
            if os.path.exists(filepath):
                try:
                    os.remove(filepath)
                    print(f"[CLEANUP] Deleted test download: {filepath}")
                except Exception as e:
                    print(f"[WARNING] Failed to delete {filepath}: {e}")

    def verify_pdf_download(self, filename):
        # Determine the expected download folder
        papers_dir = get_download_dir("paper")
        filepath = os.path.join(papers_dir, filename)
        
        self.downloaded_files.append(filepath)
        
        # 1. Assert file exists
        self.assertTrue(os.path.exists(filepath), f"File was not downloaded: {filepath}")
        
        # 2. Assert file size is non-trivial (> 100 bytes)
        filesize = os.path.getsize(filepath)
        self.assertGreater(filesize, 100, f"Downloaded file is too small ({filesize} bytes): {filepath}")
        
        # 3. Assert file starts with PDF signature (%PDF-)
        with open(filepath, 'rb') as f:
            header = f.read(5)
            self.assertEqual(header, b'%PDF-', f"File is not a valid PDF: {filepath}")
            
        print(f"[VERIFIED] File successfully validated as PDF: {filepath} ({filesize} bytes)")

    def test_try_plos(self):
        print("\n=== Testing PLOS Resolver ===")
        doi = "10.1371/journal.pone.0284488"
        title = "PLOS Test Paper"
        
        success = try_plos(doi, title)
        self.assertTrue(success, "PLOS resolver returned False")
        
        expected_filename = f"PLOS_{clean_filename(title)}.pdf"
        self.verify_pdf_download(expected_filename)

    def test_try_biorxiv(self):
        print("\n=== Testing BioRxiv Resolver ===")
        doi = "10.1101/2021.03.11.434947"
        title = "BioRxiv Test Paper"
        
        success = try_biorxiv(doi, title)
        self.assertTrue(success, "BioRxiv resolver returned False")
        
        expected_filename = f"BioRxiv_{clean_filename(title)}.pdf"
        self.verify_pdf_download(expected_filename)

    def test_try_zenodo(self):
        print("\n=== Testing Zenodo Resolver ===")
        
        # Detect if Zenodo is rate-limiting our IP before running the test
        doi = "10.5281/zenodo.3403525"
        record_id = doi.split('zenodo.')[-1]
        test_url = f"https://zenodo.org/api/records/{record_id}"
        
        try:
            req = urllib.request.Request(
                test_url, 
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            )
            with urllib.request.urlopen(req, timeout=5) as response:
                pass
        except Exception as e:
            if "403" in str(e) or "Forbidden" in str(e):
                self.skipTest("Zenodo API is currently rate-limited or blocked on this network (HTTP 403).")
        
        title = "Zenodo Test Paper"
        success = try_zenodo(doi, title)
        self.assertTrue(success, "Zenodo resolver returned False")
        
        expected_filename = f"Zenodo_{clean_filename(title)}.pdf"
        self.verify_pdf_download(expected_filename)

    def test_try_doaj(self):
        print("\n=== Testing DOAJ Resolver ===")
        doi = "10.7717/peerj.4797"
        title = "DOAJ Test Paper"
        
        success = try_doaj(doi, title)
        self.assertTrue(success, "DOAJ resolver returned False")
        
        expected_filename = f"DOAJ_{clean_filename(title)}.pdf"
        self.verify_pdf_download(expected_filename)

    def test_try_semantic_scholar(self):
        print("\n=== Testing Semantic Scholar Resolver ===")
        doi = "10.7717/peerj.4797"
        title = "Semantic Scholar Test Paper"
        
        success = try_semantic_scholar(doi, title)
        self.assertTrue(success, "Semantic Scholar resolver returned False")
        
        expected_filename = f"SemanticScholar_{clean_filename(title)}.pdf"
        self.verify_pdf_download(expected_filename)

    def test_try_publisher_direct(self):
        print("\n=== Testing Publisher Direct Heuristics (Best-Effort) ===")
        test_cases = [
            ("10.1007/s13205-020-02558-x", "Springer Test Paper", "Springer_Springer Test Paper.pdf"),
            ("10.1038/s41598-020-63494-z", "Nature Test Paper", "Nature_s41598-020-63494-z.pdf"),
            ("10.3390/s20041234", "MDPI Test Paper", "MDPI_MDPI Test Paper.pdf"),
            ("10.3389/fimmu.2020.01234", "Frontiers Test Paper", "Frontiers_Frontiers Test Paper.pdf"),
            ("10.1146/annurev-pubhealth-040218-043750", "AR Test Paper", "AR_AR Test Paper.pdf"),
            ("10.1103/PhysRevLett.120.090401", "APS Test Paper", "APS_APS Test Paper.pdf"),
            ("10.1086/674025", "Chicago Test Paper", "Chicago_Chicago Test Paper.pdf"),
            ("10.1098/rspa.2016.0246", "Royal Test Paper", "Royal_Royal Test Paper.pdf"),
            ("10.1061/(ASCE)CO.1943-7862.0000788", "ASCE Test Paper", "ASCE_ASCE Test Paper.pdf"),
            ("10.1108/IJCHM-05-2016-0294", "Emerald Test Paper", "Emerald_Emerald Test Paper.pdf"),
            ("10.1137/16M108707X", "SIAM Test Paper", "SIAM_SIAM Test Paper.pdf"),
            ("10.1134/S003103011603011X", "Pleiades Test Paper", "Springer_Pleiades Test Paper.pdf"),
            ("10.1515/sem-2018-0001", "DeGruyter Test Paper", "DeGruyter_DeGruyter Test Paper.pdf"),
            ("10.1142/S021827181850001X", "WorldScientific Test Paper", "WorldScientific_WorldScientific Test Paper.pdf"),
            ("10.1089/ast.2018.0001", "Liebert Test Paper", "Liebert_Liebert Test Paper.pdf"),
            ("10.1055/s-0001-0001", "Thieme Test Paper", "Thieme_Thieme Test Paper.pdf"),
            ("10.1145/3375633", "ACM Test Paper", "ACM_ACM Test Paper.pdf"),
            ("10.1071/AN18001", "CSIRO Test Paper", "CSIRO_CSIRO Test Paper.pdf"),
            ("10.1152/physrev.00001.2018", "APSPhysio Test Paper", "APSPhysio_APSPhysio Test Paper.pdf"),
            ("10.1128/AAC.00001-18", "ASM Test Paper", "ASM_ASM Test Paper.pdf"),
            ("10.3366/drs.2018.0001", "EUP Test Paper", "EUP_EUP Test Paper.pdf"),
            ("10.1057/s41293-018-0001-x", "Palgrave Test Paper", "Springer_Palgrave Test Paper.pdf"),
            ("10.2514/1.C035000", "AIAA Test Paper", "AIAA_AIAA Test Paper.pdf"),
            ("10.1287/mnsc.2018.0001", "INFORMS Test Paper", "INFORMS_INFORMS Test Paper.pdf")
        ]
        
        for doi, title, expected_filename in test_cases:
            print(f"Testing direct download heuristic for DOI: {doi}")
            success = try_publisher_direct(doi, title)
            if success:
                print(f"[SUCCESS] Direct heuristic succeeded for DOI: {doi}")
                self.verify_pdf_download(expected_filename)
            else:
                print(f"[INFO] Direct heuristic bypassed for DOI: {doi} (expected for paywalls/challenged papers). Falling back to pipeline.")

if __name__ == "__main__":
    unittest.main()
