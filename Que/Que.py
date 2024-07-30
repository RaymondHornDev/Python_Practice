''' Que in Python '''

class Node:
    def __init__(self, value) -> None:
        print('Node object created')
        self.next = None
        self.prev = None
        self.value = value
        
    def __del__(self):
        print('Node object deleted')
        
    def new_node(passed_value):
        return Node(passed_value)
    
    
class Que:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.has_nodes = False
        
    def _push(self, value):
        local_node = Node.new_node(value)
        
        if self.head == None:
            self.head = local_node
            self.tail = local_node
            self.has_nodes = True
        else:
            self.head.prev = local_node
            local_node.next = self.head
            self.head = local_node
            
    def _pop(self):
        if self.has_nodes:
            ret_node = self.tail
            self.tail = ret_node.prev
            if self.tail == None:
                self.head = None
                self.has_nodes = False
            else:
                self.tail.next = None
                ret_node.prev = None
                