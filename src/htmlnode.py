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
    