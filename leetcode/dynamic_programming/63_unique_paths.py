def unique_paths(obstacle_grid):
    m = len(obstacle_grid)
    n = len(obstacle_grid[0])
    matrix = [[0] * (n + 1)] * (m + 1)
    matrix[1][1] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if obstacle_grid[i - 1][j - 1] == 1:
                matrix[i][j] = 0
            else:
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
    return matrix[-1][-1]


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(unique_paths(obstacleGrid))
obstacleGrid = [[0, 1], [0, 0]]
print(unique_paths(obstacleGrid))
