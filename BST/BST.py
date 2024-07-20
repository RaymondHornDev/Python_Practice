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
            self.recursive_add(self.root, value)
        
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
        
def fill(list, value, tree):
    if value < len(list):
        tree.insert(list[value])
        fill(list, value + 1, tree)
        

        
if __name__ == "__main__":
    my_list = [5,4,3,2,1,0,6,7,8,9]
    tree = Tree()
    
    fill(my_list, 0, tree)
    
    tree.in_order(tree.root)
    tree.pre_order(tree.root)
    tree.post_order(tree.root)
    