import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_create(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertIsInstance(node, LeafNode)

    def test_props_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        htmled_propped = node.props_to_html()
        self.assertEqual(htmled_propped, 'href="https://www.google.com"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Here!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click Here!</a>')

    def test_leaf_to_html_none(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()