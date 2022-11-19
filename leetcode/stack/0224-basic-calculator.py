# coding=utf-8
print '''
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。

示例 1:

输入: "1 + 1"
输出: 2
示例 2:

输入: " 2-1 + 2 "
输出: 3
示例 3:

输入: "(1+(4+5+2)-3)+(6+8)"
输出: 23
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。
'''

import re


def calc(opands, opors):
    b = opands.pop()
    a = opands.pop()
    op = opors.pop()
    if op == "+":
        opands.append(a + b)
    elif op == "-":
        opands.append(a - b)


'''
双栈

将普通的表达式转化为逆波兰式。
'''


def calculate(s):
    opands = []
    opors = []
    nums = list([item.strip() for item in re.split('([-+()])', s) if item.strip()])

    for item in nums:
        if item == "(":
            opors.append(item)
        elif item == "+" or item == "-" or item == ")":
            # 当 opors 顶端是 + - 时，就是可以计算表达式
            while opors and (opors[-1] == "+" or opors[-1] == "-"):
                calc(opands, opors)
            # 括号中间算式计算完毕，这剩下()
            if item == ")":
                if opors and opors[-1] == "(": opors.pop()
            else:
                opors.append(item)
        # item 为数字
        else:
            opands.append(int(item))

    while opors:
        calc(opands, opors)
    return opands[-1]


print "result:", calculate('2-(5-6)')

'''
单栈
'''


def calculate2(s):
    stack = []
    nums = list([item.strip() for item in re.split('([-+()])', s) if item.strip()])

    left = 0
    next_sign = 1
    next_int = 0
    for item in nums:
        if item == "(":
            stack.append(left)
            stack.append(next_sign)
            next_sign = 1
            next_int = 0
            left = 0
        elif item == ")":
            left += next_sign * next_int
            my_sign = stack.pop()
            prev_left = stack.pop()
            left = prev_left + my_sign * left
            next_sign = 1
            next_int = 0
        elif item == "+" or item == "-":
            left += next_sign * next_int
            next_sign = 1 if item == "+" else -1
            next_int = 0
        else:
            next_int = int(item)
    return left + next_sign * next_int


print "result2:", calculate2('2-(5-6)')
