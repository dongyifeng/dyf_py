# 来自去哪网
# 给定一个 arr，里面的数字都是 0- 9，你可以随意使用 arr 中的数字，哪怕打乱顺序也行
# 请拼出一个能被 3 整除的，最大的数组，用 str 形式返回

def max_nums(nums):
    num_sum = sum(nums)
    if num_sum % 3 == 2:
        sub_num = [item for item in nums if item % 3 == 2]
        if sub_num:
            nums.remove(min(sub_num))
        else:
            tmp = sorted([item for item in nums if item % 3 == 1])[:2]
            nums.remove(tmp[0])
            nums.remove(tmp[1])
    elif num_sum % 3 == 1:
        sub_num = [item for item in nums if item % 3 == 1]
        if sub_num:
            nums.remove(min(sub_num))
        else:
            tmp = sorted([item for item in nums if item % 3 == 2])[:2]
            nums.remove(tmp[0])
            nums.remove(tmp[1])

    if sum(nums) == 0:
        return 0

    nums.sort(reverse=True)
    return "".join([str(item) for item in nums])


print(max_nums([0, 0, 7]))
