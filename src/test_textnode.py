import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
            node = TextNode("This is a text node", TextType.BOLD)
            node2 = TextNode("This is also a text node", TextType.BOLD)
            self.assertNotEqual(node, node2)

    def test_url_is_None(self):
                node = TextNode("This is a text node", TextType.BOLD)
                self.assertTrue(node.url is None)

    def test_textType_not_eq(self):
                    node = TextNode("This is a text node", TextType.BOLD)
                    node2 = TextNode("This is a text node", TextType.ITALIC)
                    self.assertNotEqual(node.text_type,node2.text_type)


if __name__ == "__main__":
    unittest.main()