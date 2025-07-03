from typing import Optional
# from ._206_reverse_ll import ListNode, disp

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def disp(node):
    while node:
        print(node.val, end=" | ")
        node = node.next
    print()

def hasCyclebrute(head: Optional[ListNode]) -> bool:
    st = set()
    i=0
    while head:
        print(i)
        i+=1
        if head in st:
            print("True")
        st.add(head)
        head = head.next
    print("False")


def hasCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            return True
    return False



n6 = ListNode(6)
n5 = ListNode(5, n6)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 =ListNode(1, n2)
disp(n1)
hasCycle(n1)
hasCyclebrute(n1)
