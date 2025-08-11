from typing import Optional
class TreeNode: pass

def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root: return root
    def helper(root):
        if not (root.left and root.right): return None
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            left_node = root.left
            rights_last_left = find_lastleft(root.right)
            rights_last_left.left = left_node
            return root.right
    
    def find_lastleft(node):
        while node and node.left:
                node = node.left
        return node
    
    head = root
    if root.val == key:
        root = helper(root)
        return root
    while root:
        if root.val > key: 
            if root.left and root.left.val == key:
                root.left = helper(root.right)
                break
            root = root.left
        else: 
            if root.right and root.right.val == key:
                root.right = helper(root.right)
                break
            root = root.right
    return head
