import sys


def min_money_count(arr, aim):
    if aim <= 0: return 0
    dp = [sys.maxsize] * (aim + 1)
    dp[0] = 0

    # for i in arr:
    #     dp[i] = 1
    arr = sorted(arr)
    for i in range(1, aim + 1):
        if dp[i] != sys.maxsize:
            continue
        tmp = dp[i]
        for m in arr:
            if i < m:
                break
            tmp = min(dp[i - m], tmp)
        dp[i] = tmp + 1
    print(dp)
    if dp[-1] >= sys.maxsize:
        return -1
    return dp[-1]


print(min_money_count([5, 2, 3], 20))
print(min_money_count([5, 3], 2))
print(min_money_count([5, 3], 4))
print(min_money_count([5, 2], 6))
