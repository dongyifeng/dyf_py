'''
130. 被围绕的区域
给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
 
输入：board =
[["X","X","X","X"],
["X","O","O","X"],
["X","X","O","X"],
["X","O","X","X"]]
输出：
[["X","X","X","X"],
["X","X","X","X"],
["X","X","X","X"],
["X","O","X","X"]]
解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

输入：board = [["X"]]
输出：[["X"]]
'''

'''
思路：
首先对边界上每一个'O'做深度优先搜索，将与其相连的所有'O'改为'-'。
然后遍历矩阵，将矩阵中所有'O'改为'X',将矩阵中所有'-'变为'O' 
'''


def solve(board):
    if not board: return board

    m = len(board)
    n = len(board[0])
    if m == 1 or n == 1: return board

    for i in [0, m]:
        for j in range(n):
            if board[i][j]=="0":
                board[i][j]="-"
            if board[j][i]=="0":
                board[i][j]="-"
            print(i, j)
            print(j,i)


    print("--------")
    for i in [0, n]:
        for j in range(m):
            print(j, i)

board=[["X","X","X","X"],
       ["X","O","O","X"],
       ["X","X","O","X"],
       ["X","O","X","X"]]
solve(board)