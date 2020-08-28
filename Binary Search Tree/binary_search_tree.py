class Node:
    """Vertex in the search tree"""
    def __init__(self, data, parent):
        self.data = data 
        self.left_child = None
        self.right_child = None
        self.parent = parent

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert_node(self, data, node):
        # Left subtree
        if data < node.data:
            if node.left_child:
                self.insert_node(data, node.left_child)
            else:
                node.left_child = Node(data, node)
        # Right subtree
        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                node.right_child = Node(data, node)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)