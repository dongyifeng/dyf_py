import heapq


def get_least_numbers(arr, k):
    if k <= 0: return []
    n = len(arr)
    if n <= k:
        return arr
    res = []
    for i in range(k):
        heapq.heappush(res, -arr[i])

    for j in range(k, n):
        if -res[0] > arr[j]:
            heapq.heappushpop(res, -arr[j])
    return [-item for item in res]


# print(get_least_numbers([4, 5, 1, 6, 2, 7, 3, 8], 4))
print(get_least_numbers([0, 0, 0, 2, 0, 5], 0))
