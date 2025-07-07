# from ._141_find_loop import ListNode


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detectCycleBrute(head):
    visited = {}
    i = 0
    while head:
        print(visited," i ",i)
        if head in visited:
            return visited[head]
        visited[head] = i
        head = head.next
        i += 1
    return None


def detectCycle(head):
    muyal , aamai= head, head
    while muyal and muyal.next:
        aamai = aamai.next
        muyal = muyal.next.next
        if muyal == aamai:
            break
    aamai = head
    while muyal != aamai:
        muyal = muyal.next
        aamai = aamai.next
    return muyal
