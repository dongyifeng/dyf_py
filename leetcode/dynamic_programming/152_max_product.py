def max_product(nums):
    res = nums[-1]
    n = len(nums)
    for i in range(n):
        tmp = nums[i]
        res = max(tmp, res)
        for j in range(i + 1, n):
            tmp *= nums[j]
            res = max(tmp, res)
    return res


import sys


def max_product2(nums):
    n = len(nums)
    f_max = [-sys.maxsize] * n
    f_min = [sys.maxsize] * n
    f_max[0] = f_min[0] = nums[0]

    for i in range(1, n):
        f_max[i] = max(f_max[i - 1] * nums[i], f_min[i - 1] * nums[i], nums[i])
        f_min[i] = min(f_max[i - 1] * nums[i], f_min[i - 1] * nums[i], nums[i])

    return max(f_max)


def max_product3(nums):
    n = len(nums)
    f_max = f_min = nums[0]

    for i in range(1, n):
        tmp_max = max(f_max * nums[i], f_min * nums[i], nums[i])
        f_min[i] = min(f_max * nums[i], f_min * nums[i], nums[i])
        f_max = tmp_max

    return max(f_max)


print(max_product([2, 3, -2, 4]))
print(max_product([2, 3, -2, -1, 4]))
print(max_product([-3, 0, 1, -2]))
