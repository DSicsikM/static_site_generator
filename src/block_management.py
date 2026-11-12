def markdown_to_blocks(markdown: str) -> list[str]:
    outList = markdown.split("\n\n")
    outList = map(lambda x: x.strip(), outList )
    
    return outList
