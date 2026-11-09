from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text: str, text_type: TextType,url: str = None ):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value):
        #If not even a text node why even bother?
        if not isinstance(value,TextNode): return False

        #Comparing all properties between themselves :)
        return self.text == value.text and self.text_type == value.text_type and self.url == value.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None,text_node.text)
        case TextType.BOLD:
            return LeafNode("b",text_node.text)
        case TextType.ITALIC:
            return LeafNode("i",text_node.text)
        case TextType.CODE:
            return LeafNode("code",text_node.text)
        case TextType.LINK:
            return LeafNode("a",text_node.text,{"href":""})
        case TextType.IMAGE:
            return LeafNode("img","",{"src":"","alt":""})
        case _:
            raise Exception(f"Text type not recognized ------- <{text_node.text_type}>")

    