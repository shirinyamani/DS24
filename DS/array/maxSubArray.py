
def maxSubArray(nums):
    if len(nums) == 0:
        return 0
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(current_sum, max_sum)

    return max_sum


#which indexes causes this sum

def max_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    start_index = 0
    end_index = 0
    current_start = 0

    for i in range(1,len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            current_start = i
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start_index = current_start
            end_index = i

    return max_sum, nums[start_index:end_index + 1]



print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([4,5,6,-2,-4,8]))