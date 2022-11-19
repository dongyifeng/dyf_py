# coding=utf-8
'''
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
'''


def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    return x ** n


'''
暴力
'''


def myPow2(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    x = x if n > 0 else 1.0 / x
    s = x
    for i in range(abs(n) - 1):
        s *= x
    return s


'''
折半

原理：x ^(n+m) = x^n * x^m
将指乘积转化为加法
'''


def myPow3(x, n):
    if n == 0: return 1.0
    memo = {1: x}
    res = myPow4(x, abs(n), memo)
    return res if n > 0 else 1.0 / res


def myPow4(x, n, memo):
    if n in memo: return memo[n]
    mid = n >> 1

    l = myPow4(x, mid, memo)
    memo[mid] = l
    r = myPow4(x, n - mid, memo)
    memo[n - mid] = r
    return l * r


def myPow5(x, n):
    ans = 1.0
    # 贡献的初始值为 0
    x_contribute = x
    while n>0:
        if n % 2==1:
            # 如果 n 二进制表示的最低位为 1，那么需要计入贡献
            ans*=x_contribute

        # 将贡献不断地平方
        x_contribute*=x_contribute
        # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
        n = n>>1
    return ans

# print myPow2(2, 10)
#
# print myPow2(2.1, 3)
#
# print myPow2(2, -2)

# print myPow2(0.0001, 2147483647)

# print 0.0001 ** 2147483647

print(myPow5(2, 10))
import math

print(math.pow(2, 10))
#
# print(myPow3(2.1, 3))
#
# print(myPow3(2, -2))

# print myPow2(0.0001, 2147483647)
