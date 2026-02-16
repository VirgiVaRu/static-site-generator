from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("tag must be provided")
        if not self.children:
            raise ValueError("a parent node must have children")
        children = []
        for child in self.children:
            children.append(child.to_html())
        return f"<{self.tag}>{"".join(children)}</{self.tag}>"