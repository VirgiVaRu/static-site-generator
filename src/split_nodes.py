from textnode import *
from extract_markdown import *

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
        text_to_split = node.text
        text_type = node.text_type
        for image in images:
            image_alt, image_link = image
            beginning, ending = text_to_split.split(f"![{image_alt}]({image_link})", 1)
            if beginning != "":
                new_nodes.append(TextNode(beginning, text_type))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            text_to_split = ending
        if text_to_split != "":
            new_nodes.append(TextNode(text_to_split, text_type))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue
        text_to_split = node.text
        text_type = node.text_type
        for link in links:
            link_text, link_url = link
            beginning, ending = text_to_split.split(f"[{link_text}]({link_url})", 1)
            if beginning != "":
                new_nodes.append(TextNode(beginning, text_type))
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            text_to_split = ending
        if text_to_split != "":
            new_nodes.append(TextNode(text_to_split, text_type))

    return new_nodes

