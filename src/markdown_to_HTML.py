from htmlnode import LeafNode, ParentNode
from block_management import block_to_block_type, markdown_to_blocks, BlockType
from regex_utilities import text_to_textnodes
from textnode import text_node_to_html_node

def markdown_to_html_node(markdown: str) -> ParentNode:
    outParentNode = ParentNode("div", [], None)
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == BlockType.CODE:
            code = block[4:-3]
            code_children = [LeafNode(None, code)] if code else []
            code_node = ParentNode("code", code_children)
            outParentNode.children.append(ParentNode("pre", [code_node]))
            continue

        children = [
            text_node_to_html_node(text_node)
            for text_node in text_to_textnodes(block)
        ]
        outParentNode.children.append(ParentNode("p", children))

    return outParentNode

if __name__ == "__main__":
    md = """
This is **bolded** paragraph text in a p tag here

This is another paragraph with _italic_ text and `code` here

"""

    temp = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"

    node = markdown_to_html_node(md)
    html = node.to_html()
    print(html)
    print(temp)
    print("Does the html match? ", html == temp)


    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    temp = "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"

    node = markdown_to_html_node(md)
    html = node.to_html()
    print(html)
    print(temp)
    print("Does the html match? ", html == temp)