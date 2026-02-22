from enum import Enum


class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None or self.props == {}:
            return ""
        props = []
        for prop in self.props:
            props.append(f" {prop}=\"{self.props[prop]}\"")
        return "".join(props)
    
    def __repr__(self):
        return f"<{self.tag}> Value: {self.value}, Children: {self.children}[{self.props_to_html()}]\n"
