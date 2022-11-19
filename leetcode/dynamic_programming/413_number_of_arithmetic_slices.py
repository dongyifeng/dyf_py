import sys


def number_of_arithmetic_slices(nums):
    n = len(nums)
    if n < 3: return 0
    nums.append(sys.maxsize)
    sub = nums[1] - nums[0]
    number = 2
    res = 0
    for i in range(2, n):
        if nums[i] - nums[i - 1] == sub:
            number += 1
            continue

        for k in range(3, number + 1):
            res += (number - k + 1)
        sub = nums[i] - nums[i - 1]
        number = 2

    return res


# print(number_of_arithmetic_slices([1, 2, 3, 4]))
# print(number_of_arithmetic_slices([7, 7, 7, 7]))
# print(number_of_arithmetic_slices([3, -1, -5, -9]))
print(number_of_arithmetic_slices([1, 2, 3, 8, 9, 10]))
