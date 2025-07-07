from package import DLL, ReverseDll

# dll = DLL()
# dll.display_forward()
# dll.display_backward()
# rdll = ReverseDll()
# rdll.append(11)
# rdll.append(22)
# rdll.append(33)
# rdll.append(44)
# rdll.display_forward()
# rdll.reverse()
# rdll.display_forward()

from package import middleNode, ListNode,reverseList, disp, reverseListRecursion, detectCycle
node = ListNode
n6 = node(6)
n5 = node(5, n6)
n4 = node(4, n5)
n3 = node(3, n4)
n2 = node(2, n3)
n1 =node(1, n2)
disp(n1)
# disp(reverseList(n1))
# disp(reverseListRecursion(n1))

n6.next = n3
print(detectCycle(n1).val)