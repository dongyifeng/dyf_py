'''
N 个加油站组成一个环形，给定两个长度都是 N 的非负数组 oil 和 dis（N > 1）,oil[i] 表示第 i 个加油站存的油可以跑多少千米，
dis[i] 代表第 i 个加油站到环中下一个加油站相隔多少千米。
假设你有一辆邮箱足够大的车，初始时车里没有油。如果车从第 i 个加油站出发，最终可以回到这个加油站，那么第 i 个加油站就算良好出发点，否则就不算。
请返回长度为 N 的 boolean 数组 res，res[i] 代表第 i 个加油站是不是良好出发点。
'''


def stations(dis, oil):
    if not dis or not oil or len(dis) < 2 or len(dis) != len(oil): return
    res = [False] * len(dis)
    n = len(dis)
    # 起始点（大于 0）
    init = -1
    # 生成纯能数组
    for i in range(n):
        dis[i] = oil[i] - dis[i]
        if dis[i] > 0: init = i

    if init == -1: return res

    # 尝试以每个加油站为出发点
    for i in range(n):
        res[i] = circular(dis, i) >= 0

    return res


# 以 i 为出发点，尝试走完一圈。如果累计和为 0 ，退出
def circular(dis, i):
    if dis[i] < 0: return dis[i]
    n = len(dis)
    sum_value = dis[i]
    j = i + 1
    while j % n != i:
        sum_value += dis[j % n]
        if sum_value < 0: break
        j += 1
    return sum_value


def stations2(dis, oil):
    if not dis or not oil or len(dis) < 2 or len(dis) != len(oil): return
    n = len(dis)
    # 起始点（大于 0）
    init = -1
    # 生成纯能数组
    for i in range(n):
        dis[i] = oil[i] - dis[i]
        if dis[i] > 0: init = i

    return [False] * len(dis) if init < 0 else enlarge_area(dis, init)


def enlarge_area(dis, init):
    n = len(dis)
    res = [False] * n
    # 连通区起始点
    start = init
    # 连通区终点
    end = next_index(init, n)
    # 突破 start 需要油量
    need = 0
    # 剩余油量
    rest = 0

    # 以 init 为起始点，跑一圈
    while True:
        # 连通区 start 扩展（如果 end 无法突破，就扩展 start，所需的油都累计在 need 中）
        if dis[start] < need:
            # 如果 dis[start] 为负数，need 值增加
            # 如果 dis[start] 为正数，need 值减少
            need -= dis[start]
        else:
            # 将 need 的累积的油计算到 rest
            rest += dis[start] - need
            # 重置 need
            need = 0
            # end 连续突破
            while rest >= 0 and end != start:
                rest += dis[end]
                end = next_index(end, n)

            # 如果 end 连续突破后，rest 还有剩余，说明是 end == start 的条件跳出循环的，已经跑了一圈了。
            # 跑过一圈后，rest >= 0 油有剩余，说明以 start 是良好起始点
            # 跑过一圈后，rest < 0 油没有剩余，说明没有一个良好起始点，直接返回
            if rest >= 0:
                res[start] = True
                # 寻找其他的良好起始点
                # 所有能正常能达到 start 的加油站都是良好起始点
                # 所有从 start 上一个节点开始一路向上寻找能正常穿过 start 的加油站，并将对应 res 设置为 True
                connect_good(dis, last_index(start, n), init, res)
                # 已经跑了一圈了，其他良好起始点也寻找完毕，任务完成，跳出。
                break
        start = last_index(start, n)
        if start == init or start == last_index(end, n):
            break
    return res


def connect_good(dis, start, init, res):
    need = 0
    n = len(dis)
    while start != init:
        # 如果当前节点 start 无法穿越，用 need 记录所需要油，继续向上寻找
        if dis[start] < need:
            need -= dis[start]
        else:
            # 成功穿越
            res[start] = True
            need = 0
        start = last_index(start, n)


# 数组需要循环访问，需要在两个端点做特殊处理
# 获取 index 前一个索引
def last_index(index, size):
    return size - 1 if index == 0 else index - 1


# 获取 index 后一个索引
def next_index(index, size):
    return 0 if index == size - 1 else index + 1


import random


def check():
    for _ in range(100):
        n = int(random.random() * 5) + 1
        oil = [int(random.random() * 5) + 1 for _ in range(n)]
        dis = [int(random.random() * 5) + 1 for _ in range(n)]

        # print(oil, dis)
        res = stations(dis[:], oil[:])
        res2 = stations2(dis[:], oil[:])

        if res != res2:
            print("ERROR", "res=", res, "res2=", res2, "oil=", oil, "dis=", dis)
    print("Nice")


check()

oil = [5, 1]
dis = [1, 5]

# for i in range(len(dis)):
#     dis[i] = oil[i] - dis[i]
#     if dis[i] > 0:
#         init = dis[i]

# print(dis)
# res= [False, False, False, False] res2= [False, True, False, False] o
# print(enlarge_area2(dis, 1))
# print(dis)
print(stations(dis, oil))

# print(oil)
# print(dis)
