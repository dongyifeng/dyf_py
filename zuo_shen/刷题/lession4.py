'''
用 zigzag 的方式打印矩阵
'''


def print_matrix_zigzag(M):
    n = len(M)
    m = len(M[0])
    a_row = a_col = b_row = b_col = 0
    direction = False
    while a_row < n and a_col < m and b_row < n and b_col < m:
        print_level(M, a_row, a_col, b_row, b_col, direction)

        a_row = a_row + 1 if a_col == m - 1 else a_row
        a_col = a_col if a_col == m - 1 else a_col + 1
        b_col = b_col + 1 if b_row == n - 1 else b_col
        b_row = b_row if b_row == n - 1 else b_row + 1
        direction = not direction
    print("")


def print_level(M, a_row, a_col, b_row, b_col, direction):
    n = len(M)
    m = len(M[0])
    if direction:
        while a_row < n and a_col > -1:
            print(M[a_row][a_col], end=" ")
            a_row += 1
            a_col -= 1
    else:
        while b_row > -1 and b_col < m:
            print(M[b_row][b_col], end=" ")
            b_row -= 1
            b_col += 1


M = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
print_matrix_zigzag(M)
print("-" * 10)
M = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]
print_matrix_zigzag(M)
print("-" * 10)
M = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
print_matrix_zigzag(M)

'''
用螺旋方式打印矩阵
'''
print("用螺旋方式打印矩阵")


def spiral_order_print(M):
    a_row = a_col = 0
    b_row = len(M) - 1
    b_col = len(M[0]) - 1

    while a_row <= b_row and a_col <= b_col:
        print_edge(M, a_row, a_col, b_row, b_col)
        a_row += 1
        a_col += 1
        b_row -= 1
        b_col -= 1
    print()


def print_edge(M, a_row, a_col, b_row, b_col):
    # 打印上边
    for i in range(a_col, b_col + 1):
        print(M[a_row][i], end=" ")

    # 打印右边
    for i in range(a_row + 1, b_row):
        print(M[i][b_col], end=" ")

    # 打印下边
    for i in range(b_col, a_col, -1):
        print(M[b_row][i], end=" ")

    # 打印左边
    for i in range(b_row, a_row, -1):
        print(M[i][a_col], end=" ")


M = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

print_edge(M, 0, 0, 3, 3)
print("-" * 10)
spiral_order_print(M)

'''
给定一个正方形矩阵，只用有限几个变量，实现矩阵中每个位置的数顺时针转动 90 度
'''


def rotate(M):
    a_row = 0
    b_row = len(M) - 1
    while a_row < b_row:
        rotate_edge(M, a_row, b_row)
        a_row += 1
        b_row -= 1


def rotate_edge(M, a_row, b_row):
    for i in range(b_row - a_row):
        tmp = M[a_row][a_row + i]

        M[a_row][a_row + i] = M[b_row - i][a_row]

        M[b_row - i][a_row] = M[b_row][b_row - i]

        M[b_row][b_row - i] = M[a_row + i][b_row]

        M[a_row + i][b_row] = tmp


M = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
rotate(M)
for item in M:
    print(item)


def rotate2(M):
    n = len(M)
    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[j][n - i - 1] = M[i][j]

    for i in range(n):
        for j in range(n):
            M[i][j] = tmp[i][j]


M = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
print(rotate2(M))
for item in M:
    print(item)

'''
有 n 个打包机器从左到右一字排开，上方有一个自动装置会抓取一批物品到每个打包机上，放到每个机器上的这些物品数量有多有少，由于物品数量不相同，
需要工人将每个机器上的物品进行移动，从而达到物品数量相等才能打包。每个物品重量太大、每次只能搬动一个物品进行移动，为了省力，只在相邻的机器上移动。
请计算在搬动最小轮数的前提下，使每个机器上的物品数量相等。如果不能使每个机器上的物品相等返回 -1.
'''


def min_ops(nums):
    nums_sum = sum(nums)
    n = len(nums)

    if nums_sum % n != 0: return -1
    avg = int(nums_sum / n)

    left_sum = 0
    res = 0
    for i in range(n):
        left_rest = left_sum - i * avg
        right_rest = nums_sum - nums[i] - left_sum - (n - i - 1) * avg

        if left_rest < 0 and right_rest < 0:
            res = max(res, abs(left_rest) + abs(right_rest))
        else:
            res = max(res, max(abs(left_rest), abs(right_rest)))

        left_sum += nums[i]
    return res


print(min_ops([1, 0, 5]))

'''
给一个包含 n 个正整数元素的集合 a，一个包含 m 个正整数的集合 b。给定 magic 操作为：从一个集合中取出一个元素，放到另一个集合里，且操作过后每个集合的平均值都大于操作之前。
'''


def max_ops(array1, array2):
    sum1 = sum(array1)
    sum2 = sum(array1)

    avg1 = sum1 / len(array1)
    avg2 = sum2 / len(array2)
    if avg1 == avg2: return 0

    if avg1 > avg2:
        more_sum = sum1
        more_arr = array1
        less_sum = sum2
        less_arr = array2
    else:
        more_sum = sum2
        more_arr = array2
        less_sum = sum1
        less_arr = array1

    more_arr.sort()
    more_n = len(more_arr)
    less_n = len(less_arr)
    set_less = set(less_arr)
    res = 0
    for i in range(len(more_arr)):
        if more_arr[i] < (more_sum / more_n) and more_arr[i] > (less_sum / less_n) and more_arr[i] in set_less:
            more_sum -= more_arr[i]
            more_n -= 1
            less_sum += more_arr[i]
            less_n += 1
            res += 1
    return res


print()

'''
给定一个字符串类型的 arr，求其中出现次数最多的前 K 个。
'''

import heapq


def top_k(arr, k):
    n = len(arr)
    if n <= k: return arr

    freq_map = {}
    for item in arr:
        freq_map[item] = freq_map.get(item, 0) + 1

    return heapq.nlargest(k, freq_map.items(), key=lambda x: x[1])


print("top_k", top_k(["a", "a", "a", "b", "b", "b", "b", "b", "b", "b", "c", "c"], 2))


class Heap:
    def __init__(self, capacity, reverse=False):
        self.a = [None] * (capacity + 1)
        self.n = capacity
        self.count = 0
        self.reverse = reverse

    def push(self, data):
        # 堆满了
        if self.count >= self.n: return
        self.count += 1
        self.a[self.count] = data
        i = self.count

        # 自下向上堆化
        self.heapinsert(i)

    def pop(self):
        if self.count == 0: return
        data = self.a[1]
        self.a[1] = self.a[self.count]
        self.count -= 1
        self.heapify(1)
        return data

    def peek(self):
        if self.count == 0: return
        return self.a[1]

    # 自下向上堆化
    def heap_insert(self,i):
        while self.parent(i) > 0 and not self.compare(self.a[i], self.a[self.parent(i)]):
            self.a[i], self.a[self.parent(i)] = self.a[self.parent(i)], self.a[i]
            i = self.parent(i)

    # 从上向下堆化
    def heapify(self, i):
        while True:
            # 左子树判断
            if self.left(i) < self.count and self.compare(self.a[i], self.a[self.left(i)]):
                j = self.left(i)
            # 右子树判断
            elif self.right(i) < self.count and self.compare(self.a[i], self.a[self.right(i)]):
                j = self.right(i)
            else:
                break
            self.a[i], self.a[j] = self.a[j], self.a[i]
            i = j

    def heapify(self, i):
        left = self.left(i)
        right = self.right()
        # right = left + 1
        while left < self.count:
            # 从 left 和 right 选择较大的下标给 largest
            largest = right if right < self.count and self.a[right] > self.a[left] else left

            # 较大孩子与父节点比较
            largest = largest if self.a[largest] > self.a[i] else i

            # 父节点比 largest 大，不需要继续下沉了
            if largest == i:
                break

            self.a[largest], self.a[i] = self.a[i], self.a[largest]
            i = largest
            left = self.left(i)

    def is_full(self):
        return self.count >= self.n

    def is_empty(self):
        return self.count == 0

    def compare(self, a, b):
        if self.reverse:
            return b > a
        return a > b

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def parent(self, i):
        return i >> 1


def top_k2(arr, k):
    n = len(arr)
    if n <= k: return arr

    freq_map = {}
    for item in arr:
        freq_map[item] = freq_map.get(item, 0) + 1

    heap = Heap(k)
    for k, v in freq_map.items():
        if not heap.is_full():
            heap.push((v, k))
            continue
        if heap.peek()[0] < v:
            heap.pop()
            heap.push((v, k))

    res = []
    while not heap.is_empty():
        res.append(heap.pop())
    return res


print("top_k2", top_k2(["a", "a", "a", "b", "b", "b", "b", "b", "b", "b", "c", "c"], 2))
