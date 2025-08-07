from typing import Optional, List
from collections import deque

class TreeNode:
    pass

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    queue = deque([root])
    result = []
    while queue:
        current_level = len(queue)
        temp = []
        for _ in range(current_level):
            node = queue.popleft()
            temp.append(node.val)
            if new_node := node.left:
                queue.append(new_node)
            if new_node := node.right:
                queue.append(new_node)
        if temp: result.append(temp)
    return result
