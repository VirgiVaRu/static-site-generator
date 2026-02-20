from parentnode import *
from markdown_to_blocks import *
from block_to_block_type import *
from textnode import *
from text_to_textnodes import text_to_textnodes
from textnode_to_htmlnode import *


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_html = ParentNode("div", [])
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                children = divide_text(block)
                parent_html.children.append(ParentNode("p", children))
            case BlockType.HEADING:
                hashtags, text = block.split(' ', 1)
                children = divide_text(text)
                parent_html.children.append(ParentNode(f"h{len(hashtags)}", children))
            case BlockType.CODE:
                node = TextNode(block[4:-3], TextType.CODE)
                node = text_node_to_html_node(node)
                parent_html.children.append(ParentNode("pre", [node]))
            case BlockType.QUOTE:
                lines = block.split("\n")
                whole_quote = []
                for line in lines:
                    whole_quote.append(line[1:].strip())
                whole_quote = "\n".join(whole_quote)
                children = divide_text(whole_quote)
                parent_html.children.append(ParentNode("blockquote", children))
            case BlockType.UNORDERED_LIST:
                children = unordered_list_bullets(block)
                parent_html.children.append(ParentNode("ul", children))
            case BlockType.ORDERED_LIST:
                children = ordered_list_bullets(block)
                parent_html.children.append(ParentNode("ol", children))
            case _:
                raise Exception("Unrecognized block type")
    return parent_html

def divide_text(text):
    lines = text.split("\n")
    for line in lines:
        line = line.strip()
    text = " ".join(lines)
    nodes = text_to_textnodes(text)
    html_nodes = []
    for node in nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes

def unordered_list_bullets(list):
    lines = list.split("\n")
    bullets = []
    for line in lines:
        line = line[1:]
        line = line.strip()
        bullets.append(ParentNode("li", divide_text(line)))
    return bullets

def ordered_list_bullets(list):
    lines = list.split("\n")
    bullets = []
    for line in lines:
        _, line = line.split(" ", 1)
        bullets.append(ParentNode("li", divide_text(line)))
    return bullets