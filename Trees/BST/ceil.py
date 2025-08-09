def findceil(root, key):
    ceil = -1
    while root:
        if root.val == key:
            return root.val
        if root.val > key:
            ceil = root.val
            root = root.left
        else:
            root = root.right
    return ceil
