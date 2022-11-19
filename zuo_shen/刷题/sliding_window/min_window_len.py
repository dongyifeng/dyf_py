'''
给定字符串 str1 和 str2 ，求 str1 的子串中含有 str2 所有字符的最小子串长度。
【举例】
str1 = “abcde” ，str2 = “ac“  因为 ”abc“ 包含 str2 所有的字符，并且在满足这一条件的 str1 的所有子串中，”abc“ 是最短的，返回 3.
str1 = “12345” ，str2 = “344“,最小包含子串不存在，返回 0。
'''

import sys


def min_len(str1, str2):
    map = dict({(item, 0) for item in str1})

    for item in str2:
        map[item] = map.get(item, 0) + 1
    left = right = 0
    match = len(str2)
    res = sys.maxsize

    while right != len(str1):
        map[str1[right]] -= 1
        if map[str1[right]] >= 0:
            match -= 1
        if match == 0:
            print("map",map)
            while map[str1[left]] < 0:
                map[str1[left]] += 1
                left += 1
            res = min(res, right - left + 1)

            print("res", res, left, right,right - left + 1, map)

            match += 1
            map[str1[left]] += 1
            left += 1
        right += 1

    return -1 if res == sys.maxsize else res


print(min_len("aaaabbccbba", "babca"))
