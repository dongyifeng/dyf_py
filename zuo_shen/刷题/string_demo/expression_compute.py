'''
给定一个字符串str，str 表示一个公式，公式里可能有整数，加减乘除，返回公式的计算结果。
【举例】
str = “3-6*9+43*70*8-6” , 返回 24023
str = “3+1*4” , 返回 7
'''


def expression_compute(string):
    stack = []
    i = 0
    while i < len(string):
        item = string[i]
        # 遇到数字
        if '0' <= item <= '9':
            num, j = get_num(string, i)
            stack.append(num)
            i = j
        # 遇到乘除：立即计算
        elif item == "*" or item == "/":
            num, j = get_num(string, i + 1)
            stack.append(compute(stack.pop(), item, num))
            i = j
        # 遇到加减：暂时缓存
        elif item == "+" or item == "-":
            stack.append(item)
            i += 1

    # 计算加减
    i = 0
    res = stack[0]
    # 注意从前向后计算
    while i < len(stack) - 1:
        operator = stack[i + 1]
        num2 = stack[i + 2]
        res = compute(res, operator, num2)
        i += 2
    return res


# 从 string 的 index 位置开始获取数字
# 返回：num, i。计算结果，后续要处理的位置
def get_num(string, index):
    num = 0
    for i in range(index, len(string)):
        item = string[i]
        if item < '0' or item > '9': break

        num = num * 10 + int(item)

    return num, i + 1 if i == len(string) - 1 else i


# 运算
def compute(num1, operator, num2):
    if operator == "+": return num1 + num2
    if operator == "-": return num1 - num2
    if operator == "*": return num1 * num2
    if operator == "/": return int(num1 / num2)


import random


def generator_expression(max_value, max_size):
    count = int(random.random() * max_size) + 2
    res = []
    operator = ["+", "-", "*", "/"]
    for i in range(count):
        res.append(str(int(random.random() * max_value) + 1))
        res.append(random.sample(operator, 1)[0])
    return "".join(res[0:-1])


def check():
    max_value = 100
    max_size = 10

    for i in range(100):
        expression = generator_expression(max_value, max_size)
        print(expression, '=', expression_compute(expression))


# print(expression_compute("14-95+62/50"))
# print(expression_compute("33*46/42"))
check()


def test():
    stack = [66, '+', 77, '+', 95, '-', 10, '+', 36, '-', 279888]

    res = 0
    i = 0
    num1 = stack[0]
    while i < len(stack) - 1:
        operator = stack[i + 1]
        num2 = stack[i + 2]
        num1 = compute(num1, operator, num2)
        i += 2
        # if i==len(stack)-1:break

    # while stack:
    #     num2 = stack.pop()
    #     operator = stack.pop()
    #     num1 = stack.pop()
    #     res = compute(num1, operator, num2)
    #     if not stack:break
    #     stack.append(res)

    print(num2)

# test()
