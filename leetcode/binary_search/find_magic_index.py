def find_magic_index(nums):
    for i in range(len(nums)):
        if i == nums[i]: return i
    return -1


def find_magic_index2(nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if nums[mid] == mid: return mid
        if nums[mid] < mid:
            right = mid - 1
        else:
            left = mid + 1
    return -1


print(find_magic_index2([0, 2, 3, 4, 5]))
# print(find_magic_index2([1, 1, 1]))
# print(find_magic_index2([0, 0, 1]))
