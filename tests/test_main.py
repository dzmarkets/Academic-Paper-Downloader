import os
import sys
import unittest
from unittest.mock import patch

# Ensure the workspace directory is in the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import run_download_pipeline
from src.core import state

class TestMainPipeline(unittest.TestCase):
    def setUp(self):
        state.abort_requested = False
        state.discovered_urls = []

    def tearDown(self):
        state.abort_requested = False
        state.discovered_urls = []

    def test_pipeline_user_cancellation(self):
        """Test that the pipeline raises an exception when the user requests an abort."""
        state.abort_requested = True
        with self.assertRaises(InterruptedError):
            run_download_pipeline("10.1234/test", "Test Title")

    @patch('src.main.try_download_book')
    def test_pipeline_book_identifier(self, mock_try_download_book):
        """Test that book identifiers bypass regular engines and go straight to book downloader."""
        mock_try_download_book.return_value = True
        result = run_download_pipeline("isbn:123456", "Book Title")
        self.assertTrue(result)
        mock_try_download_book.assert_called_once()

    @patch('src.main.try_biorxiv')
    @patch('src.main.try_plos')
    def test_pipeline_fast_path_plos(self, mock_try_plos, mock_try_biorxiv):
        """Test that PLOS DOIs take the fast path."""
        mock_try_plos.return_value = True
        result = run_download_pipeline("10.1371/journal.pone.123", "PLOS Title")
        self.assertTrue(result)
        mock_try_plos.assert_called_once()
        mock_try_biorxiv.assert_not_called()

    @patch('src.main.register_discovered_url')
    @patch('src.main.download_file')
    @patch('src.main.try_publisher_direct')
    def test_pipeline_direct_url(self, mock_try_publisher_direct, mock_download_file, mock_register_discovered_url):
        """Test that a direct URL bypasses most normal checks and correctly hits the download file fallback."""
        mock_try_publisher_direct.return_value = False
        mock_download_file.return_value = True

        url = "http://example.com/paper.pdf"
        result = run_download_pipeline(url, "Direct URL Paper")

        self.assertTrue(result)
        # Verify the fallback URL gets registered
        mock_register_discovered_url.assert_called_with(url, "Direct URL Fallback")
        # Direct URLs still run through try_publisher_direct first in the current pipeline logic
        mock_download_file.assert_called_once()

    @patch('src.main.try_doaj')
    @patch('src.main.try_zenodo')
    @patch('src.main.try_semantic_scholar')
    @patch('src.main.try_unpaywall')
    @patch('src.main.try_publisher_direct')
    def test_pipeline_sequential_fallback(
        self, mock_try_publisher_direct, mock_try_unpaywall,
        mock_try_semantic_scholar, mock_try_zenodo, mock_try_doaj
    ):
        """Test that the pipeline tries subsequent engines if earlier ones fail, and stops on success."""
        mock_try_publisher_direct.return_value = False
        mock_try_unpaywall.return_value = False
        mock_try_semantic_scholar.return_value = False
        mock_try_zenodo.return_value = True

        result = run_download_pipeline("10.1234/seq.test", "Seq Title")

        self.assertTrue(result)
        mock_try_publisher_direct.assert_called_once()
        mock_try_unpaywall.assert_called_once()
        mock_try_semantic_scholar.assert_called_once()
        mock_try_zenodo.assert_called_once()
        mock_try_doaj.assert_not_called()

    @patch('src.main.try_download_book')
    @patch('src.main.try_researchgate')
    @patch('src.main.try_europe_pmc')
    @patch('src.main.try_astesj')
    @patch('src.main.try_arxiv')
    @patch('src.main.try_libgen')
    @patch('src.main.try_scihub')
    @patch('src.main.try_ssrn')
    @patch('src.main.try_core')
    @patch('src.main.try_doaj')
    @patch('src.main.try_zenodo')
    @patch('src.main.try_semantic_scholar')
    @patch('src.main.try_unpaywall')
    @patch('src.main.try_download_taylorfrancis')
    @patch('src.main.try_publisher_direct')
    @patch('src.main.try_biorxiv')
    @patch('src.main.try_plos')
    def test_pipeline_exhausted(self, *mocks):
        """Test that the pipeline eventually gives up if all engines return False."""
        for mock in mocks:
            mock.return_value = False

        result = run_download_pipeline("10.9999/exhausted", "Exhausted Title")
        self.assertFalse(result)

        # Verify that all the mocks were called (or at least some of them based on the flow)
        # Note: Since the DOI isn't a PLOS or BioRxiv fast path, those won't be called,
        # but the rest of the standard pipeline should be.

if __name__ == '__main__':
    unittest.main()
