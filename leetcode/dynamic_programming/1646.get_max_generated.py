# 获取生成数组中的最大值

def get_maximum_generated(n):
    if n < 2: return n
    nums = [None] * (n + 1)
    nums[0] = 0
    nums[1] = 1

    max_value = 1
    for i in range(2, n + 1):
        if i % 2 == 0:
            nums[i] = nums[int(i / 2)]
        else:
            nums[i] = nums[int((i - 1) / 2)] + nums[int((i + 1) / 2)]
        max_value = max(max_value, nums[i])
    return max_value


print(get_maximum_generated(7))
print(get_maximum_generated(2))
print(get_maximum_generated(3))
