import sys


def manacher_str(s):
    return "#" + "#".join(s) + "#"


def manacher_demo(s):
    if not s: return 0
    # 中心
    C = -1
    # 最右回文右边界 + 1
    R = -1
    res = sys.maxsize
    p_arr = [0] * len(s)
    s = manacher_str(s)
    n = len(s)

    # 每一个位置都求回文半径
    for i in range(n):
        # i 至少的回文区域(不需要验证)，先给 p_arr[i]
        # 2C - i = i'
        p_arr[i] = min(p_arr[2 * C - i], R - i) if R > i else 1

        # 从不需要验证的区域，向外验证
        while i + p_arr[i] < n and i - p_arr[i] > -1:
            if p_arr[i + p_arr[i]] != s[i - p_arr[i]]:
                break
            p_arr[i] += 1

        if i + p_arr[i] > R:
            R = i + p_arr[i]
            C = i

        res = max(res, p_arr[i])
    return res - 1
