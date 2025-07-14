from typing import Optional

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

data = [[1,0,1],[0]]

def getDecimalValue(head: Optional[ListNode]):
    num = 0
    while head:
        num = num << 1 | head.val
        head = head.next
    return num
	
def getDecimalValueBrute(head: Optional[ListNode]):
    string = ""
    while head:
        string += str(head.val)
        head = head.next
    print(int(string, 2))
n3 = ListNode(1)
n2 = ListNode(0, n3)
n1 = ListNode(1, n2)
print(getDecimalValue(n1))