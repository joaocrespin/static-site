import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_create(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertIsInstance(node, ParentNode)

    def test_to_html_p(self):
        node = ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                ).to_html()
        self.assertEqual(node, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_grandchildren(self):
        first_grandchild_node = LeafNode("b", "number1")
        second_grandchild_node = LeafNode("b", "number2")
        child_node = ParentNode("span", [first_grandchild_node, second_grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>number1</b><b>number2</b></span></div>",
        )

    def test_to_html_with_multiple_children_andgrandchildren(self):
        first_grandchild_node = LeafNode("b", "number1")
        second_grandchild_node = LeafNode("b", "number2")
        third_grandchild_node = LeafNode("b", "number3")
        fourth_grandchild_node = LeafNode("b", "number4")
        first_child_node = ParentNode("span", [first_grandchild_node, second_grandchild_node])
        second_child_node = ParentNode("span", [third_grandchild_node, fourth_grandchild_node])
        parent_node = ParentNode("div", [first_child_node, second_child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>number1</b><b>number2</b></span><span><b>number3</b><b>number4</b></span></div>",
        )

    def test_no_children(self):
        node = ParentNode("div", None)
        self.assertIsNone(node.children)

    def test_no_children_to_html(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()
          
if __name__ == "__main__":
    unittest.main()