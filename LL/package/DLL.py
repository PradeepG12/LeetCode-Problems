from package import Node

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node 

    def display_forward(self):
        current = self.head
        print(current.prev, end=" -> ")
        while current:
            print(current.data, end="  ->  ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        print(current.next, end=" -> ")
        while current:
            print(current.data, end="  ->  ")
            current = current.prev
        print("None")
