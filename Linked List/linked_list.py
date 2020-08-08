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

    def size_of_linked_list(self):
        return self.num_of_nodes


    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node

    def remove(self, data):
        if self.head is None:
            return

        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        if actual_node is None:
            return

        if previous_node is None:
            self.head = actual_node.next_node
        else:
            previous_node.next_node = actual_node.next_node

test_list = LinkedList()


test_list.insert_at_start({'name':'Taddes', 'age':31})
test_list.insert_at_start({'name':'Sarah', 'age':31})
test_list.insert_at_start({'name':'Karl', 'age':21})
print(test_list.size_of_linked_list())
test_list.traverse()
test_list.remove({'name':'Karl', 'age':21})
print(test_list.size_of_linked_list())
test_list.traverse()