def dabiao(n):
    if n < 3: return n

    res = x1 = 0
    x2 = 1
    for i in range(n):
        res = x1 + x2
        x1 = x2
        x2 = res

    return res


def get_n(n):
    if n < 1: return 0
    if n < 3: return 1
    return get_n(n - 1) + get_n(n - 2)


def get_count(n):
    if n < 4: return 0

    x1 = res = 1
    x2 = 2
    tmp = 0
    while tmp <= n:
        tmp = x1 + x2
        x1 = x2
        x2 = tmp
        res += 1

    return n - res



#
# print(dabiao(5))
# print(get_n(4))

print(get_count(20))
