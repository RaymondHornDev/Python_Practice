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
        
    def push(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            pass
    def recursive_add(node, value):
        if node.value < value:
            loc_node = Node(value)
            
            loc_node.prev = node
            node.next = loc_node
        else:
            loc_node = Node(value)
            
            loc_node.next = node
            node.prev = loc_node
            