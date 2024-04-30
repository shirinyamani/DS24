import collections
from collections import deque
class Solution:
    def levelOrder(self, root):
        res = []
        q = deque()
        if root:
            q.append(root)
        while q:
            nodes = []
            for _ in range(len(q)):
                curr = q.popleft()
                nodes.append(curr.val)

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)
            res.append(nodes)
        return res
            