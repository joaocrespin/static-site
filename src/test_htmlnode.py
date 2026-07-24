import unittest
from htmlnode import HtmlNode

class TestTextNode(unittest.TestCase):
    def test_create(self):
        node = HtmlNode(tag="h1", value="main text")
        self.assertIsInstance(node, HtmlNode)

    def test_props_to_html(self):
        node = HtmlNode(tag="a", value="click here", props={"href": "https://www.google.com","target": "_blank",})
        htmled_propped = node.props_to_html()
        self.assertEqual(htmled_propped, 'href="https://www.google.com" target="_blank"')

    def test_none_props_to_html(self):
        node = HtmlNode(tag="a", value="click here")
        htmled_propped = node.props_to_html()
        self.assertEqual(htmled_propped, "")

    def test_empty_node(self):
        node = HtmlNode()
        self.assertIsInstance(node, HtmlNode)


if __name__ == "__main__":
    unittest.main()