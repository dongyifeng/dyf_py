# coding=utf-8
print '''
思路一：暴力
以第i根柱子为最矮柱子所能延伸的最大面积
'''


def largestRectangleArea(heights):
    if not heights: return 0
    n = len(heights)
    if n < 2: return heights[0]

    result = 0
    for i in range(n):
        tmp = heights[i]
        for j in range(i - 1, -1, -1):
            if heights[j] >= heights[i]:
                tmp += heights[i]
            else:
                break
        for k in range(i + 1, n):
            if heights[k] >= heights[i]:
                tmp += heights[i]
            else:
                break
        result = max(tmp, result)
    return result


print largestRectangleArea([2, 1, 5, 6, 2, 3])

print largestRectangleArea([1, 1])

print '''
思路二：单调栈
'''

from Stack import *


def largestRectangleArea2(heights):
    stack = Stack()
    heights = [0] + heights + [0]

    res = 0
    for i in range(len(heights)):
        while not stack.is_empty() and heights[stack.peek()] > heights[i]:
            tmp = stack.pop()
            res = max(res, (i - stack.peek() - 1) * heights[tmp])
            print 'max', res, (i, heights[i])
        stack.push(i)
        print (i, heights[i]), stack.items

    return res


# print largestRectangleArea2([2, 1, 5, 6, 2, 3])
# print largestRectangleArea2([1, 1])

print largestRectangleArea2([1, 2, 1])

