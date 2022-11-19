# coding=utf-8
print "从stream 中获取第 k 的元素"

import heapq


class KthLargest:
    def __init__(self, k):
        self.k = k
        self.heap = []

    def add(self, item):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, item)
        else:
            if (item > self.heap[0]):
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, item)
        return self.heap[0]

    def get_top_k(self):
        return self.heap[0]


kthLargest = KthLargest(3)
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for item in data:
    kthLargest.add(item)
print kthLargest.get_top_k()
