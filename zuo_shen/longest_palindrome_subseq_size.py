def manacher_str(s):
    return "#" + "#".join(s) + "#"


def longest_palindrome_subseq_size(s):
    res = 0
    s = manacher_str(s)
    n = len(s)
    for i in range(n):
        tmp = 0
        l = r = i
        while r < n and l >= 0:
            if s[l] != s[r]:
                break
            r += 1
            l -= 1
            tmp += 1
        res = max(res, tmp)
    return res - 1




print(longest_palindrome_subseq_size("xabay"))
print(manacher_str("xabay"))
