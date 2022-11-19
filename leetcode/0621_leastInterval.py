# coding:utf-8

'''
给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。

然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的最短时间。

示例 1：

输入: tasks = ["A","A","A","B","B","B"], n = 2
输出: 8
执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
注：

任务的总个数为 [1, 10000]。
n 的取值范围为 [0, 100]。
'''


def leastInterval(tasks, n):
    sleep_map = dict()
    ready_map = set(task for task in tasks)
    task_count = dict()
    for item in tasks:
        if item not in task_count:
            task_count[item] = 0
        task_count[item] += 1

    result = []
    i = 0
    while i < len(tasks):
        if not ready_map:
            result.append(None)
        else:
            task = ready_map.pop()
            result.append(task)
            if task_count[task] == 1:
                task_count.pop(task)
            else:
                task_count[task] = task_count[task] - 1
                sleep_map[task] = n + 1
            i += 1
        for k, v in sleep_map.items():
            if v - 1 == 0:
                ready_map.add(k)
                sleep_map.pop(k)
            sleep_map[k] = v - 1
    print result
    return len(result)


assert 8, leastInterval(["A", "A", "A", "B", "B", "B"], 2)

assert 16, leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)

print leastInterval(["A", "B", "C", "A", "B"], 2)
