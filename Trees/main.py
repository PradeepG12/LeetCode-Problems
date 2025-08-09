from package import TreeNode, maxDepth
from BST import findceil


# Node = TreeNode
# root = Node(5)
# root.left = Node(4)
# root.right = Node(8)
# root.left.left = Node(11)
# root.left.left.left = Node(7)
# root.left.left.right = Node(2)
# root.right.left = Node(13)
# root.right.right = Node(4)

# sol = Solution()
# print(sol.preorderTraversal(root))
# print(sol.inorderTraversal(root))
# print(sol.postorderTraversal(root))
# d = maxDepth(root)
# print(d)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(13)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(2)
root.left.left.right = TreeNode(4)
root.left.right = TreeNode(6)
root.left.right.right = TreeNode(9)
root.right.left = TreeNode(11)
root.right.right = TreeNode(14)

print(findceil(root,12))
print(findceil(root,14))
