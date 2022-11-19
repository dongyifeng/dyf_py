'''
来源：华为

给定两个数组 A 和 B，长度都是 N
A[i] 不可以在 A 中与其他数交换，只可以选择和 B[i] 交换（0<= i < n）
你的目的是让 A 有序，返回你能不能做到
'''


def can_sort(A, B):
    if not A or len(A) < 2:
        return True
    return process(A, B, 1, True) or process(A, B, 1, False)


def process(A, B, index, swap):
    if len(A) == index:
        return True

    pre = B[index - 1] if swap else A[index - 1]
    # 不交换
    p1 = False if pre > A[index] else process(A, B, index + 1, False)
    # 交换
    p2 = False if pre > B[index] else process(A, B, index + 1, True)

    return p1 or p2


print(can_sort([3, 2, 1, 5, 6], [0, 6, 4, 3, 1]))
