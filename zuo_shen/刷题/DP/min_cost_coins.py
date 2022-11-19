'''
CC 里面有一个土豪很喜欢一位女直播 kiki 唱歌，平时就经常给她点赞、送礼、私聊。最近 CC 直播平台在举行中秋之星直播唱歌比赛，
假设一开始该女主播的初始人气值为 start，能够晋升下一轮人气需要刚好达到 end，土豪给主播增加人气可以采取一下三种方法：

1. 点赞；花费 x C币，人气 + 2
2. 送礼；花费 y C 币，人气 * 2
3. 私聊；花费 z C币，人气 - 2

其中 end 远大于 start 且 end 为偶数，请写一个程序帮助土豪计算一下，最少花费多少 C 币就能帮助该主播 kiki 将人气刚好达到 end，从而能够晋级下一轮？

限制 $0<x,y,z<=10000 ;\quad 0<start,end<1000000$

【例如】

输入：start = 3，end = 100，x = 1，y = 2，z = 6

输出：6
'''

# def min_cost_coins(start, end, x, y, z):
#     return process(start, end, x, y, z)
#
#
# def process(start, end, x, y, z):
#     if start == end:
#         return 0
#     a = process(start + 2, end, x, y, z) + x
#     b = process(start * 2, end, x, y, z) + y
#     c = process(start - 2, end, x, y, z) + z
#
#     return min(a, b, c)


import sys


def min_cost_coins2(start, end, add, times, delete):
    return process2(0, start, end, add, times, delete, int(((end - start) / 2)) * add)


def process2(cost, start, end, add, times, delete, limit_coin):
    if cost > limit_coin: return sys.maxsize
    if start < 0: return sys.maxsize
    if start >= (2 * end): return sys.maxsize

    if start == end: return cost

    res = sys.maxsize
    tmp = process2(cost + add, start + 2, end, add, times, delete, limit_coin)
    if tmp != sys.maxsize:
        res = tmp

    tmp = process2(cost + delete, start - 2, end, add, times, delete, limit_coin)
    if tmp != sys.maxsize:
        res = min(res, tmp)

    tmp = process2(cost + times, start * 2, end, add, times, delete, limit_coin)
    if tmp != sys.maxsize:
        res = min(res, tmp)

    return res


add = 6
times = 5
delete = 1

print(min_cost_coins2(10, 30, add, times, delete))
