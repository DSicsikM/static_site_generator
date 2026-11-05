from textnode import TextNode,TextType

def main():
    text = "This is some text"
    textType = TextType.LINK
    url = "https://www.boot.dev"
    textNode = TextNode(text,textType,url)
    print(textNode)

main()