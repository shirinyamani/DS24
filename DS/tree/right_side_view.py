import collections

def rightside(root):
    q = collections.deque([root])
    res = []
    while q:
        rightside = None
        for _ in range(len(q)):
            curr = q.popleft()
            if curr:
                rightside = curr
                q.append(curr.left)
                q.append(curr.right)
        if rightside:
            res.append(rightside.val)
    return res
                
                
            