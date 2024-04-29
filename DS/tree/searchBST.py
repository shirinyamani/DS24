def searchBST(root, val):
    if not root:
        return None
    if root == val:
        return root
    
    elif val < root:
        return searchBST(root.left, val)
    
    else:
        return searchBST(root.right, val)