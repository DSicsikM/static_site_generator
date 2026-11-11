from textnode import TextNode,TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    out_nodes: list[TextNode] = list()
    for node in old_nodes:
        if node.text == "": 
            continue
        
        if node.text_type != TextType.TEXT or delimiter not in node.text:
            out_nodes.append(node)
        else:
            blocks = node.text.split(delimiter)
            if blocks[0] == "":
                transform = True
                blocks.pop(0)
            else:
                transform = False
            for block in blocks:
                if block == "": continue
                if not transform:
                    out_nodes.append(TextNode(block,TextType.TEXT))
                    transform = True
                else:
                    out_nodes.append(TextNode(block,text_type))
                    transform = False
    return out_nodes