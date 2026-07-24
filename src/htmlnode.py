class HtmlNode():
    def __init__(self, tag:str = None, value:str = None, children: list[HtmlNode] = None, 
                 props: dict[str, str] = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if not self.props:
            return ""
        html = " ".join(f'{prop}="{self.props[prop]}"' for prop in self.props)
        return html

    def __repr__(self) -> str:
        return f"HtmlNode({self.tag}\n{self.value}\n{self.children}\n{self.props})"