import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_no_props(self):
        node = HTMLNode("b", "some text")
        self.assertEqual(node.props_to_html(), "")

    def test_one_prop(self):
        node = HTMLNode("link", "reliable link", props={"href":"https://www.github.com"})
        self.assertEqual(" href=\"https://www.github.com\"", node.props_to_html())

    def test_props(self):
        node = HTMLNode("img", "pretty image", props={"src":"some_image.png", "alt":"pretty image"})
        self.assertEqual(" src=\"some_image.png\" alt=\"pretty image\"", node.props_to_html())
