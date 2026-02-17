import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_one_bold(self):
        old_nodes = [
            TextNode("This has a **bold** word.", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, '**', TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, "This has a ")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, " word.")

    def test_split_one_italic(self):
        old_nodes = [
            TextNode("This has an _italic_ word.", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, '_', TextType.ITALIC)
        self.assertEqual(len(new_nodes), 3)

    def test_split_one_code(self):
        old_nodes = [
            TextNode("This has `code`", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, '`', TextType.CODE)
        self.assertEqual(len(new_nodes), 3)

    def test_split_two_bold(self):
        old_nodes = [
            TextNode("This has **two** **bold** words.", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, '**', TextType.BOLD)
        self.assertEqual(len(new_nodes), 5)

    def test_not_matching_delimiter(self):
        old_nodes = [
            TextNode("This has **two** **bold words.", TextType.TEXT)
        ]
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter(old_nodes, '**', TextType.BOLD)

    
