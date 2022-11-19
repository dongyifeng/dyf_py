def triangle_number(nums):
    nums.sort()
    res = 0
    for i in range(len(nums)):
        a = nums[i]
        for j in range(i + 1, len(nums)):
            b = nums[j]
            tmp = a + b
            for k in range(j + 1, len(nums)):
                if tmp > nums[k]:
                    res += 1
                else:
                    break
    return res


def triangle_number2(nums):
    nums.sort()
    n = len(nums)
    res = 0
    for i in range(n - 2):
        a = nums[i]
        k = i
        for j in range(i + 1, n - 1):
            b = nums[j]
            tmp = a + b
            while k + 1 < n and tmp > nums[k + 1]:
                k += 1

            res += max(k - j, 0)

    return res


def triangle_number2(nums):
    nums.sort()
    n = len(nums)
    res = 0
    for i in range(n - 2):
        a = nums[i]
        k = i
        for j in range(i + 1, n - 1):
            b = nums[j]
            tmp = a + b
            while k + 1 < n and tmp > nums[k + 1]:
                k += 1

            res += max(k - j, 0)

    return res


def triangle_number3(nums):
    nums.sort()
    n = len(nums)
    res = 0
    for i in range(n - 2):
        a = nums[i]
        for j in range(i + 1, n - 1):
            b = nums[j]
            k = find(nums, j + 1, a + b)
            res += max(k - j, 0)

    return res


def find(nums, left, target):
    right = len(nums) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if nums[mid] == target:
            while nums[mid - 1] == target:
                mid -= 1
            return mid - 1
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return right
    # return min(left,len(nums)-1)


# print(triangle_number([2, 2, 3, 4]))
# print(triangle_number([4, 2, 3, 4]))
print(triangle_number2([4, 2, 3, 4]))
print(triangle_number3([4, 2, 3, 4]))

# print(triangle_number([1, 2, 3, 4, 5, 6]))
print(triangle_number2([1, 2, 3, 4, 5, 6]))

print(triangle_number3([1, 2, 3, 4, 5, 6]))
