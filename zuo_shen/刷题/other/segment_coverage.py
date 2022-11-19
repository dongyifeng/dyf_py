'''
一条直线上有 n 个线段，第 i 个线段的坐标为$(x_1[i],x_2[i])$。请你计算出直线上重叠线段数量最多的地方，有多少个线段相互重叠？
'''


def max_level_count(arr):
    if not arr: return 0
    