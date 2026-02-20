import unittest
from block_to_block_type import *

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        block = "This is a paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
    def test_heading(self):
        block1 = "# This is a heading 1"
        block2 = "### This is a heading 3"
        block3 = "###### This is a heading 6"
        self.assertEqual(block_to_block_type(block1), BlockType.HEADING)
        self.assertEqual(block_to_block_type(block2), BlockType.HEADING)
        self.assertEqual(block_to_block_type(block3), BlockType.HEADING)
        
    def test_code(self):
        block = """```
        text = "code of block"
        print("this is a {text}")
        ```"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        
    def test_quote(self):
        block = ">This is a quote\n>someone must have said\n>at some moment"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        
    def test_unordered_list(self):
        block = "- This is a list\n-With a couple of bullet points\n- or perhaps three"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        
    def test_ordered_list(self):
        block = "1. Now this is ordered\n2. With several steps\n3. Number 3 is the best"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)