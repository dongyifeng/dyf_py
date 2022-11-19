'''
小 Q 正在给一条长度为 n 的道路设计路灯安置方案。

为了让问题更简单，小 Q 把道路视为 n 个方案，需要照亮的地方用 “.” 表示，不需要照亮的障碍物格子用 “X” 表示。小 Q 现在需要在道路上设置一些
路灯，对于安置在 pos 位置的路灯，这栈路灯可以照亮 pos -1 ，pos ，pos + 1 这三个位置。小 Q 希望能安置尽量少的路灯照亮所有 “.” 区域，
希望你能帮他计算一下最少需要多少栈路灯。
'''

# 至少需要多少灯，可以把 . 都点亮
def min_light(s):
    i = 0
    light = 0
    n = len(s)
    while i < n:
        if s[i] == "X":
            i += 1
            continue
        light += 1
        if i + 1 == n:
            break

        i += 2 if s[i + 1] == "X" else 3
    return light


print(min_light(".XX..X...X.."))
