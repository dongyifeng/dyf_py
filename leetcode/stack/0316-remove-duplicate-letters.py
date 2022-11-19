# coding=utf-8
print '''
给定一个仅包含小写字母的字符串，去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

示例 1:

输入: "bcabc"
输出: "abc"
示例 2:

输入: "cbacdcbc"
输出: "acdb"
'''


def removeDuplicateLetters2(s):
    stack = []
    for i in range(len(s)):
        char = s[i]
        if char in stack: continue
        # stack 中存在 char，如果 stack.top > char 并且 stack.top 后续还有重复存在，stack.top 丢弃。
        while stack and stack[-1] > char and s.find(stack[-1], i) > i: stack.pop()
        stack.append(char)
    return "".join(stack)


print removeDuplicateLetters2("bcabc")
print removeDuplicateLetters2("cbacdcbc")
