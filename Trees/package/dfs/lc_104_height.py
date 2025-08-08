from typing import Optional
class TreeNode:
    pass

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

def isBalancedBrute(root: Optional[TreeNode]) -> bool:
    def __helper(root):
        if not root:
            return 0, True
        l_height, l_balanced = __helper(root.left)
        r_height, r_balanced = __helper(root.right)
        if not l_balanced or not r_balanced:
            return 0, False
        if abs(l_height - r_height) > 1:
            return 0, False
        return __helper(max(l_height, r_height)+1, True)
    _, result = __helper(root)
    return result

def isBalanced(root: Optional[TreeNode]) -> bool:
    def _helper(root):
        if not root: return 0
        left = _helper(root.left)
        right = _helper(root.right)
        if (left or right) == -1: return -1
        if abs(left-right)>1: return -1
        return max(left, right) + 1
    return _helper(root) != -1

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    maxi = 0
    def _helper(root):
        nonlocal maxi
        if not root: return 0
        left = _helper(root.left)
        right = _helper(root.right)
        maxi = max(left+right, maxi)
        return max(left, right)+1
    _helper(root)
    return maxi