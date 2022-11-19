import sys


def min_path_sum(grid):
    row = len(grid)
    col = len(grid[0])
    matrix = [[sys.maxsize for _ in range(col + 1)] for _ in range(row + 1)]
    matrix[0][1] = 0
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            matrix[i][j] = min(matrix[i - 1][j] + grid[i - 1][j - 1], matrix[i][j - 1] + grid[i - 1][j - 1])
    return matrix[-1][-1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(min_path_sum(grid))
# 7


grid = [[1, 2, 3], [4, 5, 6]]
print(min_path_sum(grid))
# 12
