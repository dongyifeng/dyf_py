def run(nums):
    n = len(nums)
    if n < 2: return max(nums)
    array = [0] * n
    array[0] = nums[0]
    array[1] = max(nums[0], nums[1])
    for i in range(2, n):
        array[i] = max(array[i - 1], array[i - 2] + nums[i])
    print(array)
    return array[-1]


def run2(nums):
    n = len(nums)
    if n < 2: return max(nums)
    tmp1 = nums[0]
    tmp2 = max(nums[0], nums[1])
    for i in range(2, n):
        tmp = max(tmp2, tmp1 + nums[i])
        tmp1 = tmp2
        tmp2 = tmp
    return tmp2


def run3(nums):
    n = len(nums)
    if n < 2: return max(nums)
    return max(run(nums[1:]), run(nums[:n - 1]))


print(run3([2, 3, 2]))
# print(run3([2, 7, 9, 3, 1]))
