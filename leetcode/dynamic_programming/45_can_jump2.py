def jump(nums):
    n = len(nums)
    if n <= 1: return 0

    inverted_index = [[] for _ in range(n)]
    for i in range(n - 1):
        for j in range(1, nums[i] + 1):
            if i + j < n: inverted_index[i + j].append(i)

    min_distance = [0] * n
    for i in range(1, n):
        min_distance[i] = min([min_distance[j] + 1 for j in inverted_index[i]])

    return min_distance[-1]


print(jump([2, 3, 1, 1, 4]))
print(jump([2, 1]))
