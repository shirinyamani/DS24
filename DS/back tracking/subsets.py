class Solution:
    def subsets(self, nums):
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            root = nums[i]
            #deision to include
            subset.append(root)
            dfs(i + 1)
            #decision not to include
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res
        



