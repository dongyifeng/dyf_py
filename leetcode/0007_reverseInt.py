# coding:utf-8

def reverse(x):
    if x > 2147483647 or x < -2147483648: return 0
    r = 0
    f = 1 if x > 0 else -1
    t = abs(x)
    while t != 0:
        pop = t % 10
        r = r * 10 + pop
        t = int(t / 10)
    r = r * f
    if r > 2147483647 or r < -2147483648: return 0

    return r


print reverse(123)
print reverse(-123)
print reverse(120)
