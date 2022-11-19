def special_array(nums):
    nums.sort()
    n = len(nums)
    i = 0
    x = 0
    while x <= n:
        while i < n:
            if nums[i] >= x:
                break
            i += 1
        if x == n - i:
            return x
        if x > n - i:
            return -1
        x += 1
    return -1


def find(nums, start, k):
    end = len(nums) - 1
    mid = 0
    while start < end:
        mid = start + ((end - start) >> 1)
        if nums[mid] < k:
            start = mid + 1
        if nums[mid] >= k:
            end = mid - 1
    print(start, mid, end)


def find2(nums, k):
    for i in range(len(nums)):
        if nums[i] >= k:
            return i


# print(special_array([3, 5]))
# print(special_array([0, 0]))
# print(special_array([0, 4, 3, 0, 4]))
# print(special_array([3, 6, 7, 7, 0]))

# print(find([3, 5], 0, 3))
# print(find([0, 0], 0, 0))
# print(find([0, 0, 3, 4, 4], 0, 0))

print(find([0, 0, 3, 4, 4], 0, 2))
print(find([0, 0, 3, 4, 4], 0, 3))
# print(find([0, 0, 3, 4, 4], 0, 4))

print("-" * 10)

# print(find2([3, 5], 3))
# print(find2([0, 0],  0))
# print(find2([0, 0, 3, 4, 4],  0))
print(find2([0, 0, 3, 4, 4], 2))
print(find2([0, 0, 3, 4, 4], 3))
# print(find2([0, 0, 3, 4, 4],  4))
