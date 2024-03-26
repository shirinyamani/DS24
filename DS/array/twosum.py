def two_sum(nums, target):
    res = []
    for i, _ in enumerate(nums):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                res.extend([i, j])

    return res 


def pair_sum(l, k):
    if len(l) <2:
        return
    
    seen = set()
    output = set()

    for num in l:
        target = k-num
    
        if target not in seen:
            seen.add(num)
        else:
            output.add( ((min(num, target)), max(num,target)))

    #return len(output)
    print ('\n'.join(map(str, list(output))))

print(two_sum([2,4,3,2], 5))
print(pair_sum([1,3,3,2,2], 4))