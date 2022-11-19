'''
arr=【3,2,7】 每个数表示每一个咖啡机冲一杯咖啡用的时间。有 N 个人要喝咖啡，假设每人喝咖啡的时间为 0。每人要在咖啡机前排队冲咖啡。
只有 1 台洗咖啡杯的机器（只能串行不能并行），需要 a 的时间才能洗完。咖啡杯如果不洗靠挥发 b 时也能变干净。
问所有人喝完咖啡并且让各自的咖啡杯变干净至少需要多少时间？
'''

import heapq


def min_time(arr, n, a, b):
    heap = []
    for item in arr:
        heapq.heappush(heap, (item, 0, item))

    drinks = [0] * n
    for i in range(n):
        s, time_point, work_time = heapq.heappop(heap)
        drinks[i] = time_point + work_time
        heapq.heappush(heap, (s + work_time, time_point + work_time, work_time))

    print(drinks)
    return process(drinks, a, b, 0, 0)


# 还剩 wash_line 时间可以用洗杯机
def process(drinks, a, b, index, wash_line):
    if index == len(drinks) - 1:
        # 洗杯 vs 风干，取最小值
        # 如果洗杯：如果 wash_line 大说明需要等， max(wash_line, drink[index])
        return min(max(wash_line, drinks[index]) + a, drinks[index] + b)

    # 选择一：洗杯
    # wash 是我当前的咖啡杯，洗完的时间
    wash = max(wash_line, drinks[index]) + a
    # 我洗完后，其他人用的时间
    next1 = process(drinks, a, b, index + 1, wash)
    # 我与其他人最晚完成的时间就是总的时间
    p1 = max(wash, next1)

    # 选择二：风干
    # dry 是我当前的咖啡杯，风干的时间
    dry = drinks[index] + b
    # 我在风干,没有影响 wash_line，其他的使用的时间
    next2 = process(drinks, a, b, index + 1, wash_line)
    p2 = max(dry, next2)

    # 两种选择的最小值
    return min(p1, p2)


print(min_time([2, 3, 7], 10, 10, 10))
