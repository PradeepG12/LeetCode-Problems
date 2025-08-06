from typing import Optional, List as ListNode

data = [[1,2,2,1],[1,2],[5,4,3,4,5]]

def isPalindromeBrute(head: Optional[ListNode]) -> bool:
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    i, j = 0, len(arr)-1
    while i<j:
        if arr[i] != arr[j]:
            return False
        i += 1
        j -= 1
    return True

def isPalindrome(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    rev = reverse(slow)
    while head and rev:
        if head.val != rev.val:
            return False
        head = head.next
        rev = rev.next
    return True

def reverse(node):
    if not node.next:
        return node
    new_node = reverse(node.next)
    node.next.next = node
    node.next = None
    return new_node