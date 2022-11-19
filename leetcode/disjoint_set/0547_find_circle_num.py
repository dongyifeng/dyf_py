'''
547. 省份数量

有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。

示例 1：
输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2

示例 2：
输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
输出：3
'''


class DisjointSet:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent, self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


def find_circle_mum(edges):
    disjoint_set = DisjointSet()
    node_set = set()
    for i in range(len(edges)):
        x, y = edges[i]
        disjoint_set.union(x, y)
        node_set.add(x)
        node_set.add(y)

    result = 0
    for node in node_set:
        if node not in disjoint_set.parent:
            result += 1
    return result


def find_circle_mum_matrix(is_connected):
    if not is_connected: return 0
    disjoint_set = DisjointSet()
    node_set = range(len(is_connected))

    for i in range(len(is_connected)):
        for j in range(len(is_connected[i])):
            if i != j and is_connected[i][j] == 1:
                disjoint_set.union(i, j)

    result = 0
    for node in node_set:
        if node not in disjoint_set.parent:
            result += 1
    return result


# edges = [(0, 1), (1, 2), (1, 3), (2, 4), (2, 5), (6, 7)]
# print(find_circle_mum(edges))

isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(find_circle_mum_matrix(isConnected))

isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(find_circle_mum_matrix(isConnected))
