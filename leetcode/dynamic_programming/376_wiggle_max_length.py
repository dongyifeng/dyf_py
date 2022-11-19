def wiggle_max_length(nums):
    n = len(nums)
    if n < 2: return n
    pre_diff = nums[0] - nums[1]
    res = 2 if pre_diff != 0 else 1
    for i in range(2, n):
        diff = nums[i - 1] - nums[i]
        if (diff > 0 and pre_diff <= 0) or (diff < 0 and pre_diff >= 0):
            res += 1
            pre_diff = diff
    return res


def wiggle_max_length2(nums):
    n = len(nums)
    if n < 2: return n
    up = [0] * n
    down = [0] * n
    down[0] = up[0] = 1

    for i in range(1, n):
        if nums[i] == nums[i - 1]:
            up[i] = up[i - 1]
            down[i] = down[i - 1]
            continue
        if nums[i] > nums[i - 1]:
            up[i] = down[i - 1] + 1
            down[i] = down[i - 1]
            continue
        down[i] = up[i - 1] + 1
        up[i] = up[i - 1]

    return max(up[n - 1], down[n - 1])


def wiggle_max_length3(nums):
    n = len(nums)
    if n < 2: return n
    up = down = 1

    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            up = down + 1
            continue
        if nums[i] < nums[i - 1]:
            down = up + 1

    return max(up, down)


print(wiggle_max_length3([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(wiggle_max_length([1, 2]))
# print(wiggle([2, 2]))
# print(wiggle_max_length([1]))
# print(wiggle_max_length([1, 2, 1, 2, 1, 2]))
# print(wiggle_max_length([2, 1, 2, 1, 2, 2, 1]))
# print(wiggle_max_length([1, 2, 3, 4, 5]))
print(wiggle_max_length3([1, 1, 7, 4, 9, 2, 5]))
print(wiggle_max_length3([3, 3, 3, 2, 5]))
