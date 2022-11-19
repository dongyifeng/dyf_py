'''
给定一个字符串str，str 表示一个公式，公式里可能有整数，加减乘除和左右括号，返回公式的计算结果。
【举例】
str = “48*((70-65)-43)+8*1” , 返回 -1816
str = “3+1*4” , 返回 7
str = “3+(1*4)” , 返回 7
【说明】
1. 可以认为给定的字符串一定是正确的公式，即不需要对 str 做公式有效性检查。
2. 如果是负数，就需要用括号括起来，比如”4*(-3)“ 。但如果负数作为公式的开头或者括号部分的开头，则可以没有括号，比如：”-3*4“ 和 ”(-3*4)“ 都是合法的。
3. 不用考虑计算过程中发生的溢出的情况
'''


def expression_compute(string):
    return process(string, 0)[0]


def get_num(string, index):
    num = 0
    for i in range(index, len(string)):
        item = string[i]
        if item < '0' or item > '9': break

        num = num * 10 + int(item)

    return num, i + 1 if i == len(string) - 1 else i


# 计算 string 公式
# 优先括号内的公式，再计算乘除，再计算加减
def process(string, index):
    que = []
    i = index
    while i < len(string):
        # (：递归调用
        if string[i] == "(":
            num, j = process(string, i + 1)
            i = j
            que.append(num)
        # 遇到数字
        elif "0" <= string[i] <= "9":
            num, j = get_num(string, i)
            que.append(num)
            i = j
        # ) 计算括号内的公式
        elif string[i] == ")":
            res = sub_expression_compute(que)
            return res, i + 1
        else:
            que.append(string[i])
            i += 1

    # 计算没有括号，剩下的公式
    return sub_expression_compute(que), i


# 计算 array 内的公式
# 优先计算乘除，再计算加减
def sub_expression_compute(array):
    stack = []
    i = 0
    # 计算乘除
    while i < len(array):
        if array[i] == "*" or array[i] == "/":
            stack.append(compute(stack.pop(), array[i], array[i + 1]))
            i += 2
        else:
            stack.append(array[i])
            i += 1

    # 计算加减
    i = 0
    res = stack[0]
    while i < len(stack) - 1:
        operator = stack[i + 1]
        num2 = stack[i + 2]
        res = compute(res, operator, num2)
        i += 2
    return res


def compute(num1, operator, num2):
    if operator == "+": return num1 + num2
    if operator == "-": return num1 - num2
    if operator == "*": return num1 * num2
    if operator == "/": return int(num1 / num2)


# import random
#
#
# def generator_expression(max_value, max_size):
#     count = int(random.random() * max_size) + 2
#     res = []
#     operator = ["+", "-", "*", "/"]
#     for i in range(count):
#         res.append(str(int(random.random() * max_value) + 1))
#         res.append(random.sample(operator, 1)[0])
#     return "".join(res[0:-1])
#
#
# def check():
#     max_value = 100
#     max_size = 10
#
#     for i in range(100):
#         expression = generator_expression(max_value, max_size)
#         print(expression, '=', expression_compute(expression))


print(expression_compute("48*((70-65)-43)+8*1"))
print(expression_compute("3+1*4"))
print(expression_compute("3+(1*4)"))
