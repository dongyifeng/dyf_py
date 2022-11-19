'''
一个矩阵中只有 0 和 1两种值，每个位置都可以和自己的上、下、左、右四个位置相连，如果有一片 1 连在一起，这个部分叫做一个岛，求一个矩阵中有多少个岛？
【举例】
0	0	1	0	1	0
1	1	1	0	1	0
1	0	0	1	0	0
0	0	0	0	0	0

这个矩阵中有三个岛。
【进阶】
如何设计一个并行算法解决问题。
'''


def num_of_islands(M):
    row = len(M)
    col = len(M[0])

    res = 0
    for i in range(row):
        for j in range(col):
            if M[i][j] == 1:
                print((i, j))
                res += 1
                infect(M, i, j, row, col)
    return res


def infect(M, i, j, row, col):
    if M[i][j] != 1 or i < 0 or j < 0 or i >= row or j >= col:
        return

    M[i][j] = 2
    # 向上传染
    infect(M, i - 1, j, row, col)
    # 向下传染
    infect(M, i + 1, j, row, col)
    # 向左传染
    infect(M, i, j - 1, row, col)
    # 向右传染
    infect(M, i, j + 1, row, col)


M = [[0, 0, 1, 0, 1, 0],
     [1, 1, 1, 0, 1, 0],
     [1, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0]]
print(num_of_islands(M))

for item in M:
    print(item)
