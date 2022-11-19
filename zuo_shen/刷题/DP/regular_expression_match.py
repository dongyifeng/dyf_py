'''
判定一个由 [a - z] 字符构成的字符串和一个包含“?” 和 ”*“ 通配符的字符串是否匹配。
通配符”？“ 匹配任意单一字符，”*“ 匹配任意多个字符包括 0 个字符。
字符串长度不会超过100，字符串不为空。
输入描述：
字符串 str 和包含通配符的字符串 pattern。返回值：true 表示匹配，false 表示不匹配。
'''


def is_match(string, exp):
    if not string or not exp: return False

    return is_valid(string, exp) and f(string, exp, 0, 0)


def is_valid(string, exp):
    for item in string:
        if item == "*" or item == "?": return False
    for i in range(len(exp)):
        if exp[i] == "*" and (i == 0 or exp[i - 1] == "*"): return False
    return True


# str[si:] 能否被 exp[ei:] 匹配出来
# 必须保证 ei 压中的不是 *（这是潜台词，为了减少 f 的参数）
def f(string, exp, si, ei):
    # base case
    if ei == len(exp):
        return si == len(string)

    # 可能性一：ei + 1 位置不是 *
    if ei + 1 == len(exp) or exp[ei + 1] != "*":
        # exp[ei] 与 string[si] 必须匹配 + 后续能走通
        return si != len(string) and (exp[ei] == string[si] or exp[ei] == "?") and f(string, exp, si + 1, ei + 1)

    # 可能性二：ei + 1 位置是 *
    while si != len(string) and (exp[ei] == string[si] or exp[ei] == "?"):
        # exp[ei+2] 去匹配 string[si]
        if f(string, exp, si, ei + 2):
            return True
        # exp[ei+2] 去匹配 string[si] 匹配失败，exp[ei+2] 与 string[si+1] 匹配，之所以能后续匹配是 * 表示多个 string[si]
        si += 1

    return f(string, exp, si, ei + 2)


def is_match2(string, exp):
    if not string or not exp or not is_valid(string, exp): return False
    n_exp = len(exp)
    n_str = len(string)
    dp = [[False] * (n_exp + 1) for _ in range(n_str + 1)]

    # base case
    dp[-1][-1] = True

    for i in range(len(exp) - 2, -1, -2):
        # 只有 a*b*c*...d 这种范式为True 否则为 False
        if exp[i] != "*" and exp[i + 1] == "*":
            dp[n_str][i] = True
        else:
            break
    if exp[-1] == "?" or string[-1] == exp[-1]:
        dp[-2][-2] = True

    for ei in range(len(exp) - 2, -1, -1):
        for si in range(len(string) - 1, -1, -1):
            # 可能性一：ei + 1 位置不是 *
            if exp[ei + 1] != "*":
                # exp[ei] 与 string[si] 必须匹配 + 后续能走通
                dp[si][ei] = (exp[ei] == string[si] or exp[ei] == "?") and dp[si + 1][ei + 1]
            else:
                # 可能性二：ei + 1 位置是 *
                i = si
                while i != len(string) and (exp[ei] == string[i] or exp[ei] == "?"):
                    # exp[ei+2] 去匹配 string[si]
                    if dp[i][ei + 2]:
                        dp[si][ei] = True
                        break
                    # exp[ei+2] 去匹配 string[si] 匹配失败，exp[ei+2] 与 string[si+1] 匹配，之所以能后续匹配是 * 表示多个 string[si]
                    i += 1
                if not dp[si][ei]:
                    dp[si][ei] = dp[i][ei + 2]

    return dp[0][0]


import random


def generator_random_str(max_size):
    alphabet = [chr(i) for i in range(97, 123)]
    size = int(random.random() * max_size) + 4
    index1 = int(random.random() * size)
    index2 = int(random.random() * size)
    arr = [random.sample(alphabet, 1)[0] for _ in range(size)]
    arr1 = arr[:]
    arr.insert(index1, "*")
    arr.insert(index2, "?")

    return ''.join(arr1), ''.join(arr)


def check():
    max_size = 10
    for i in range(500):
        str1, exp = generator_random_str(max_size)

        res1 = is_match(str1, exp)
        res2 = is_match2(str1, exp)

        if res1 != res2:
            print("ERROR", str1, "res1=", res1, "res2=", res2)
    print("OVER")


check()

print(is_match("abcd", "a??d"))
print(is_match2("abcd", "a??d"))

print(is_match("abcd", "a???d"))
print(is_match2("abcd", "a???d"))
