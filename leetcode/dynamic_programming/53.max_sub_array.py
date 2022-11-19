def max_sub_array(nums):
    sub_array = [None] * (len(nums) + 1)
    sub_array[0] = 0
    for i in range(len(nums)):
        sub_array[i + 1] = max(sub_array[i] + nums[i], nums[i])
    return max(sub_array[1::])


print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
