class Info:
    def __init__(self, yes, no):
        self.yes = yes
        self.no = no


import sys


def snake(matrix):
    res = - sys.maxsize
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            cur = process(matrix, row, col)
            res = max(res, max(cur.yes, cur.no))
    return res


def process(matrix, row, col):
    if col == 0:
        return Info(-matrix[row][0], matrix[row][0])

    left = process(matrix, row, col - 1)
    # 之前旅程中，一次能力也沒有用，能达到的最大路径和
    pre_no = left.no if left.no >= 0 else -1
    # 之前旅程中，用过一次能力，能达到的最大路径和
    pre_yes = left.yes if left.yes >= 0 else -1

    if row - 1 >= 0:
        left_up = process(matrix, row - 1, col - 1)
        # 如果为负数，说明已经死亡，这条尝试路径断了
        if left_up.yes >= 0:
            pre_yes = max(pre_yes, left_up.yes)
        if left_up.no >= 0:
            pre_no = max(pre_no, left_up.no)

    if row + 1 < len(matrix):
        left_down = process(matrix, row + 1, col - 1)
        if left_down.yes >= 0:
            pre_yes = max(pre_yes, left_down.yes)
        if left_down.no >= 0:
            pre_no = max(pre_no, left_down.no)

    yes = no = -1
    # 之前旅程中，no 这条尝试路径没有断
    if pre_no >= 0:
        # 当前 yes，之前旅途中 no + （当前翻转）
        yes = pre_no - matrix[row][col]
        # 当前 yes，之前旅途中 no + 不翻转
        no = pre_no + matrix[row][col]
    if pre_yes >= 0:
        # 当前 yes，之前旅途中 no + （当前翻转）PK 之前旅途中 yes + 当前不翻转
        yes = max(yes, pre_yes + matrix[row][col])

    return Info(yes, no)


def snake2(matrix):
    res = - sys.maxsize
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            cur = process2(matrix, row, col)
            res = max(res, max(cur.yes, cur.no))
    return res


def process2(matrix, row, col):
    if col == 0:
        return Info(-matrix[row][0], matrix[row][0])

    pre_no = pre_yes = -1
    if row > 0:
        left_up = process2(matrix, row - 1, col - 1)
        if left_up.no >= 0:
            pre_no = left_up.no
        if left_up.yes >= 0:
            pre_yes = left_up.yes

    left = process2(matrix, row, col - 1)
    if left.no >= 0:
        pre_no = max(pre_no, left.no)
    if left.yes >= 0:
        pre_yes = max(pre_yes, left.yes)

    if row < len(matrix) - 1:
        left_down = process2(matrix, row + 1, col - 1)
        if left_down.no >= 0:
            pre_no = max(pre_no, left_down.no)
        if left_down.yes >= 0:
            pre_yes = max(pre_yes, left_down.yes)

    no = yes = -1
    if pre_no >= 0:
        no = pre_no + matrix[row][col]
        yes = pre_no - matrix[row][col]
    if pre_yes >= 0:
        yes = max(yes, pre_yes + matrix[row][col])

    return Info(yes, no)


def snake3(matrix):
    res = - sys.maxsize

    dp_yes = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
    dp_no = [[-1] * len(matrix[0]) for _ in range(len(matrix))]

    # base_case
    for i in range(len(matrix)):
        dp_yes[i][0] = -matrix[i][0]
        dp_no[i][0] = matrix[i][0]

    for col in range(1, len(matrix[0])):
        for row in range(len(matrix)):
            # 之前旅程中，一次能力也沒有用，能达到的最大路径和
            pre_no = dp_no[row][col - 1] if dp_no[row][col - 1] >= 0 else -1
            # 之前旅程中，用过一次能力，能达到的最大路径和
            pre_yes = dp_yes[row][col - 1] if dp_yes[row][col - 1] >= 0 else -1

            if row - 1 >= 0:
                # 如果为负数，说明已经死亡，这条尝试路径断了
                if dp_yes[row - 1][col - 1] >= 0:
                    pre_yes = max(pre_yes, dp_yes[row - 1][col - 1])
                if dp_no[row - 1][col - 1] >= 0:
                    pre_no = max(pre_no, dp_no[row - 1][col - 1])

            if row + 1 < len(matrix):
                if dp_yes[row + 1][col - 1] >= 0:
                    pre_yes = max(pre_yes, dp_yes[row + 1][col - 1])
                if dp_no[row + 1][col - 1] >= 0:
                    pre_no = max(pre_no, dp_no[row + 1][col - 1])

            yes = no = -1
            # 之前旅程中，no 这条尝试路径没有断
            if pre_no >= 0:
                # 当前 yes，之前旅途中 no + （当前翻转）
                yes = pre_no - matrix[row][col]
                # 当前 yes，之前旅途中 no + 不翻转
                no = pre_no + matrix[row][col]
            if pre_yes >= 0:
                # 当前 yes，之前旅途中 no + （当前翻转）PK 之前旅途中 yes + 当前不翻转
                yes = max(yes, pre_yes + matrix[row][col])
            dp_yes[row][col] = yes
            dp_no[row][col] = no

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            res = max(res, max(dp_no[row][col], dp_yes[row][col]))
    return res


import random


def genrator_random_matrix(max_value, max_size):
    col = int(random.random() * max_size) + 1
    row = int(random.random() * max_size) + 1

    matrix = []
    for i in range(row):
        matrix.append([int(random.random() * max_value) - int(random.random() * max_value) for _ in range(col)])
    return matrix


def check():
    max_value = 100
    max_size = 10
    for i in range(100):
        matrix = genrator_random_matrix(max_value, max_size)
        actual = snake(matrix)
        expect = snake2(matrix)
        expect2 = snake3(matrix)

        if actual != expect or actual != expect2:
            print("ERROR", actual, expect, matrix)


matrix = [
    [3, -4, 35, -38, 46]
]

print(snake(matrix))
print(snake2(matrix))
print(snake3(matrix))

check()
