
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def preOrder(node):
    if not node:
        return
    print(node.val, end=' ')
    preOrder(node.left)
    preOrder(node.right)

def inOrder(node):
    if not node:
        return
    preOrder(node.left)
    print(node.val, end=' ')
    preOrder(node.right)

def postOrder(node):
    if not node:
        return
    preOrder(node.left)
    preOrder(node.right)
    print(node.val, end=' ')

Node = TreeNode
root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.left = Node(13)
root.right.right = Node(4)

# preOrder(root)
# print()
# inOrder(root)
# print()
# postOrder(root)

# def path_sum(node, target):
#     if not node:
#         return
#     if not (node.left or node.right):
#         return node.val == target
    
#     remainder = target - node.val
#     return path_sum(node.left, remainder) or path_sum(node.right, remainder) 

# # print(path_sum(root, 22))

# def find_leaf(node) -> int:
#     if node is None:
#         return 0 
#     if not node.left and not node.right:
#         return 1
#     return (find_leaf(node.left) + find_leaf(node.right))
# print(find_leaf(root))


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)  
        print(node.val, end=" | ")
        self.in_order(node.right)

    def pre_order(self, node):
        if node is None: return
        print(node.val, end=" | ")
        self.pre_order(node.left)
        self.pre_order(node.right)

    def post_order(self, node):
        if node is None: return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.val, end=" | ")

    def bfs(self, node):

        from collections import deque

        queue = deque()
        queue.append(node)
        while queue:
            curr_node = queue.popleft()
            print(curr_node.val , end=" | ")
            if left_node := curr_node.left:
                queue.append(left_node)
            if right_node := curr_node.right:
                queue.append(right_node)



root = Tree(val=10)
root.left = Tree(val=20)
root.right = Tree(val=30)
root.right.left = Tree(val=40)
"""
root.in_order(root)
print()
root.pre_order(root)
print()
root.post_order(root)
print()
root.bfs(root)
"""