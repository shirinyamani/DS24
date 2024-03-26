
def missingNumber(nums):
    sorted_num = sorted(nums)
    n = len(sorted_num)

    for i in range(n):
        if sorted_num[i] != i:
            return i
    return n


def missingnum1(nums):
    n = len(nums)
    nums = set(nums)

    for num in range(n+1):
        if num not in nums:
            return num


print(missingnum1([7,6,5,3,2,1, 0]))
