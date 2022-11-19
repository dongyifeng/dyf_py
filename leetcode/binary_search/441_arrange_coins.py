def arrange_coins(n):
    if n == 1: return n
    tmp = 1
    sub = 2
    while tmp <= n:
        tmp += sub
        sub += 1
    return sub - 2


import math


# 数学公式
def arrange_coins2(n):
    return int((math.sqrt(1 + 8 * n) - 1) / 2)


# 二分查找
def arrange_coins3(n):
    if n == 1: return n
    right = n
    left = 1

    while left <= right:
        mid = (left + right) >> 1
        tmp = mid * (mid + 1) >> 1
        if tmp == n:
            return mid
        if n > tmp:
            left = mid + 1
        else:
            right = mid - 1
    return right


print(arrange_coins(3))
print(arrange_coins(2))
print(arrange_coins(5))
print(arrange_coins(8))

print("-" * 100)

print(arrange_coins2(3))
print(arrange_coins2(2))
print(arrange_coins2(5))
print(arrange_coins2(8))

print("-" * 100)

print(arrange_coins3(3))
print(arrange_coins3(2))
print(arrange_coins3(5))
print(arrange_coins3(8))
