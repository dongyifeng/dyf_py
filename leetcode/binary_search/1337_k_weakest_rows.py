# 1337. 矩阵中战斗力最弱的 K 行


def k_weakest_rows1(mat, k):
    res = sorted([(sum(mat[i]), i) for i in range(len(mat))])
    return [i for s, i in res[:k]]


def k_weakest_rows2(mat, k):
    res = sorted([(find_one(mat[i]), i) for i in range(len(mat))])
    return [i for s, i in res[:k]]


import heapq


def k_weakest_rows3(mat, k):
    q = []

    for i in range(len(mat)):
        q.append((find_one(mat[i]), i))

    heapq.heapify(q)
    return [item[1] for item in heapq.nsmallest(k, q)]


def find_one(row):
    if row[0] == 0: return 0
    if row[-1] == 1: return len(row)

    left = 0
    right = len(row) - 1
    while left <= right:
        mid = (left + right) >> 1
        if row[mid] == 1 and row[mid + 1] == 0: return mid + 1
        if row[mid] == 0:
            right = mid - 1
        else:
            left = mid + 1


mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]

k = 3

print(k_weakest_rows2(mat, k))
print(k_weakest_rows1(mat, k))
print(k_weakest_rows3(mat, k))

mat = [[1, 0, 0, 0],
       [1, 1, 1, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 0]]

k = 2

print(k_weakest_rows2(mat, k))
print(k_weakest_rows1(mat, k))
print(k_weakest_rows3(mat, k))

l = [(2, 0), (4, 1), (1, 2), (5, 3)]
heapq.heapify(l)
print(heapq.nlargest(3, l, key=lambda a: a[0]))

q = []
for item in l:
    heapq.heappush(q, item)

print(heapq.nlargest(3, q, key=lambda a: a[0]))
