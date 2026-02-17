class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        result = ""
        if not self.props:
            return ""
        
        for key, value in self.props.items():
            result += f' {key}="{value}"'

        return result

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None,  props)

    def to_html(self):
        if not self.value:
            raise ValueError("no value inside the leaf")
        
        if not self.tag:
            return f"{self.value}"
        
        result = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        return result
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("no tag inside parentnode")
        
        if not self.children:
            raise ValueError("no children in parentnode")
        
        result = ""

        for items in self.children:
            result += items.to_html()

        return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"