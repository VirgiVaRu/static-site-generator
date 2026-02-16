import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "totally reliable link", {"href":"https://github.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://github.com\">totally reliable link</a>")
        
    def test_leaf_to_html_image(self):
        node = LeafNode("img", "very pretty image", {"src":"pretty_image.png", "alt":"a very pretty image"})
        self.assertEqual(node.to_html(), "<img src=\"pretty_image.png\" alt=\"a very pretty image\">very pretty image</img>")

    def test_leaf_with_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()