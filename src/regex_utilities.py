import re

def extract_markdown_images(text:str) -> list[tuple]:
    image_names = re.findall(r"!\[([^\]]*)\]", text)
    image_urls = re.findall(r"\(([^)]+)\)", text)
    return list(zip(image_names, image_urls))

def extract_markdown_links(text:str) -> list[tuple]:
    link_names = re.findall(r"\[([^\]]*)\]", text)
    link_urls = re.findall(r"\(([^)]+)\)", text)
    return list(zip(link_names, link_urls))
