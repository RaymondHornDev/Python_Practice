class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None
    
class List:
    def __init__(self) -> None:
        self.head = None
        self.has_nodes = False
        
    def push(self, value):
        if self.head is None:
            self.head = Node(value)
            self.has_nodes = True
        else:
            self.recursive_add(self.head, value)
            
    def recursive_add(self, node, value):
        if node.value < value:
            if node.next is None:
                loc_node = Node(value)
            
                loc_node.prev = node
                node.next = loc_node
            else:
                self.recursive_add(node.next, value)
        else:
            loc_node = Node(value)
            
            loc_node.next = node
            
            if node is self.head:
                self.head = loc_node
            else:
                loc_node.prev = node.prev
                loc_node.prev.next = loc_node
                
            node.prev = loc_node
            
    def pop(self):
        ret_node = self.head
        if self.head.next is not None:
            self.head = self.head.next
            self.head.prev = None
            ret_node.next = None
        else:
            self.head = None
            self.has_nodes = False
        return ret_node
    
def fill_list(passed_list, passed_array):
    for item in passed_array:
        passed_list.push(item)
        
def empty_list(passed_list):
    while passed_list.has_nodes:
        node = passed_list.pop()
        print(node.value)
    
loc_list = List()
loc_array = [1, 2, 5, 3, 7, 4, 6, 9, 8]

fill_list(loc_list, loc_array)
empty_list(loc_list)