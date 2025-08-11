from typing import Optional
def TreeNode(): pass
def isValidBST(root: Optional[TreeNode]) -> bool:
    max = float('inf')
    min = float('-inf')
    def helper(root, min, max):
        if not root: return True
        if not min < root.val < max: return False
        return helper(root.left, min, root.val) and helper(root.right, root.val, max)
    return helper(root, min, max)