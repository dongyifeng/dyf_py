def min_path_sum1(m):
    if not m:
        return 0
    row = len(m)
    col = len(m[0])

    dp = [[0] * col for _ in range(row)]
    dp[0][0] = m[0][0]
    for i in range(1, row):
        dp[i][0] += dp[i - 1][0] + m[i][0]

    for i in range(1, col):
        dp[0][i] += dp[0][i - 1] + m[0][i]

    for i in range(1, row):
        for j in range(1, col):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + m[i][j]

    for i in range(row):
        print(dp[i])
    return dp[-1][-1]


def min_path_sum2(m):
    row = len(m)
    col = len(m[0])

    more = max(row, col)
    less = max(row, col)
    row_more = more == row

    arr = [0] * less
    arr[0] = m[0][0]
    for i in range(1, less):
        arr[i] = arr[i - 1] + (m[0][i] if row_more else m[i][0])

    for i in range(1, more):
        arr[0] += (m[i][0] if row_more else m[0][i])
        for j in range(1, less):
            arr[j] = min(arr[j - 1], arr[j]) + (m[i][j] if row_more else m[j][i])
    return arr[-1]


print(min_path_sum1([[1, 3, 5, 9],
                     [8, 1, 3, 4],
                     [5, 0, 6, 1],
                     [8, 8, 4, 0]]))

print(min_path_sum2([[1, 3, 5, 9],
                     [8, 1, 3, 4],
                     [5, 0, 6, 1],
                     [8, 8, 4, 0]]))
