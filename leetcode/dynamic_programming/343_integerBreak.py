def integer_break(n):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        max_value = 0
        for j in range(1, i):
            max_value = max(max_value, max(j * (i - j), j * dp[i - j]))
        dp[i] = max_value
    return dp[-1]


def integer_break2(n):
    if n <= 2: return 1

    res = 0
    for i in range(1, n):
        res = max(res, max(i * (n - i), i * integer_break2(n - i)))
    return res


def integer_break3(n):
    if n <= 2: return 1
    return max(max(i * (n - i), i * integer_break3(n - i)) for i in range(1, n))


# print(data)
# print(get_left_node(data))
# print(process(2))
print(integer_break(3))
print(integer_break2(4))
# print(integer_break(4))


for i in range(2, 100):
    a = integer_break(i)
    b = integer_break2(i)
    c = integer_break3(i)

    print(i)
    if a != b or a != c:
        print(i, a, b, c)
