from htmlnode import LeafNode, ParentNode
from block_management import block_to_block_type, markdown_to_blocks, BlockType
from regex_utilities import text_to_textnodes
from textnode import text_node_to_html_node

def markdown_to_html_node(markdown: str) -> ParentNode:
    outParentNode = ParentNode("div", [], None)
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        print(f"Block: {block} | Type: {block_to_block_type(block)}")
        if block_to_block_type(block) == BlockType.CODE:
            code = block[4:-3]
            code_children = [LeafNode(None, code)] if code else []
            code_node = ParentNode("code", code_children)
            outParentNode.children.append(ParentNode("pre", [code_node]))
            continue

        elif block_to_block_type(block) == BlockType.QUOTE:
            quote = block[2:]
            quote_children = [
                text_node_to_html_node(text_node)
                for text_node in text_to_textnodes(quote)
            ]
            outParentNode.children.append(ParentNode("blockquote", quote_children))
            continue

        elif block_to_block_type(block) == BlockType.UNORDERED_LIST:
            list_items = block.split("\n")
            list_children = []
            for item in list_items:
                item_text = item[2:]
                item_children = [
                    text_node_to_html_node(text_node)
                    for text_node in text_to_textnodes(item_text)
                ]
                list_children.append(ParentNode("li", item_children))
            outParentNode.children.append(ParentNode("ul", list_children))
            continue

        elif block_to_block_type(block) == BlockType.ORDERED_LIST:
            list_items = block.split("\n")
            list_children = []
            for item in list_items:
                item_text = item[3:]
                item_children = [
                    text_node_to_html_node(text_node)
                    for text_node in text_to_textnodes(item_text)
                ]
                list_children.append(ParentNode("li", item_children))
            outParentNode.children.append(ParentNode("ol", list_children))
            continue

        elif block_to_block_type(block) == BlockType.HEADING:
            heading_level = len(block.split(" ")[0])
            heading_text = block[heading_level + 1:]
            heading_children = [
                text_node_to_html_node(text_node)
                for text_node in text_to_textnodes(heading_text)
            ]
            outParentNode.children.append(
                ParentNode(f"h{heading_level}", heading_children)
            )
            continue

        elif block_to_block_type(block) == BlockType.PARAGRAPH:
            children = [
                text_node_to_html_node(text_node)
                for text_node in text_to_textnodes(block)
            ]
            outParentNode.children.append(ParentNode("p", children))

        else:
            raise Exception(f"Block type not recognized ------- <{block_to_block_type(block)}>")

    return outParentNode