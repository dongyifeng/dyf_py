# 435. 无重叠区间

import sys
def erase_overlap_intervals(intervals):
    res = 0
    last_right = -sys.maxsize
    tmp = []
    for left, right in sorted(intervals, key=lambda item: item[1]):
        if left < last_right: continue
        res += 1
        last_right = right
        tmp.append((left,right))

    print(tmp)
    return len(intervals) - res


print(erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
print(erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]))
print(erase_overlap_intervals([[1, 2], [2, 3]]))
print(erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [-100, -2], [5, 7]]))
