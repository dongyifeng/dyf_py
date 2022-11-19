from functools import cmp_to_key


def lowest_lexicography(strs):
    strs.sort(key=cmp_to_key(lambda x, y: 1 if x + y >= y + x else -1))
    return "".join(strs)


def lowest_lexicography2(strs):
    return permute(strs)


def permute(nums):
    if not nums: return ""
    # 栈：好回溯
    path = []
    # 在一条路径上，节点是否访问过。
    used = [False] * len(nums)
    res = "".join(nums)
    return dfs(nums, len(nums), 0, path, used, res)


def dfs(nums, length, depth, path, used, res):
    # 遍历到根节点
    if depth == length:
        # 数据拷贝，后续遍历会修改path 中的值
        # res.append(path[::])
        return min(res, "".join(path))

    # 所有节点都需要作为开头
    for i in range(length):
        if used[i]: continue
        path.append(nums[i])
        used[i] = True
        res = min(dfs(nums, length, depth + 1, path, used, res), res)
        # 回到 dfs 上一层，状态恢复
        path.pop()
        used[i] = False
    return res


import random


def random_array_generator(max_size, max_value):
    ascii_case = "abcdefghijklmnopqrstuvwxyz"
    return ["".join(random.sample(ascii_case, int(1 + random.random() * max_value))) for _ in
            range(int(random.random() * max_size))]


def check():
    n = 100
    max_value = 5
    max_size = 10

    for _ in range(n):
        strs = random_array_generator(max_size, max_value)
        strs3 = strs[:]
        strs2 = strs[:]

        actual = lowest_lexicography(strs3)
        expect = lowest_lexicography2(strs2)
        if actual != expect:
            print("error:", strs3, strs2, strs, "actual:", actual, "expect:", expect)
    print("Game Over!")


check()
#
# print("KNecx1H")
nums = [ 'a', 'b',  'a',  'b', 'c', 'd']
print( lowest_lexicography(nums))
print( lowest_lexicography2(nums))
