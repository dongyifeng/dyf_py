def factorial_sum(n):
    res = 0
    factorial = 1
    for i in range(1, n):
        if res == n: return True
        if res > n: return False
        factorial *= i
        res += factorial


print(factorial_sum(9))
print(factorial_sum(10))
