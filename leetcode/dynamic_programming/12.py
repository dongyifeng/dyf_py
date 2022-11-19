# 不是连续子数组
def s(nums):
    n = len(nums)
    res = sum(nums)
    nums.sort()
    for i in range(1, n):
        t = n
        k = (t - (i + 1)) * i + 1
        h = 0
        for j in range(k, 0, -1):
            tmp = (t - (i + 1)) * i + 1
            if tmp < 0: break
            res += nums[h] * tmp
            t -= 1
            h += 1
    return res


def sum_subarray_mins(nums):
    n = len(nums)
    res = 0
    for i in range(1, n + 1):
        for j in range(n - i + 1):
            res += min(nums[j: j + i])
    return res % (10 ** 9 + 7)


def sum_subarray_mins2(nums):
    n = len(nums)
    res = 0
    for i in range(1, n + 1):
        array = nums[0: i]
        last_min = min(array)
        for j in range(1, n - i + 1):
            res += last_min

            array.append(nums[j])
            array.remove(array[0])

            if nums[j+i-1] < last_min:
                last_min = nums[j]
                continue
            if nums[j-1] == last_min:
                last_min = min(array)


    return res % (10 ** 9 + 7)


print(sum_subarray_mins2([11, 81, 94, 43, 3]))
print(sum_subarray_mins2([3, 1, 2, 4]))
