class HeapGreater:
    class DataNode:
        def __init__(self, data):
            self.data = data

    def __init__(self, comparator):
        self.comparator = comparator
        self.heap = [None]
        self.index_map = {}
        self.size = 1

    def build(self, data):
        self.heap = data
        self.size = len(data)
        self.heap.insert(0, None)
        self.index_map.clear()
        for i in range(1, self.size):
            self.index_map[HeapGreater.DataNode(self.heap[i])] = i

        n = len(data) >> 1
        for i in range(n, -1, -1):
            self.heap_insert(i)

    def __contains__(self, item):
        return item in self.index_map

    def peek(self):
        if self.size > 1:
            return self.heap[1]

    def pop(self):
        res = self.peek()
        if res == None: return
        self.swap(1, self.size)
        self.index_map.pop(res)
        self.remove(self.size)
        self.size -= 1
        self.heapify(1)
        return res

    def push(self, obj):
        if obj == None: return

        self.size += 1
        self.heap.append(obj)
        self.index_map[HeapGreater.DataNode(obj)] = self.size
        self.heap_insert(self.size)

    def replace(self, obj):
        res = self.peek()
        if res == None:
            return obj

        if obj == None:
            return self.pop()

        self.remove(res)
        self.index_map[HeapGreater.DataNode(obj)] = 1
        self.heap.insert(1, obj)
        self.heapify(1)
        return res

    def push_and_pop(self, obj):
        res = self.pop()
        if res == None:
            return obj

        if obj == None:
            return self.pop()

        if self.comparator(obj.data, res.data):
            return obj

        self.index_map.pop(res)
        self.index_map[HeapGreater.DataNode(obj)] = 1
        self.heap.insert(1, obj)
        self.heapify(1)
        return res

    def left(self, index):
        return 2 * index

    def right(self, index):
        return 2 * index + 1

    def parent(self, index):
        return index >> 1

    def is_empty(self):
        return self.size <= 1

    def remove(self, obj):
        replace = self.heap[self.size]
        index = self.index_map[replace]
        self.index_map.pop(replace)
        self.heap.pop(self.size)
        self.size -= 1
        if not obj:
            self.heap.insert(index, replace)
            self.index_map[HeapGreater.DataNode(obj)] = index
            self.resign(replace)

    def heapify(self, index):
        left = self.left(index)
        right = self.right(index)

        while left < self.size:
            largest = right if right <= self.size and self.comparator(self.heap[right].data,
                                                                      self.heap[left].data) else left
            largest = largest if self.comparator(self.heap[largest].data, self.heap[index].data) > 0 else index

            if largest == index: break

            self.swap(largest, index)
            index = largest
            left = self.left(index)

    def heap_insert(self, index):
        parent = self.parent(index)
        while parent > 0 and self.comparator(self.heap[index].data, self.heap[parent].data):
            self.swap(index, parent)
            index = parent
            parent = self.parent(index)

    def resign(self, obj):
        index = self.index_map[obj]
        self.heap_insert(index)
        self.heapify(index)

    def get_all_elements(self):
        res = []
        for i in range(1, self.size + 1):
            res.append(self.heap[i])
        return res

    def swap(self, i, j):
        o1 = self.heap[i]
        o2 = self.heap[j]

        self.heap.index(i, o2)
        self.heap.index(j, o1)
        self.index_map[HeapGreater.DataNode(o2)] = i
        self.index_map[HeapGreater.DataNode(o1)] = j


import heapq
import random


def check():
    n = 10000
    data = []
    heap_greater = HeapGreater(lambda x, y: x > y)
    max_value = 100
    for i in range(n):
        if int(random.random() * 10) in [1, 2, 3, 4, 5]:
            num = int(random.random() * max_value)
            heapq.heappush(data, num)
            heap_greater.push(num)

        if int(random.random() * 10) in [6, 7]:
            if len(data)>0 and not heap_greater.is_empty():
                num1=heapq.heappop(data)
                num2=heap_greater.pop()
                if num1!=num2:
                    print("ERROR", num1, num2)

        if len(data)>0 and not heap_greater.is_empty():

            if data[0] != heap_greater.peek().data:
                print("ERROR", data[0], heap_greater.peek())


check()
