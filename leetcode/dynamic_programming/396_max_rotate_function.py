# 396. 旋转函数
import sys


def max_rotate_function(nums):
    n = len(nums)
    res = -sys.maxsize

    for i in range(n):
        tmp = 0
        for j in range(n):
            tmp += j * nums[j - i]
        res = max(res, tmp)
    return


def max_rotate_function2(nums):
    n = len(nums)
    nums_sum = sum(nums)

    res = b = sum([i * nums[i] for i in range(n)])
    last_index = -1
    for i in range(1, n):
        b = b + nums_sum - n * nums[last_index]
        last_index -= 1
        res = max(res, b)
    return res


print(max_rotate_function2([4, 3, 2, 6]))
