from typing import Optional
class TreeNode:
    pass

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1
