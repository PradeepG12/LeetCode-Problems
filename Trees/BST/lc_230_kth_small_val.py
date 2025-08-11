from typing import Optional
import heapq
def TreeNode(): pass

def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    count = val = 0
    def helper(root):
        nonlocal count
        if not root:
            return
        helper(root.left)
        count += 1
        if count == k: 
            val = root.val
            return val
        helper(root.right)
    helper(root)
    return val
