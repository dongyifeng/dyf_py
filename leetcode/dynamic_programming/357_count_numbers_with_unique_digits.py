# 357. 计算各个位数不同的数字个数

def count_numbers_with_unique_digits(n):
    dp = [0] * (n + 1)
    dp[1] = 10
    for i in range(2, n + 1):
        dp[i] = 9
        for j in range(i - 1):
            dp[i] *= (9 - j)
    return sum(dp)


def count_numbers_with_unique_digits(n):
    if n == 0: return 1
    res = 10
    for i in range(2, n + 1):
        tmp = 9
        for j in range(i - 1):
            tmp *= (9 - j)
        res += tmp
    return res


# def s(n):
#     tmp = 9
#     res = 1
#     for i in range(n - 1):
#         res *= (tmp - i)
#     return res


# print(s(2))
print(count_numbers_with_unique_digits(2))
