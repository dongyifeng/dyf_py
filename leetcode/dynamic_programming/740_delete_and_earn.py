def delete_and_earn(nums):
    nums = sorted(nums)

    distinct_nums = []
    num_sum_map = {}
    for num in nums:
        if num not in num_sum_map:
            num_sum_map[num] = 0
            distinct_nums.append(num)
        num_sum_map[num] += num

    nums = distinct_nums

    if len(nums) < 2: return max(nums)

    dp = [0] * len(nums)
    dp[0] = num_sum_map[nums[0]]
    # dp[1] = dp[0] + num_sum_map[nums[1]] if nums[1] != nums[0] + 1 else max(dp[0], num_sum_map[nums[1]])
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            dp[i] = dp[i - 1] + num_sum_map[nums[i]]
        else:
            dp[i] = max(dp[i - 1], dp[i - 2] + num_sum_map[nums[i]])
    return dp[-1]


print(delete_and_earn([2, 3, 4]))
print(delete_and_earn([2, 2, 3, 3, 3, 4]))
print(delete_and_earn([3, 1]))
