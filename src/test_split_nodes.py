import unittest
from textnode import TextType,TextNode
from split_nodes import split_nodes_delimiter

class TestSplitNodes(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        correct_transformation = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            ]
        self.assertEqual(new_nodes,correct_transformation)

    def test_eq_2(self):
        node = TextNode("This is text with **two** instances of a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        correct_transformation = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("two", TextType.BOLD),
            TextNode(" instances of a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
            ]
        self.assertEqual(new_nodes,correct_transformation)

    def test_no_delimiter_present(self):
        node = TextNode("This is text with a code block word, or is it?", TextType.TEXT)
        try:
            new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        except Exception:
            if Exception.__text_signature__ == "The provided delimiter was not found in the nodes":
                self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()