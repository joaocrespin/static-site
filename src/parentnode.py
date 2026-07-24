from htmlnode import HtmlNode

class ParentNode(HtmlNode):
    def __init__(self, tag:str, children: list[HtmlNode], props: dict[str, str] = None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("parent node must have a tag")
        if self.children is None:
            raise ValueError("parent node must have children")
        html = f"<{self.tag}" + f"{" " + self.props_to_html() + ">" if self.props else ">"}"

        for child in self.children:
            html += child.to_html()
        return html + f"</{self.tag}>"

    def __repr__(self) -> str:
        return f"HtmlNode({self.tag}\n{self.children}\n{self.props})"