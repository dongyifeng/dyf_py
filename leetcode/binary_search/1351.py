def count_negatives(grid):
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] < 0:
                res += 1
    return res


def count_negatives2(grid):
    res = 0
    m = len(grid[0])
    count = 0
    last_count = 0
    for i in range(len(grid)):
        count = len([j for j in range(m - count - 1, -1, -1) if grid[i][j] < 0]) + last_count
        res += count
        last_count = count

    return res


def count_negatives3(grid):
    m = len(grid[0])
    res = 0
    for i in range(len(grid)):
        left = 0
        right = m - 1
        pos = -1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if grid[i][mid] < 0:
                pos = mid
                right = mid - 1
            else:
                left = mid + 1
        if pos != -1:
            res += m - pos
    return res


print(count_negatives2([[4, 3, 2, 1], [4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
print(count_negatives2([[1, -1], [-1, -1]]))
