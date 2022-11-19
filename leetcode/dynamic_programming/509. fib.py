# 斐波那契数

def fib2(n):
    if n < 2: return n
    return fib2(n - 1) + fib2(n - 2)


def fib(n):
    if n < 2: return n
    num1 = 0
    num2 = 1
    res = 0
    for i in range(1, n):
        res = num1 + num2
        num1 = num2
        num2 = res
    return res


print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
