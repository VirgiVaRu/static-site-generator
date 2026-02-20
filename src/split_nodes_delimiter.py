from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        segments = old_node.text.split(delimiter)
        if len(segments) % 2 != 1:
            raise Exception("invalid Markdown syntax. every demiliter must have a match")
        
        for i in range(0, len(segments)-1, 2):
            text_node = TextNode(segments[i], TextType.TEXT)
            if text_node.text != "":
                new_nodes.append(text_node)
            delimited_node = TextNode(segments[i+1], text_type)
            new_nodes.append(delimited_node)
        text_node = TextNode(segments[-1], TextType.TEXT)
        if text_node.text != "":
            new_nodes.append(text_node)
    
    return new_nodes
                    