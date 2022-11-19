'''
给定一个正整数 n，一个正整数 s（1 <= s <=n）,一个正整数 e（1 <= e <=n）,一个正整数 k （k > 0）

表示从 s 点出发，走 k 步到 e 点，一共有多少走法?

【例子】n = 5；s = 2；e = 4；k = 4

1	2	3	4	5

​	  s		  e

路径1：2 --> 3 --> 4 --> 5 --> 4

路径2：2 --> 3 --> 4 --> 3 --> 4

路径3：2 --> 3 --> 2 --> 3 --> 4

路径4：2 --> 1 --> 2 --> 3 --> 4
'''


def walk_ways(n, e, s, k):
    return process(n, e, k, s)


#
# n 和 e 是常量
# rest 剩余步数
# cur 当前位置
def process(n, e, rest, cur):
    #
    if rest == 0:
        return 1 if cur == e else 0

    if cur == 1:
        return process(n, e, rest - 1, cur + 1)
    if cur == n:
        return process(n, e, rest - 1, cur - 1)
    return process(n, e, rest - 1, cur - 1) + process(n, e, rest - 1, cur + 1)


print(walk_ways(5, 4, 2, 4))


def walk_ways2(n, e, s, k):
    dp = [[-1] * (n + 1) for _ in range(k + 1)]
    return process2(n, e, k, s, dp)


#
# n 和 e 是常量
# rest 剩余步数
# cur 当前位置
def process2(n, e, rest, cur, dp):
    if dp[rest][cur] != -1:
        return dp[rest][cur]

    if rest == 0:
        dp[rest][cur] = 1 if cur == e else 0

    elif cur == 1:
        dp[rest][cur] = process(n, e, rest - 1, cur + 1)
    elif cur == n:
        dp[rest][cur] = process(n, e, rest - 1, cur - 1)
    else:
        dp[rest][cur] = process(n, e, rest - 1, cur - 1) + process(n, e, rest - 1, cur + 1)
    return dp[rest][cur]


print(walk_ways2(5, 4, 2, 4))


def walk_ways3(n, e, s, k):
    dp = [[-1] * (n + 1) for _ in range(k + 1)]

    for i in range(n + 1):
        dp[0][i] = 1 if i == e else 0

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            if j == 1:
                dp[i][j] = dp[i - 1][j + 1]
            elif j == n:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

    return dp[e][s]


print(walk_ways3(5, 4, 2, 4))
