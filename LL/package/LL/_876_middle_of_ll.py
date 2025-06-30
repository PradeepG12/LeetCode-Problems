from typing import Optional
"""head = [1,2,3,4,5]"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    i = j = head
    while j and j.next:
        i = i.next
        j = j.next.next
    return i

