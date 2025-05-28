from typing import List, Optional

from .common import TreeNode


class Solution:
    def preorderTraversal(self, root) -> List[int]:
        if root is None:
            return []
        output = [root.val]
        output += self.preorderTraversal(root.left)
        output += self.preorderTraversal(root.right)
        return output

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output = []
        output += self.inorderTraversal(root.left)
        output.append(root.val)
        output += self.inorderTraversal(root.right)
        return output

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
