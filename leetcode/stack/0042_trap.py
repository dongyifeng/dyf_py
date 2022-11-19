# coding=utf-8
print '''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
'''

from Stack import *


def trap(height):
    if not height or len(height) < 3: return 0
    left = 0
    right = 1

    s = 0
    while left < len(height):
        if height[right] >= height[left]:
            for i in range(left, right):
                s += height[left] - height[i]
            left = right
        right += 1
        if right == len(height):
            left += 1
            right = left
    return s


def trap2(height):
    s = 0
    stack = Stack()
    current = 0
    while current < len(height):
        # 如果栈不空并且当前指向的高度大于栈顶高度就一直循环
        while not stack.is_empty() and height[current] > height[stack.peek()]:
            # 取出要出栈的元素
            h = height[stack.peek()]
            stack.pop()
            if stack.is_empty(): break
            # 两堵墙之前的距离
            distance = current - stack.peek() - 1
            m = min(height[stack.peek()], height[current])
            s += distance * (m - h)
        stack.push(current)
        current += 1

    return s

# print trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print trap([1, 7, 5])
