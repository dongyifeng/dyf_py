def word_break(s, wordDict):
    word_dict = set(wordDict)
    n = len(s)
    f = [False] * (n + 1)
    f[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if f[j] and s[j:i] in word_dict:
                f[i] = True
                break

    return f[n]


print(word_break("leetcode", set(["leet", "code"])))
print(word_break("applepenapple", set(["apple", "pen"])))
print(word_break("catsandog", set(["cats", "dog", "sand", "and", "cat"])))
print(word_break("aaaaaaa", set(["aaaa", "aaa"])))
