'''
输入：正数数组 costs，正数数组 profits，正数 k，正数 m。

- costs[i]  表示 i 号项目的花费。
- profits[i] 表示 i 号项目在扣除花费之后还能挣到的钱（利润）。
- k 表示你只能串行的最多做 k 个项目
- m 表示你初始的资金

说明：你没做完一个项目，马上获得的收益，可以支持你去做下一个项目。

输出：你最后获得的最大钱数。
'''

import heapq


def get_max_capital(costs, profits, k, m):
    min_cost_heap = []
    max_profit_heap = []

    # 所有项扔到被锁池中，花费组织的小根堆
    for i in range(len(costs)):
        heapq.heappush(min_cost_heap, (costs[i], profits[i]))

    # 进行 k 轮
    for _ in range(k):
        # 能力所及的项目，全解锁
        while min_cost_heap and min_cost_heap[0][0] <= m:
            cost, profit = heapq.heappop(min_cost_heap)
            heapq.heappush(max_profit_heap, (-profit, cost))

        if not max_profit_heap:
            return m

        profit, cost = heapq.heappop(max_profit_heap)
        m -= profit

    return m


def get_max_capital2(costs, profits, k, m):
    min_cost_heap = sorted(zip(costs, profits))
    max_profit_heap = []

    i = 0
    for _ in range(k):

        while i < len(costs) and min_cost_heap[i][0] <= m:
            cost, profit = min_cost_heap[i]
            heapq.heappush(max_profit_heap, (-profit, cost))
            i += 1

        if not max_profit_heap:
            return m

        profit, cost = heapq.heappop(max_profit_heap)
        m -= profit

    return m


print(get_max_capital([1, 1, 2, 2, 3, 4], [1, 4, 3, 7, 2, 10], 4, 1))
print(get_max_capital2([1, 1, 2, 2, 3, 4], [1, 4, 3, 7, 2, 10], 4, 1))
