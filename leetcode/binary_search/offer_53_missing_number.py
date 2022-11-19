def missing_number(nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if nums[mid] == mid:
            left = mid + 1
        else:
            right = mid - 1
    return left


print(missing_number([0, 1, 3]))
print(missing_number([0, 1, 2, 3, 4, 5, 6, 7, 9]))
