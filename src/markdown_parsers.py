import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise Exception(f"The phrase {node.text} has invalid Markdown sintax")
        
        for i in range(len(parts)):
            if parts[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(parts[i], TextType.TEXT))
                continue
            new_nodes.append(TextNode(parts[i], text_type))

    return new_nodes

def extract_markdown_images(text: str) -> str:
    result = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return result

def extract_markdown_links(text: str) -> str:
    result = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return result

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
                    new_nodes.append(node)
                    continue
        parts = extract_markdown_images(node.text)
        remaining_text = node.text

        for part in parts:
            alt, url = part
            markdown_str = f"![{alt}]({url})"
            before, remaining_text = remaining_text.split(markdown_str, maxsplit=1)

            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
                    new_nodes.append(node)
                    continue
        parts = extract_markdown_links(node.text)
        remaining_text = node.text

        for part in parts:
            name, url = part
            markdown_str = f"[{name}]({url})"
            before, remaining_text = remaining_text.split(markdown_str, maxsplit=1)

            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(name, TextType.LINK, url))
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text: str) -> list[TextNode]:
    textnodes_list = split_nodes_delimiter([TextNode(text, TextType.TEXT)], "**", TextType.BOLD)
    textnodes_list = split_nodes_delimiter(textnodes_list, "_", TextType.ITALIC)
    textnodes_list = split_nodes_delimiter(textnodes_list, "`", TextType.CODE)
    textnodes_list = split_nodes_image(textnodes_list)
    textnodes_list = split_nodes_link(textnodes_list)
    return textnodes_list
