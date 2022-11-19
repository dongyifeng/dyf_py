def find_right_interval(intervals):
    intervals_map = {}
    # 记录区间索引位置
    for i in range(len(intervals)):
        intervals_map[intervals[i][0]] = i
    intervals.sort()

    n = len(intervals)
    res = [-1] * n
    for i in range(n):
        # 二分查找
        target = intervals[i][1]
        left = i
        right = n - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if intervals[mid][0] >= target:
                res[intervals_map[intervals[i][0]]] = intervals_map[intervals[mid][0]]
                right = mid - 1
            else:
                left = mid + 1
    return res


intervals = [[3, 4], [2, 3], [1, 2]]
print(find_right_interval(intervals))
# intervals = [[1, 4], [2, 3], [3, 4]]
# print(find_right_interval(intervals))
# intervals = [[1, 2]]
# print(find_right_interval(intervals))
