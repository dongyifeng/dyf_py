'''
一块金条切成两半，是需要花费和长度数值一样的铜板的。比如长度为 20 的金条，不管切成长度多大的两半，都要花费 20 个铜板。

一群人想整分整块金条，怎么划分最省铜板？

【例如】给定数组【10,	20,	30】，代表这一共三个人，整块金条长度为 10 + 20 + 30 = 60。金条要分成10，20，30 三个部分。如果先把长度 60 的金条分成 10 和 50，花费 60，再把 50 的金条分成 20 和 30，花费 50；一共花费 110 铜板。但是如果先把金条分成 30 和 30，花费 60；再把长度 30 金条分成 10 和 20，花费 30；一共花费 90 铜板。

输入一个数组，返回划分的最小代价。
'''

import heapq


def get_min_cost(nums):
    if not nums and len(nums) < 3: return nums
    heap = []
    for num in nums:
        heapq.heappush(heap, num)

    res = 0
    while len(heap)>1:
        num = heapq.heappop(heap) +heapq.heappop(heap)
        res += num
        heapq.heappush(heap, num)

    return res


print(get_min_cost([10, 20, 30]))
