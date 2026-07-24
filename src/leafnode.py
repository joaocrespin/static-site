from htmlnode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, tag:str, value:str, props: dict[str, str] = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("all leaf nodes must have a value")

        if self.tag is not None:
            return f"<{self.tag}" + f"{" " + self.props_to_html() + ">" if self.props else ">"}" + f"{self.value}</{self.tag}>"
    
        return self.value 

    def __repr__(self) -> str:
        return f"HtmlNode({self.tag}\n{self.value}\n{self.props})"