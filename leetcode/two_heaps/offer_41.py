import heapq
import sys


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        # 向 max_heap 插入
        if len(self.max_heap) == len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))
        else:
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap,-num))

    # def addNum(self, num):
    #     """
    #     :type num: int
    #     :rtype: None
    #     """
    #     self.count += 1
    #     if self.count == 1:
    #         heapq.heappush(self.max_heap, -num)
    #         return
    #     # 向 max_heap 插入
    #     if self.count % 2 == 1:
    #         if num > self.min_heap[0]:
    #             x = heapq.heappop(self.min_heap)
    #             heapq.heappush(self.min_heap, num)
    #             heapq.heappush(self.max_heap, -x)
    #         else:
    #             heapq.heappush(self.max_heap, -num)
    #     # 向 min_heap 插入
    #     else:
    #         if num < -self.max_heap[0]:
    #             x = -heapq.heappop(self.max_heap)
    #             heapq.heappush(self.max_heap, -num)
    #             heapq.heappush(self.min_heap, x)
    #         else:
    #             heapq.heappush(self.min_heap, num)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.max_heap) == 0 and len(self.min_heap): return 0
        return -self.max_heap[0] if len(self.max_heap) != len(self.min_heap) else (self.min_heap[0] - self.max_heap[
            0]) / 2.0


medianFinder = MedianFinder()
medianFinder.addNum(-1)
medianFinder.addNum(-2)
medianFinder.addNum(-3)
print(medianFinder.findMedian())
print("min_heap", medianFinder.min_heap)
print("max_heap", [-item for item in medianFinder.max_heap])
