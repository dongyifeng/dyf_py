def single_non_duplicate(nums):
    if len(nums) == 1: return nums[0]

    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + ((right - left) >> 1)
        if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]: return nums[mid]

        even = mid % 2 == 0
        if even:
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid - 2

        if not even:
            if nums[mid] == nums[mid - 1]:
                left = mid + 1
            else:
                right = mid - 1

    return nums[left]


print(single_non_duplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(single_non_duplicate([1, 1, 3, 3, 4, 4, 8, 9, 9]))
print(single_non_duplicate([3, 3, 7, 7, 10, 11, 11]))
print(single_non_duplicate([10, 11, 11]))
