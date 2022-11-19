# coding=utf-8
print '''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
'''

from Stack import *


def isValid(s):
    pair = {"(": ")", "[": "]", "{": "}"}
    stack = Stack()
    for char in list(s):
        if char in pair:
            stack.push(char)
        else:
            if stack.is_empty() or pair[stack.pop()] != char: return False

    return stack.is_empty()


# 优化后
def isValid2(s):
    pair = {"(": ")", "[": "]", "{": "}", "?": "?"}
    stack = ['?']

    for char in list(s):
        if char in pair:
            stack.append(char)
        elif pair[stack.pop()] != char:
            return False

    return len(stack) == 1


# print isValid2("()")
#
# print isValid2("()[]{}")
#
# print isValid2("(]")
#
# print isValid2("([)]")
#
# print isValid2("{[]}")
#
# print isValid2("{[]}")

print isValid2("]")

print isValid2("[")
