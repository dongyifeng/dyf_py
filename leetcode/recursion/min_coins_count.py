'''
给一个正整数数组 arr=【2,7,3，5,3】，每一个数表示一枚硬币，硬币可以重复。再一个 aim=10，求用硬币组成 aim，使用最少的硬币是多个？
'''


def min_coins_count(array, aim):
    return f(array, aim, 0, 0)


def f(array, aim, cur, s):
    if cur == len(array):
        return 1 if s == aim else 0

    return f(array, aim, cur + 1, s) + f(array, aim, cur + 1, s + array[cur])


array = [2, 7, 3, 5, 3]
aim = 10
print(min_coins_count(array, aim))


def min_coins_count2(array, aim):
    return f2(array, aim, 0)


def f2(array, aim, cur):
    if aim < 0: return -1
    if aim == 0: return 0

    # aim > 0 没有硬币可用了
    if cur == len(array):
        return -1

    # aim > 0 并且有硬币
    # 由于返回值有 -1，-1 会干扰求 min
    # min( f2(array, aim, cur + 1), f2(array, aim - array[cur], cur + 1))
    p1 = f2(array, aim, cur + 1)
    p2 = f2(array, aim - array[cur], cur + 1)

    if p1 == -1 and p2 == -1:
        return -1
    elif p1 == -1 or p2 == -1:
        return max(p1, p2 + 1)

    return min(p1, p2 + 1)


def min_coins_count3(array, aim):
    n = len(array)
    dp = [[-1] * (aim + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 0
    for cur in range(n - 1, -1, -1):
        for rest in range(1, aim + 1):
            p1 = dp[cur + 1][rest]
            p2 = dp[cur + 1][rest - array[cur]] if rest - array[cur] >= 0 else -1
            if p1 == -1 and p2 == -1:
                dp[cur][rest] = -1
            elif p1 == -1 or p2 == -1:
                dp[cur][rest] = max(p1, p2 + 1)
            else:
                dp[cur][rest] = min(p1, p2 + 1)

    return dp[0][aim]


array = [2, 7, 3, 5, 3]
aim = 10
print(min_coins_count3(array, aim))

print(min_coins_count2(array, aim))
