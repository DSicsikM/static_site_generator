from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
    outList = markdown.split("\n\n")
    outList = map(lambda x: x.strip(), outList )

    return outList

def block_to_block_type(block: str) -> BlockType:
    heading = len(re.findall(r"#+\s", block)) > 0

    if heading:
        return BlockType.HEADING

    code = len(re.findall(r"```\n.+\n```", block)) > 0

    if code:
        return BlockType.CODE

    quote = len(re.findall(r">.+\S+", block)) > 0

    if quote:
        return BlockType.QUOTE

    unordered_list = len(re.findall(r"- .+\s", block)) > 0

    if unordered_list:
        return BlockType.UNORDERED_LIST

    ordered_list = len(re.findall(r"\d+\. .+", block)) > 0

    if ordered_list:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH