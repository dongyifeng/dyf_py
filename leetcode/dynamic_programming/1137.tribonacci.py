# 第 N 个泰波那契数

def tribonacci(n):
    if n < 2: return n
    if n == 2: return 1

    t0 = 0
    t1 = 1
    t2 = 1
    for i in range(3, n + 1):
        t_n = t0 + t1 + t2
        t0 = t1
        t1 = t2
        t2 = t_n
    return t_n


print(tribonacci(4))
