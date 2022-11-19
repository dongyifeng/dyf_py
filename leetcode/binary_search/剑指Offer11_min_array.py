def min_array(numbers):
    if len(numbers) == 1: return numbers[0]
    # 没有旋转
    if numbers[0] < numbers[-1]:
        return numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            return numbers[i]
    return numbers[0]


import sys


def min_array2(numbers):
    left = 0
    right = len(numbers) - 1
    while left < right:
        mid = left + ((right - left) >> 1)
        if numbers[mid] < numbers[right]:
            right = mid
        elif numbers[mid] > numbers[right]:
            left = mid + 1
        else:
            right -= 1

    return numbers[left]


# print(min_array2([3, 4, 5, 1, 2]))
# print(min_array2([2, 2, 2, 0, 1]))
# print(min_array2([3, 3, 3, 1]))
# print(min_array2([3, 3, 1, 3]))
# print(min_array2([3, 1, 1]))
print(min_array2([10, 1, 10, 10, 10]
                 ))
