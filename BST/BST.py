''' BST in Python '''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
class Tree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            pass
    def recursive_add(self, node, value):
        if node.value > value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.recursive_add(node.left, value)
                
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.recursive_add(node.right, value)
                
    def in_order(self, node):
        if node.left is not None:
            self.in_order(node.left)
        print(node.value)
        if node.right is not None:
            self.in_order(node.right)
            
    def pre_order(self, node):
        print(node.value)
        if node.left is not None:
            self.pre_order(node.left)
        if node.right is not None:
            self.pre_order(node.right)
            
    def post_order(self, node):
        if node.left is not None:
            self.post_order(node.left)
        if node.right is not None:
            self.post_order(node.right)
        print(node.value)