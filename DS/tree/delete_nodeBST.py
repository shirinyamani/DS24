class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_min(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr
        
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            else:
                minnode = find_min(root.right)
                root.val = minnode.val
                root.right = self.deleteNode(root.right, minnode.val)
        return root
        