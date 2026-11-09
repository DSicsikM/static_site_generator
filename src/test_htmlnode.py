import unittest
from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        nul_htmlNode = HTMLNode()
        nul_htmlNode2 = HTMLNode()
        self.assertEqual(nul_htmlNode, nul_htmlNode2)

    def test_eq_properties(self):
        htmlNode = HTMLNode("<a>","This is some text",None,{"property1" : "value1"})
        htmlNode2 = HTMLNode("<a>","This is some text",None,{"property1" : "value1"})
        self.assertEqual(htmlNode, htmlNode2)

    def test_not_eq_properties(self):
        htmlNode = HTMLNode("<a>","This is some text",None,{"property1" : "value1"})
        htmlNode2 = HTMLNode("<a>","This is some other text",None,{"property1" : "value1"})
        self.assertNotEqual(htmlNode, htmlNode2)

    def test_nul_properties(self):
        htmlNode = HTMLNode()
        self.assertTrue(
            htmlNode.tag is None and
            htmlNode.value is None and
            htmlNode.children is None and
            htmlNode.props is None
            )

    def test_props_to_html(self):
        htmlNode = HTMLNode()
        try:
            print(htmlNode.to_html())
        except NotImplementedError:
            self.assertTrue(True)

    # Commenting for tidyness purposes :)
    # def test_repr(self):
    #     htmlNode_child = HTMLNode("<a>","This is a child",None,{"property2" : "value2"})
    #     htmlNode = HTMLNode("<p>","This is a parent",htmlNode_child,{"property1" : "value1"})
    #     print(htmlNode)

    # Commenting for tidyness purposes :)
    # def test_props_to_html(self):
    #     htmlNode = HTMLNode("<p>","This is a parent",None,{"property1" : "value1"})
    #     print(htmlNode.props_to_html())


if __name__ == "__main__":
    unittest.main()