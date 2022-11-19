'''
现有 n1 + n2 种面值的硬币，其中前 n1 种为普通币，可以取任意枚，后 n2 种为纪念币，每种最多只能取一枚，每种硬币有一个面值，问能用多少种方法拼出 m 个面值？
'''


def coins1(arr, aim):
    if not arr: return
    dp = [[0] * (aim + 1) for _ in range(len(arr))]

    for i in range(len(arr)):
        dp[i][0] = 1

    for i in range(1, aim + 1):
        if arr[0] * i < aim + 1:
            dp[0][arr[0] * i] = 1

    for i in range(1, len(arr)):
        for j in range(1, aim + 1):
            dp[i][j] = dp[i - 1][j]
            dp[i][j] += dp[i][j - arr[i]] if (j - arr[i]) >= 0 else 0

    return dp


def coins2(arr, aim):
    if not arr: return
    dp = [[0] * (aim + 1) for _ in range(len(arr))]

    for i in range(len(arr)):
        dp[i][0] = 1

    if arr[0] <= aim:
        dp[0][arr[0]] = 1

    for i in range(1, len(arr)):
        for j in range(1, aim + 1):
            dp[i][j] = dp[i - 1][j]
            dp[i][j] += dp[i - 1][j - arr[i]] if j - arr[i] >= 0 else 0

    return dp


def money_ways(arbitrary, only_one, money):
    if money < 0: return 0
    if not arbitrary and not only_one:
        return 1 if money == 0 else 0

    dp_1 = coins1(arbitrary, money)
    dp_2 = coins2(only_one, money)
    n_1 = len(arbitrary) - 1
    n_2 = len(arbitrary) - 1
    if not dp_1: return dp_2[n_2][money]
    if not dp_2: return dp_1[n_1][money]

    res = 0
    for i in range(money + 1):
        res += dp_1[n_1][i] * dp_1[n_2][money - i]
    return res
