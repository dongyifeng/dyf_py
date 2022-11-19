'''
给定一个元素为非负整数的二维数组 matrix ，每行和每列都是从小到大有序的。再给定一个非负整数 aim，请判断 aim 是否在 matrix 中。
'''


def find(M, aim):
    n = len(M)
    m = len(M[0])
    row = 0
    col = m - 1

    while row < n and col > -1:
        if M[row][col] == aim:
            return True
        if M[row][col] > aim:
            col -= 1
        else:
            row += 1
    return False


print(find([[1, 5, 9, 10], [2, 6, 11, 16], [7, 9, 15, 17]], 7))
print(find([[1, 5, 9, 10], [2, 6, 11, 16], [7, 9, 15, 17]], 2))
print(find([[1, 5, 9, 10], [2, 6, 11, 16], [7, 9, 15, 17]], 3))

'''
给定一个的二维数组 matrix ，矩阵只有 0 和 1 组成，1 在 0 的左边，求 1 最多的行号。
'''


def maxOne(M):
    n = len(M)
    m = len(M[0])
    row = 0
    col = m - 1

    res = -1
    while row < n and col > -1:
        if M[row][col] == 1:
            col -= 1
            res = row
        else:
            row += 1
    return res


print(maxOne([[0, 0, 0, 0, 1, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 1, 1],
              [0, 0, 0, 1, 1, 1, 1, 1],
              [0, 0, 0, 1, 1, 1, 1, 1],
              [0, 1, 1, 1, 1, 1, 1, 1]
              ]))

print(maxOne([[0, 0, 0, 0, 1, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 1, 1],
              [0, 0, 0, 1, 1, 1, 1, 1],
              [0, 1, 1, 1, 1, 1, 1, 1],
              [0, 0, 1, 1, 1, 1, 1, 1]
              ]))

print(maxOne([[0, 0, 0, 0, 1, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 1, 1],
              [0, 1, 1, 1, 1, 1, 1, 1],
              [0, 0, 0, 1, 1, 1, 1, 1],
              [0, 0, 1, 1, 1, 1, 1, 1]
              ]))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


res = 0


def max_weight(head):
    global res
    process(head, 0)
    return res


def process(node, pre):
    global res
    pre += node.val
    # 叶子节点
    if not node.left and not node.right:
        res = max(res, pre)
        return

    if node.left:
        process(node.left, pre)
    if node.right:
        process(node.right, pre)


def max_weight2(head):
    return process2(head)


def process2(node):
    left_value = 0
    right_value = 0
    if node.left:
        left_value = process2(node.left)
    if node.right:
        right_value = process2(node.right)
    return max(left_value, right_value) + node.val


head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)

head.left.left = TreeNode(4)
head.left.right = TreeNode(5)

head.right.left = TreeNode(6)
head.right.right = TreeNode(7)

print("max_weight", max_weight(head))
print("max_weight2", max_weight2(head))

'''
请编写一个程序，对一个栈里的整型数据，按升序进行排序（即排序前，栈里的数据是无序的，排序后最大元素位于栈顶），要求最多只能使用一个额外的栈存放临时数据，但不得将元素复制到别的数据结构中。
'''


def process3(stack):
    tmp_stack = []
    while stack:
        x = stack.pop()
        if not tmp_stack or x < tmp_stack[-1]:
            tmp_stack.append(x)
            continue

        while tmp_stack and x > tmp_stack[-1]:
            stack.append(tmp_stack.pop())
        stack.append(x)

    while tmp_stack:
        stack.append(tmp_stack.pop())


stack = [3, 6, 2, 5, 4]
process3(stack)
print(stack)


def max_depth(string):
    count = 0
    res = 0
    for item in string:
        if item == "(":
            count += 1
            res = max(res, count)
        else:
            count -= 1
    return res


print("max_depth", max_depth("((()))"))


def is_match(string):
    count = 0
    for item in string:
        if item == "(":
            count += 1
        else:
            count -= 1
            if count < 0:
                return False
    return True


print(is_match("((()))"))
print(is_match(")((())"))


def num_tree(n):
    if n == 0: return 1
    if n < 3:
        return n
    res = 0
    for i in range(n):
        res += num_tree(i) * num_tree(n - i - 1)
    return res


def num_tree2(n):
    if n < 0: return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]

    return dp[-1]


print(num_tree(4))
print(num_tree2(4))

'''
将给定的数转换为字符串，原则如下：1 对应 a，2 对应 b，... 26 对应 z。例如：12258 可以转换为 ”abbeh“，”aveh“，“abyh”，”lbeh“，”lyh“  ，
个数为 5。编写一个数，给出可以转换的不同字符串的个数。
'''


def num_to_string_ways(num):
    if num <= 0:
        return 0
    return process3(str(num), 0)


def process3(string, index):
    if index == len(string):
        return 1

    # index 后还有其他数字
    # 以 0 开头返回 0
    if string[index] == "0":
        return 0

    # index 及其后续还有数字字符，且不以 0 开头，以 1 ~ 9 开头
    res = process3(string, index + 1)

    if index == len(string) - 1:
        return res

    # index + 1 没有越界
    # index 和 index + 1 共同构成一个部分 < 27
    if ((ord(string[index]) - ord("a")) * 10 + (ord(string[index + 1]) - ord("a"))) < 26:
        res += process3(string, index + 2)
    return res


print(num_to_string_ways(12258))

'''
假设 s 和 m 初始化：s = ”a“；m = s

再定义两种操作：

第一种操作：

1. m = s
2. s = s + s

第二种操作：s = s + m

求最小的操作步骤数，可以将 s 拼接到长度等于 n
'''


def div_sum_and_count(n):
    sum = 0
    count = 0
    for i in range(2, n):
        while n % i == 0:
            sum += i
            count += 1
            n /= i
    return (sum, count)


def min_ops(n):
    if n < 2: return 0
    if is_prime(n):
        return n - 1
    sum, count = div_sum_and_count(n)
    return sum - count


def is_prime(n):
    for i in range(2, n):
        if n % i == 0: return False
    return True


print("min_ops")
print(min_ops(10))
