def find_kth_positive(arr, k):
    tmp = [arr[i] - (i + 1) for i in range(len(arr))]

    position = 0
    for i in range(len(arr)):
        if tmp[i] >= k:
            break
        position += 1

    print("position", position)
    if position == 0:
        return k

    return arr[position - 1] + (k - tmp[position - 1])


def find_kth_positive2(arr, k):
    position = 0
    for i in range(len(arr)):
        tmp = arr[i] - (i + 1)
        if tmp >= k:
            break
        position += 1

    print("position", position)
    if position == 0:
        return k

    tmp = arr[position - 1] - position
    print("position", position)
    return arr[position - 1] + (k - tmp)


import sys


def find_kth_positive3(arr, k):
    tmp = [arr[i] - (i + 1) for i in range(len(arr))]
    tmp.append(sys.maxsize)
    tmp.insert(0, -sys.maxsize)

    left = 0
    right = len(tmp) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if tmp[mid] == k:
            right = mid - 1
            break
        if tmp[mid] < k:
            left = mid + 1
        if tmp[mid] > k:
            right = mid - 1

    if right == 0:
        return k
    tmp = tmp[1:len(tmp) - 1]
    return arr[right - 1] + (k - tmp[right - 1])


print("result", find_kth_positive3([2, 3, 4, 7, 11], 5))
print("result", find_kth_positive3([1, 2, 3, 4], 2))
print("result", find_kth_positive3([1, 3], 1))
print("result", find_kth_positive3([3, 10], 1))
print("result", find_kth_positive3([1], 1))
print("result", find_kth_positive3([7, 13, 21, 25, 29, 32, 38, 45], 4))

print("-" * 10000)
print("result", find_kth_positive([2, 3, 4, 7, 11], 5))
print("result", find_kth_positive([1, 2, 3, 4], 2))
print("result", find_kth_positive([1, 3], 1))
print("result", find_kth_positive([3, 10], 1))
print("result", find_kth_positive([1], 1))
print("result", find_kth_positive([7, 13, 21, 25, 29, 32, 38, 45], 4))
# print("result", find_kth_positive3([2, 3, 4, 7, 11], 5))
# #
# # # # print("-"*100)
# print("result", find_kth_positive([1, 2, 3, 4], 2))
# print("result", find_kth_positive3([1, 2, 3, 4], 2))

#
# print("result",find_kth_positive([1, 3], 1))
# print("result",find_kth_positive3([1, 3], 1))
# #
# print("result",find_kth_positive([3, 10], 1))
# print("result",find_kth_positive3([3, 10], 1))
#
#
# # print(find_kth_positive2([1], 1))
#
# print("result", find_kth_positive2([7, 13, 21, 25, 29, 32, 38, 45], 4))
# print("result", find_kth_positive3([7, 13, 21, 25, 29, 32, 38, 45], 4))
