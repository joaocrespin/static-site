from textnode import TextNode, TextType

if __name__ == "__main__":
    dummy_node = TextNode("dummy value", TextType.LINK, "https://www.google.com")
    print(dummy_node)