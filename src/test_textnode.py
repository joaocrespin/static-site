import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_create(self):
            node = TextNode("Test Node", TextType.LINK, "https://www.testnode.com")
            self.assertIsInstance(node, TextNode)

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a image node", TextType.IMAGE)
        self.assertNotEqual(node, node2)

    def test_empty_url(self):
         node = TextNode("website", TextType.LINK)
         self.assertIsNone(node.url)

    def test_empty_type(self):
         with self.assertRaises(AttributeError):
            node = TextNode("This is a text node", None)
            print(node)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")     

    def test_bold(self):
            node = TextNode("This is a bold node", TextType.BOLD)
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, "b")
            self.assertEqual(html_node.value, "This is a bold node")   

    def test_italic(self):
            node = TextNode("This is a italic node", TextType.ITALIC)
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, "i") 

    def test_code(self):
            node = TextNode("This is a text node", TextType.CODE)
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, "code")       
              
    def test_link(self):
            node = TextNode("This is a text node", TextType.LINK, "127.0.0.1")
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, "a")
            self.assertEqual(html_node.props, {"href":"127.0.0.1"})

    def test_image(self):
        node = TextNode("This is secretly an image", TextType.IMAGE, "/src/images/dolphin")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src":"/src/images/dolphin", "alt":"This is secretly an image"}) 


if __name__ == "__main__":
    unittest.main()