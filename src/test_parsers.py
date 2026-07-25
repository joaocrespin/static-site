import unittest
from textnode import TextNode, TextType
from markdown_parsers import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes

class TestParsers(unittest.TestCase):
    def test_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[0], TextNode("This is text with a ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("code block", TextType.CODE))
        self.assertEqual(new_nodes[2], TextNode(" word", TextType.TEXT))

    def test_empty_first_string(self):
        node = TextNode("**bold** end", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertIsNot(new_nodes[0].text, "")
        self.assertEqual(new_nodes[0], TextNode("bold", TextType.BOLD))

    def test_empty_node(self):
        with self.assertRaises(ValueError):
            node = TextNode("", TextType.TEXT)
            split_nodes_delimiter([node], "", TextType.TEXT)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdow_multiple_images(self):
        matches = extract_markdown_images(
            "This is text with two images, ![twice](twicejyp.com/ot9.png) and ![logo](test.com/logo)"
        )
        self.assertListEqual([("twice", "twicejyp.com/ot9.png"), ("logo", "test.com/logo")], matches)

    def test_extract_markdow_multiple_links(self):
        text = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual(text, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )
    def test_ending_image(self):
        node = TextNode(
            "ending image ![python logo](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("ending image ", TextType.TEXT),
                TextNode("python logo", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),   
            ],
            new_nodes,
        )

    def test_no_image(self):
        node = TextNode("no image at all", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("no image at all", TextType.TEXT)], new_nodes)
        
    def test_split_links(self):
        node = TextNode(
            "This is text with an [python](https://i.imgur.com/zjjcJKZ.png) and another [go](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("python", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("go", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_leading_link(self):
        node = TextNode(
            "[python](https://i.imgur.com/zjjcJKZ.png) starting link",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("python", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" starting link", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_no_link(self):
        node = TextNode("no link at all", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [TextNode("no link at all", TextType.TEXT)], new_nodes)

    def test_text_to_textnodes(self):
        textnodes = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertEqual(textnodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])

if __name__ == "__main__":
    unittest.main()