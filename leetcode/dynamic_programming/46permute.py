def permute(nums):
    if not nums: return [[]]
    path = []
    used = [False] * len(nums)
    res = set()
    return dfs(nums, len(nums), 0, path, used, res)


def dfs(nums, length, depth, path, used, res):
    if depth == length:
        res.add(tuple(path[::]))
        return

    for i in range(length):
        if used[i]: continue
        path.append(nums[i])
        used[i] = True
        dfs(nums, length, depth + 1, path, used, res)
        path.pop()
        used[i] = False
    return res


for line in permute([1, 1, 2, 3]):
    print(line)
