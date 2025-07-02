class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    new_head = None
    lsst = []
    while head:
        lsst.append(head.val)
        head = head.next

    while lsst:
        new_node = ListNode(lsst.pop())
        if not new_head:
            new_head = new_node
            current = new_head
        else:
            current.next = new_node
            current = current.next
    return new_head

def reverseListRecursion(head):

    if head.next is None:
        return head
    new_node = reverseListRecursion(head.next)
    head.next.next = head
    head.next = None
    return new_node

def disp(node):
    while node:
        print(node.val, end=" | ")
        node = node.next
    print()
