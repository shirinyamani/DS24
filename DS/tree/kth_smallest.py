def smallest(root, k):
        #recursive
        ans=[]
        def foo(root):
            # if len(ans)==k: return 
            if root:
                foo(root.left)
                ans.append(root.val)
                foo(root.right)
        foo(root)
        return ans[k-1]

        #iterative
        if not root:
            return 
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right