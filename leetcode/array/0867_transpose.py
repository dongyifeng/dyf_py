# 转置矩阵
# 给定一个矩阵 A， 返回 A 的转置矩阵。
# 矩阵的转置:将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

# 示例 1：
# 输入：[[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[1,4,7],[2,5,8],[3,6,9]]

# 示例 2：
# 输入：[[1,2,3],[4,5,6]]
# 输出：[[1,4],[2,5],[3,6]]

def transpose(A):
    row_count = len(A)
    column_count = len(A[0])
    T = [[0] * row_count for _ in range(column_count)]

    for i in range(row_count):
        for j in range(column_count):
            T[j][i] = A[i][j]
    return T


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
T = transpose(A)
print(T)

A = [[1, 2, 3], [4, 5, 6]]
T = transpose(A)
print(T)
