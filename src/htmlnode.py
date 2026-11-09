class HTMLNode():
    def __init__(self,tag:str = None,value:str = None,children:"HTMLNode" = None,props:dict = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise  NotImplementedError

    def props_to_html(self) -> str:
        out_html = ""
        for item in self.props:
            out_html += f"{item}=\"{self.props[item]}\""
        return out_html

    def __repr__(self):
        tag = f"Tag -> {self.tag} \n"
        value = f"Value -> {self.value} \n"
        children = f"Children -> \n  {self.children} \n"
        props = f"Props -> {self.props} \n"
        return tag + value + children + props

    def __eq__(self, value):
        #If not even a text node why even bother?
        if not isinstance(value,HTMLNode): return False

        #Comparing all properties between themselves :)
        return (
            self.tag == value.tag and 
            self.value == value.value and 
            self.children == value.children and
            self.props == value.props
            )

class LeafNode(HTMLNode):
    def __init__(self,tag:str,value:str,props:dict = None) -> None:
            self.tag = tag
            self.value = value
            self.props = props
            super(LeafNode,self).__init__(self.tag,self.value,None,self.props)

    def to_html(self) -> str:
            if self.value == "":
                 raise ValueError("Leaf node element has no VALUE.")

            if self.tag in [None,""]:
                 return self.value

            props = ""
            if self.props is not None:
                for elem in self.props:
                    props += f" {elem}=\"{self.props[elem]}\""

            return f"<{self.tag}{props}>{self.value}</{self.tag}>"

    def __repr__(self):
        tag = f"Tag -> {self.tag} \n"
        value = f"Value -> {self.value} \n"
        props = f"Props -> {self.props} \n"
        return tag + value + props