# 486. 预测赢家
def predict_the_winner(nums):
    return dfs(nums, 0, len(nums) - 1, 1) >= 0


def dfs(nums, start, end, turn):
    if start == end:
        return nums[start] * turn
    score_start = nums[start] * turn + dfs(nums, start + 1, end, -turn)
    score_end = nums[end] * turn + dfs(nums, start, end - 1, -turn)
    return max(score_start * turn, score_end * turn) * turn


def predict_the_winner2(nums):
    n = len(nums)
    dp = [[None for _ in range(n)] for _ in range(n)]
    return dfs2(nums, 0, len(nums) - 1, 1, dp) >= 0


def dfs2(nums, start, end, turn, dp):
    if start == end:
        return nums[start] * turn
    if dp[start][end]:
        return dp[start][end]

    score_start = nums[start] * turn + dfs2(nums, start + 1, end, -turn, dp)
    score_end = nums[end] * turn + dfs2(nums, start, end - 1, -turn, dp)
    res = max(score_start * turn, score_end * turn) * turn
    dp[start][end] = res
    return res


print(predict_the_winner2([1, 5, 233, 7]))


def predict_the_winner3(nums):
    n = len(nums)
    dp = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = nums[i]

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
    return dp[0][n - 1] >= 0


print(predict_the_winner3([1, 5, 233, 7]))


def predict_the_winner4(nums):
    n = len(nums)
    dp = [nums[i] for i in range(n)]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            dp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])

    return dp[n - 1] >= 0


print(predict_the_winner4([1, 5, 233, 7]))
print(predict_the_winner4([1, 5, 2]))
