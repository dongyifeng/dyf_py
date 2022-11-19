# coding:utf-8


# import numpy as np

import sys


def median(data):
    n = len(data)
    if n % 2 == 0:
        return (data[int(n / 2)] + data[int(n / 2) - 1]) / 2
    return data[int(n / 2)]


def findMedianSortedArrays(num1, num2):
    i = j = l = r = 0
    n = len(num1) + len(num2)
    num1.append(sys.maxsize)
    num2.append(sys.maxsize)

    while i < len(num1) and j < len(num2):
        r, l = l, r
        if num1[i] < num2[j]:
            r = num1[i]
            i += 1
        elif num1[i] >= num2[j]:
            r = num2[j]
            j += 1

        if (i + j - 1) == int(n / 2):
            return (r + l) / 2 if n % 2 == 0 else r


# print(median([1, 2, 3]))
# print(median([1, 2, 3, 4]))
#
# print(findMedianSortedArrays([1, 3], [2]))

print(findMedianSortedArrays([1, 2], [3, 4]))

















