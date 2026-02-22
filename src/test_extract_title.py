import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = """
# Hello world   
This is a test
"""
        self.assertEqual(extract_title(md), "Hello world")

    def test_extract_title_error(self):
        md = """
## Hello world   
This is a test
"""
        with self.assertRaises(Exception):
            extract_title(md)