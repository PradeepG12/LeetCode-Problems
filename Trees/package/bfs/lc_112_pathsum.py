from typing import Optional
class TreeNode:
    pass
from collections import deque

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    queue = deque([(root, 0)])
    while queue:
        node, total = queue.popleft()
        if not (node.left and node.right):
            return total == total+node.val
        if node.left:
            queue.append(node.left, total+node.val)
        if node.right:
            queue.append(node.right, total+node.val)
    return False