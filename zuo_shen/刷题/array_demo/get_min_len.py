'''
给定一个无序数组 arr，求出需要排序的最短子数组长度。
【例如】arr=【1,5,3,4,2,6,7】返回 4，因为只有【5,3,4,2】需要排序。
'''


def get_min_len(arr):
    if not arr: return 0
    min_value = arr[-1]
    no_min_index = -1
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > min_value:
            no_min_index = i
        else:
            min_value = min(min_value, arr[i])

    if no_min_index == -1: return 0

    max_value = arr[0]
    no_max_index = -1
    for i in range(1, len(arr)):
        if arr[i] < max_value:
            no_max_index = i
        else:
            max_value = max(max_value, arr[i])

    return no_max_index - no_min_index + 1


arr = [1, 5, 3, 4, 2, 8, 9]
print(get_min_len(arr))
# print(get_min_len2(arr))
