class Node:

    def __init__(self, data):
        self.data = data 
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None 
        self.num_of_nodes = 0
    
    def insert_at_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node 
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        actual_node = self.head

        while actual_node is not None:
            actual_node = actual_node.next_node
        
        # Determines last node of list
        actual_node.next_node = new_node

    