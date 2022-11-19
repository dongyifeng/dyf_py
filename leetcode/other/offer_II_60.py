def top_k_qrequent(nums, k):
    qreq = {}
    for item in nums:
        qreq[item] = qreq.get(item, 0) + 1
    a = sorted(qreq.items(), key=lambda x: x[1], reverse=True)
    return [x for x, y in a[:k]]


# print(top_k_qrequent([3, 3, 3, 2, 2, 1], 2))

import heapq


def top_k_qrequent2(nums, k):
    qreq = {}
    for item in nums:
        qreq[item] = qreq.get(item, 0) + 1
    print(qreq)
    return [y for x, y in get_least_numbers([(y, x) for x, y in qreq.items()], k)]

    # a = sorted(qreq.items(), key=lambda x: x[1], reverse=True)
    # return [x for x, y in a[:k]]


def get_least_numbers(arr, k):
    if k <= 0: return []
    n = len(arr)
    if n <= k:
        return arr
    res = []
    for i in range(k):
        heapq.heappush(res, arr[i])

    for j in range(k, n):
        if res[0] < arr[j]:
            heapq.heappushpop(res, arr[j])
    return [item for item in res]


# print(top_k_qrequent2([3, 3, 3, 2, 2, 1], 2))
print(top_k_qrequent2([4, 1, -1, 2, -1, 2, 3], 2))
