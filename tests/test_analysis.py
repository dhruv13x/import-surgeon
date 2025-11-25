#!/usr/bin/env python3
# tests/test_analysis.py

import unittest

from import_surgeon.modules.analysis import check_remaining_usages


class TestAnalysis(unittest.TestCase):
    # Test check_remaining_usages updated
    def test_check_remaining_usages_multiple_symbols(self):
        content = "old.mod.Sym1 used\nold.mod.Sym2 here"
        warnings = check_remaining_usages(content, "old.mod", ["Sym1", "Sym2"])
        self.assertEqual(len(warnings), 2)
        self.assertIn("Sym1: 1", warnings[0])
        self.assertIn("Sym2: 1", warnings[1])

    def test_check_remaining_usages_no_match(self):
        content = "new.mod.Sym1 used"
        warnings = check_remaining_usages(content, "old.mod", ["Sym1"])
        self.assertEqual(len(warnings), 0)

    def test_check_remaining_usages_invalid_regex(self):
        content = "some content"
        warnings = check_remaining_usages(content, "old.mod", ["*"])
        self.assertEqual(len(warnings), 0)


if __name__ == "__main__":
    unittest.main()
