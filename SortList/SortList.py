class Node:
    def __init__(self, value) -> None:
        self.valu = value
        self.next = None
        self.prev = None
        
    def new_node(value):
        return Node(value)
    
class List:
    def __init__(self) -> None:
        self.head = None
        self.has_nodes = False