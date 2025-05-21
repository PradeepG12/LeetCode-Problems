from package import DLL

""" none <- 1 <-> 2 <-> 3 <-> 4 -> none """

class ReverseDll(DLL):
    def reverse(self):
        current = self.head
        print("Gok Gok",current.data)
        prev_node = None

        while current:
            prev_node = current.prev
            current.prev = current.next
            current.next = prev_node
            current = current.prev
        
        if prev_node:
            self.head = prev_node.prev