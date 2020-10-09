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
        if data < node.data:
            if node.left_child:
                self.insert_node(data, node.left_child)
            else:
                node.left_child = Node(data, node)
        elif data > node.data:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                node.right_child = Node(data, node)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def traverse_in_order(self, node):
        """
            Recursively visiting each subsequent node on each side.
        """
        if node.left_child:
            self.traverse_in_order(node.left_child)

        print(node.data)

        if node.right_child:
            self.traverse_in_order(node.right_child)

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)



    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)
    
    def get_max(self, node):
        if node.right_child:
            return self.get_max(node.right_child)
        return node.data

    def get_max_iter(self):
        actual = self.root
        while actual.right_child is not None:
            actual = actual.right_child
        
        return actual.data


bst = BinarySearchTree()
bst.insert(4)
bst.insert(5)
bst.insert(24)
bst.traverse()
print(bst.get_max_value())
bst.insert(62)
print(bst.get_max_iter())