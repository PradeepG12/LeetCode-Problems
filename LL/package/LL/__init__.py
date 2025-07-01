# from package import Node
from ._876_middle_of_ll import middleNode, ListNode
from ._206_reverse_ll import reverseList,disp

# class LL:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
        
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end="  ->  ")
#             current = current.next
#         print("None")
