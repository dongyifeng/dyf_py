class UnionFind:
    def __init__(self, array):
        self.father = dict((item, item) for item in array)
        self.size_map = dict((item, 1) for item in array)

    def find(self, x):
        if self.father[x] == x:
            return x

        path = []
        while self.father[x] != x:
            path.append(x)
            x = self.father[x]

        while path:
            self.father[path.pop()] = x
        return x

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        more_parent = x_parent if self.size_map[x_parent] > self.size_map[y_parent] else y_parent
        less_parent = x_parent if more_parent == y_parent else y_parent

        self.father[less_parent] = more_parent
        self.size_map[more_parent] += self.size_map[less_parent]
        self.size_map.pop(less_parent)

    def same(self, x, y):
        return self.find(x) == self.find(y)


disjointSet = UnionFind([1, 2, 2, 3, 4])

disjointSet.union(1, 2)
print(disjointSet.father)
disjointSet.union(1, 3)
print(disjointSet.father)
disjointSet.union(1, 4)

print(disjointSet.father)

