from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bstFromPreorder(preorder: List[int]) -> Optional[TreeNode]:
    n = len(preorder)
    root = TreeNode(preorder[0])
    for i in range(1,n):
        helper(root, preorder[i])
    def helper(root, val):
        if root.val > val:
            if not root.left:
                root.left = TreeNode(val)
                return
            helper(root.left, val)
        elif root.val < val:
            if not root.right:
                root.right = TreeNode(val)
                return
            helper(root.right, val)