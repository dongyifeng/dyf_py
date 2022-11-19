# coding=utf-8
print '''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:
输入: dividend = 10, divisor = 3
输出: 3

示例 2:
输入: dividend = 7, divisor = -3
输出: -2

说明:
被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
'''

'''
暴力：用加法代替乘法
'''


def divide(dividend, divisor):
    f = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)else -1
    s = 0
    i = 0
    while s <= abs(dividend):
        s += abs(divisor)
        i += 1
    return f * (i - 1)


import math


def divide2(dividend, divisor):
    if dividend > 2147483648: return 2147483647
    if dividend <-2147483648:return 2147483647
    if divisor == 1 or divisor == -1: return divisor * dividend
    f = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)else -1

    mid = abs(dividend) >> 1
    if mid <= 0: return 0
    # print 'mid', mid
    r = 1
    while mid >= abs(divisor):
        r += 1
        t = mid >> 1
        mid = max(mid - t, t)
        # print 'mid', mid

    return r * f


print divide2(1, 2)

# print divide(10, 3)
# print divide2(10, 3)
# #
# print divide(7, -3)
#
# print divide2(7, -3)
#
# print divide(-1, 1)
# print divide2(-1, 1)
#
# print divide2(-2147483648, -1)
