def combinationSum(candidates, target):
    res = []
    def dfs(i, curr, total):
        if total == target:
            res.append(curr.copy())
            return
        
        if i >= len(candidates) or total > target:
            return

        #decision to include the node
        curr.append(candidates[i])
        dfs(i, curr, total + candidates[i])

        #decision not to include
        curr.pop()
        dfs(i + 1, curr, total)
    dfs(0, [], 0)
    return res
