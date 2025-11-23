#!/usr/bin/env python3
# tests/test_cli_extended.py

import unittest
import json
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock, mock_open

from import_surgeon.cli import main, parse_args

class TestCliExtended(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_version_flag(self):
        """Test --version flag."""
        # argparse exits on --version, so we need to catch SystemExit
        with patch("sys.stdout", new=MagicMock()) as mock_stdout:
            with self.assertRaises(SystemExit):
                parse_args(["--version"])
            # We can't easily check output because argparse prints to stdout/stderr directly
            # but confirming it raises SystemExit is good enough

    @patch("import_surgeon.cli.tqdm")
    def test_tqdm_fallback(self, mock_tqdm):
        """Test tqdm fallback when import fails."""
        # We need to reload the module to trigger the fallback logic
        # But that's tricky with 'from ... import ...' style imports in tests
        # Instead, we can test the fallback function directly if we can access it

        # However, the fallback is defined inside the try/except block at module level.
        # Let's simulate ImportError by mocking sys.modules for a fresh import
        with patch.dict(sys.modules, {'tqdm': None}):
             # Reload cli
             import importlib
             import import_surgeon.cli
             importlib.reload(import_surgeon.cli)

             # Check if tqdm is the dummy function
             # The dummy function returns the iterable
             iterable = [1, 2, 3]
             self.assertEqual(import_surgeon.cli.tqdm(iterable), iterable)

             # Restore
             importlib.reload(import_surgeon.cli)

    def test_rollback_no_summary_json(self):
        """Test rollback without summary-json argument."""
        with patch("logging.Logger.error") as mock_err:
            exit_code = main(["--rollback"])
            self.assertEqual(exit_code, 2)
            mock_err.assert_called_with("Missing --summary-json for rollback")

    def test_rollback_invalid_json(self):
        """Test rollback with invalid summary json file."""
        json_path = self.temp_path / "bad.json"
        json_path.write_text("{invalid json")

        with patch("logging.Logger.error") as mock_err:
            exit_code = main(["--rollback", "--summary-json", str(json_path)])
            self.assertEqual(exit_code, 1)
            self.assertTrue(any("Rollback failed" in str(call) for call in mock_err.mock_calls))

    def test_missing_modules_or_migration(self):
        """Test missing required arguments (modules/migrations)."""
        # Case 1: No old_module, no migration
        with patch("logging.Logger.error") as mock_err:
            exit_code = main(["--new-module", "new", "--symbols", "S"])
            self.assertEqual(exit_code, 2)
            # mock_err.assert_called_with("Missing required: --old-module or migrations in config")
            self.assertTrue(any("Missing required: --old-module or migrations in config" in str(c) for c in mock_err.mock_calls))

        # Case 2: No new_module
        with patch("logging.Logger.error") as mock_err:
            exit_code = main(["--old-module", "old", "--symbols", "S"])
            self.assertEqual(exit_code, 2)
            # mock_err.assert_called_with("Missing required: --new-module or migrations in config")
            self.assertTrue(any("Missing required: --new-module or migrations in config" in str(c) for c in mock_err.mock_calls))

        # Case 3: No symbols
        with patch("logging.Logger.error") as mock_err:
            exit_code = main(["--old-module", "old", "--new-module", "new"])
            self.assertEqual(exit_code, 2)
            # mock_err.assert_called_with("Missing required: --symbol / --symbols or migrations in config")
            self.assertTrue(any("Missing required: --symbol / --symbols or migrations in config" in str(c) for c in mock_err.mock_calls))

    @patch("import_surgeon.cli.process_file")
    @patch("import_surgeon.cli.find_py_files")
    def test_process_file_errors_counting(self, mock_find, mock_process):
        """Test error counting in main loop."""
        mock_find.return_value = [Path("file1.py"), Path("file2.py")]
        mock_process.side_effect = [
             (False, "ERROR: file1", {"warnings": []}),
             (False, "OK", {"warnings": []})
        ]

        argv = ["--old-module", "old", "--new-module", "new", "--symbols", "S", str(self.temp_path)]
        exit_code = main(argv)
        self.assertEqual(exit_code, 1)

if __name__ == "__main__":
    unittest.main()
