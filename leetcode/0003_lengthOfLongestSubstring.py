# coding:utf-8

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    longest = 0
    sub_string = dict()
    i = 0
    while i < len(s):
        item = s[i]
        if item in sub_string:
            longest = max(longest, len(sub_string))
            i = sub_string[item] + 2 if sub_string[item] - i > 1 else i
            sub_string = dict([(k, v) for k, v in sub_string.items() if v > sub_string[item]])
            continue

        sub_string[item] = i
        i += 1
    # print(sub_string)
    return max(longest, len(sub_string))


# print(lengthOfLongestSubstring("abcabcbb"))
#
# print(lengthOfLongestSubstring("bbbbb"))
#
# print(lengthOfLongestSubstring("pwwkew"))

print(lengthOfLongestSubstring("dvdf"))
print(lengthOfLongestSubstring("aab"))
