# 排序 + hash 表
import collections


def check_if_exist1(arr):
    tmp = collections.Counter(arr)

    for item in arr:
        if item == 0 and tmp[2 * item] > 1:
            return True
        if item != 0 and tmp[2 * item] >= 1:
            return True
    return False


# 排序 + 二分查找
def check_if_exist(arr):
    arr.sort()

    for i in range(len(arr)):
        target = arr[i] * 2
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) >> 1
            if arr[mid] == target and mid != i:
                return True
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    return False


def check_if_exist2(arr):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] * 2 == arr[right]: return True
        if arr[left] * 2 > arr[right]: right -= 1
        if arr[left] * 2 < arr[right]: right -= 1

    return False


print(check_if_exist([10, 2, 5, 3]))
print(check_if_exist([7, 1, 14, 11]))
print(check_if_exist([3, 1, 7, 11]))
print(check_if_exist([0, 0]))
print(check_if_exist([-2, 0, 10, -19, 4, 6, -8]))
print(check_if_exist([-10, 12, -20, -8, 15]))
print(check_if_exist([-16, -13, 8]))

print("-" * 10)
print(check_if_exist1([10, 2, 5, 3]))
print(check_if_exist1([7, 1, 14, 11]))
print(check_if_exist1([3, 1, 7, 11]))
print(check_if_exist1([0, 0]))
print(check_if_exist1([-2, 0, 10, -19, 4, 6, -8]))
print(check_if_exist1([-10, 12, -20, -8, 15]))
print(check_if_exist1([-16, -13, 8]))
