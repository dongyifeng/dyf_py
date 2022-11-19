# coding:utf-8


print('''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

 
''')

'''
暴力破解
'''


def force(s):
    n = len(s)
    result = ''
    for i in range(n):
        for j in range(i + 1, n):
            sub_str = s[i:j]
            if is_palindrome0(sub_str) and len(sub_str) > len(result):
                result = sub_str
    return result

'''
判断字符串是否是回文串
'''
def is_palindrome0(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

'''
双指针
时间复杂度：O(n^2)
空间复杂度：O(n^2)
'''
def longest_palindrome1(s):
    n = len(s)
    start = 0
    max_len = 1
    for i in range(1, n):
        new_start, new_len = is_palindrome(s, i - 1, i + 1)
        if new_len and new_len > max_len:
            start = new_start
            max_len = new_len

        new_start, new_len = is_palindrome(s, i - 1, i)
        if new_len and new_len > max_len:
            start = new_start
            max_len = new_len

    return s[start: start + max_len]


def is_palindrome(s, left, right):
    tmp_len = 0
    tmp_start = -1
    while left >= 0 and right < len(s):
        if s[left] != s[right]:
            break
        if (right - left + 1) > tmp_len:
            tmp_len = right - left + 1
            tmp_start = left
        left -= 1
        right += 1
    return (tmp_start, tmp_len)


'''
动态规划解法
时间复杂度：O(n^2)
空间复杂度：O(n^2)

dp[i][j] = True 表示：s[i:j] 是回文串

推导公式：dp[i][j] = (s[i] == s[j]) and ( i-j<2 or dp[i+1][j-1] )

dp[i+1][j-1] 是表示：s[i:j] 掐头去尾的子串是否是回文串。如果是，且 s[i] == s[j] 那么，s[i:j] 也是回文串。
'''


def longest_palindrome(s):
    n = len(s)
    dp = [[None] * n for k in range(n)]
    start = 0
    max_len = 1
    for i in range(n):
        for j in range(i + 1):
            if i - j < 2:
                dp[j][i] = s[i] == s[j]
            else:
                dp[j][i] = s[i] == s[j] and dp[j + 1][i - 1]

            if dp[j][i] and (i - j + 1) > max_len:
                max_len = i - j + 1
                start = j

    return s[start: start + max_len]


'''
动态规划解法（将二维数组，压缩成一位数组）
时间复杂度：O(n^2)
空间复杂度：O(n)
'''


def longest_palindrome3(s):
    n = len(s)
    dp = [None for k in range(n)]
    start = 0
    max_len = 1
    for i in range(n):
        for j in range(i + 1):
            if i - j < 2:
                dp[j] = s[i] == s[j]
            else:
                dp[j] = s[i] == s[j] and dp[j + 1]

            if dp[j] and (i - j + 1) > max_len:
                max_len = i - j + 1
                start = j

    return s[start: start + max_len]


print(force("babad"))
print(force("cbbd"))
print(force("abbaabccba"))
print("-" * 100)

print(longest_palindrome1("babad"))
print(longest_palindrome1("cbbd"))
print(longest_palindrome1("abbaabccba"))
print("-" * 100)

print(longest_palindrome("babad"))
print(longest_palindrome("cbbd"))
print(longest_palindrome("abbaabccba"))

print("-" * 100)

print(longest_palindrome3("babad"))
print(longest_palindrome3("cbbd"))
print(longest_palindrome3("abbaabccba"))
