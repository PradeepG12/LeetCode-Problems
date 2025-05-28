from package import TreeNode, Solution


Node = TreeNode
root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.left = Node(13)
root.right.right = Node(4)

sol = Solution()
print(sol.preorderTraversal(root))
print(sol.inorderTraversal(root))
print(sol.postorderTraversal(root))
