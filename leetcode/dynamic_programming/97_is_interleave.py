def is_interleave(s1, s2, s3):
    l = len(s1)
    r = len(s2)

    if l + r != len(s3): return False
    matrix = [[False for _ in range(l + 1)] for _ in range(r + 1)]
    matrix[0][0] = True

    for i in range(r + 1):
        for j in range(l + 1):
            p = i + j - 1
            if i > 0:
                matrix[i][j] |= matrix[i - 1][j] and s2[i - 1] == s3[p]
            if j > 0:
                matrix[i][j] |= matrix[i][j - 1] and s1[j - 1] == s3[p]

    return matrix[r][l]


def is_interleave2(s1, s2, s3):
    l = len(s1)
    r = len(s2)

    if l + r != len(s3): return False
    array = [False] * (l + 1)
    array[0] = True

    for i in range(r + 1):
        for j in range(l + 1):
            p = i + j - 1
            if i > 0:
                array[j] &= s2[i - 1] == s3[p]
            if j > 0:
                array[j] |= array[j - 1] and s1[j - 1] == s3[p]

    return array[-1]


print(is_interleave("aabcc", "dbbca", "aadbbbaccc"))
print(is_interleave("a", "", "c"))
print(is_interleave("aabcc", "dbbca", "aadbbcbcac"))

print('-' * 100)
print(is_interleave2("aabcc", "dbbca", "aadbbbaccc"))
print(is_interleave2("a", "", "c"))
print(is_interleave2("aabcc", "dbbca", "aadbbcbcac"))
