import re
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter

def extract_markdown_images(text:str) -> list[tuple]:
    image_names = re.findall(r"!\[([^\]]*)\]", text)
    image_urls = re.findall(r"\(([^)]+)\)", text)
    return list(zip(image_names, image_urls))

def extract_markdown_links(text:str) -> list[tuple]:
    link_names = re.findall(r"\[([^\]]*)\]", text)
    link_urls = re.findall(r"\(([^)]+)\)", text)
    return list(zip(link_names, link_urls))

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    outNodes: list[TextNode] = list()
    for node in old_nodes:
        if "[" not in node.text or node.text_type != TextType.TEXT:
            outNodes.append(node)
        else:
            text = node.text
            break_point = text.index("[")
            while len(text) > 0:
                if break_point > 0:
                    node = TextNode(text[:break_point],TextType.TEXT)
                    text = text[break_point:]
                    if len(text) == 0:
                        outNodes.append(node)
                        break
                    break_point = text.index("[")
                else:
                    link = extract_markdown_links(text)
                    node = TextNode(link[0][0],TextType.LINK,link[0][1])
                    text = text[text.index(")")+1:]
                    if len(text) == 0:
                        outNodes.append(node)
                        break
                    break_point = text.index("[") if "[" in text else len(text)
                outNodes.append(node)
    return outNodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    outNodes: list[TextNode] = list()
    for node in old_nodes:
        if "!" not in node.text or node.text_type != TextType.TEXT:
            outNodes.append(node)
        else:
            text = node.text
            break_point = text.index("!")
            while len(text) > 0:
                if break_point > 0:
                    node = TextNode(text[:break_point],TextType.TEXT)
                    text = text[break_point:]
                    if len(text) == 0:
                        outNodes.append(node)
                        break
                    break_point = text.index("!")
                else:
                    link = extract_markdown_links(text)
                    node = TextNode(link[0][0],TextType.IMAGE,link[0][1])
                    text = text[text.index(")")+1:]
                    if len(text) == 0:
                        outNodes.append(node)
                        break
                    break_point = text.index("!") if "!" in text else len(text)
                outNodes.append(node)
    return outNodes

def text_to_textnodes(text:str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
