def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) >> 1
        if nums[mid] == target: return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


print(search([-1, 0, 3, 5, 9, 12], 9))
print(search([-1, 0, 3, 5, 9, 12], 2))
