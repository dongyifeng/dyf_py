import sys

def target_indices(nums, target):
    nums.sort()
    nums.insert(0, -sys.maxsize)
    nums.append(sys.maxsize)
    print(nums)
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if nums[mid] == target:
            break
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    if nums[mid] != target:
        return []

    res = set([mid - 1])
    i = mid + 1
    j = mid - 1

    while True:
        if nums[i] != target and nums[j] != target:
            break
        if nums[i] == target:
            res.add(i - 1)
            i += 1
        if nums[j] == target:
            res.add(j - 1)
            j -= 1

    return sorted(res)


print(target_indices([1, 2, 5, 2, 3], 2))
print(target_indices([1, 2, 5, 2, 3], 3))
print(target_indices([1, 2, 5, 2, 3], 5))
print(target_indices([1, 2, 5, 2, 3], 4))

print(target_indices(
    [72, 55, 15, 4, 92, 31, 11, 56, 32, 26, 77, 76, 58, 19, 76, 60, 84, 57, 4, 57, 37, 95, 97, 68, 43, 90, 87, 23, 46,
     33, 66, 5, 31, 42, 30, 99, 50, 68, 86, 8, 17, 10, 50, 41, 30, 87, 59, 81, 73, 44, 93, 81, 17, 70, 15, 6, 72, 79, 1,
     52, 83, 12, 66, 44, 90, 65, 53, 34, 39, 73, 11, 98, 61, 28, 59, 10, 100, 59, 56, 39, 47, 40, 1, 73, 88, 2, 40, 70,
     22, 91, 43, 47, 74, 97, 16, 72, 95, 93, 31, 76]
    , 1))

[72, 55, 15, 4, 92, 31, 11, 56, 32, 26, 77, 76, 58, 19, 76, 60, 84, 57, 4, 57, 37, 95, 97, 68, 43, 90, 87, 23, 46, 33,
 66, 5, 31, 42, 30, 99, 50, 68, 86, 8, 17, 10, 50, 41, 30, 87, 59, 81, 73, 44, 93, 81, 17, 70, 15, 6, 72, 79, 1, 52, 83,
 12, 66, 44, 90, 65, 53, 34, 39, 73, 11, 98, 61, 28, 59, 10, 100, 59, 56, 39, 47, 40, 1, 73, 88, 2, 40, 70, 22, 91, 43,
 47, 74, 97, 16, 72, 95, 93, 31, 76]
1
