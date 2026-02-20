import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
            )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = """
# This is a heading 1

## This is a heading 2

### And this is a heading 3 with _italic_ text and `code`

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a heading 1</h1><h2>This is a heading 2</h2><h3>And this is a heading 3 with <i>italic</i> text and <code>code</code></h3></div>",
            )
    
    def test_quote(self):
        md = """
> This is **bolded** quote
> text in a blockquote
> with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is <b>bolded</b> quote text in a blockquote with <i>italic</i> text and <code>code</code> here</blockquote></div>",
            )
    
    def test_unordered_list(self):
        md = """
- A bullet point
- with `code`
- and **bold**

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>A bullet point</li><li>with <code>code</code></li><li>and <b>bold</b></li></ul></div>",
            )
    
    def test_ordered_list(self):
        md = """
1. A bullet point
2. with `code`
3. and **bold**

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>A bullet point</li><li>with <code>code</code></li><li>and <b>bold</b></li></ol></div>",
            )