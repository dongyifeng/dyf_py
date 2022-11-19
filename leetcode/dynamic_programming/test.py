import sys


def t(nums):
    level = len(nums)
    max_len = len(nums[-1])
    array = [sys.maxsize] * (max_len + 1)
    array[0] = 0
    for i in range(level):
        tmp = [sys.maxsize] * (max_len + 1)
        for j in range(1, len(nums[i]) + 1):
            tmp[j] = min(array[j], array[j - 1]) + nums[i][j - 1]
        array = tmp
    return min(array)


print(t([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
