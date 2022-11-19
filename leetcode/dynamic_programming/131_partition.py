def partition(s):
    n = len(s)
    matrix = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        matrix[i][i] = True


    # for i in range(n):
    #     for j in range(n - i):
    #         if s[i - j] == s[i + j]:
    #             matrix[i - j][i + j] = True
    #
    # print(matrix)


print(partition("aab"))
