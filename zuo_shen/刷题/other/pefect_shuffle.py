'''
完美洗牌

给定一个长度为偶数的数组 arr，长度记为 2*N。前 N 个为左部分，后 N 个为右部分。arr 就可以表示为
【L1，L2，...，Ln，R1，R2，...，Rn】，请将数组调整成  【R1，L1，R2，L2，...，Ln，Rn】的样子。
空间复杂度要求：O(1)
'''


def modify_index(i, length):
    if i <= int(length / 2): return 2 * i
    return 2 * (i - int(length / 2)) - 1


def modify_index2(i, length):
    return (2 * i) % (length + 1)


# 从 start 位置开始，向右 length 长度这一段，做下标续连推
# 出发位置（trigger）：1，,3，9...
def cycles(arr, start, length, k):
    # 找到每一个出发位置 trigger，一共 k 个
    # 每个 trigger 都进行下标连续推
    # 出发位置是从 1 开始计算的，而数组下标是 0 开始计算的
    i = 0
    trigger = 1
    while i < k:
        pre_value = arr[trigger + start - 1]
        cur = modify_index2(trigger, length)
        while cur != trigger:
            tmp = arr[cur + start - 1]
            arr[cur + start - 1] = pre_value
            pre_value = tmp
            cur = modify_index2(cur, length)

        arr[cur + start - 1] = pre_value
        trigger *= 3
        i += 1


def shuffle(arr):
    if not arr or len(arr) % 2 != 0: return
    proces(arr, 0, len(arr) - 1)


# 在 arr[left:right+1] 上做完美洗牌的调整
def proces(arr, left, right):
    # 切成一块一块的解决，每一块的长度满足 3^k-1
    while right > left - 1:
        length = right - left + 1
        base = 3
        k = 1

        # 计算小于等于 length 并且离 length 最近的，满足 3^k-1 的数
        # 也就是找到最大的 k，满足 3^k <= length
        while base <= int((length + 1) / 3):
            base *= 3
            k += 1

        # 当前要解决长度为 base - 1 的块，一半就是再除2
        half = int((base - 1) / 2)
        # left 和 right 的中点位置
        mid = int((left + right) / 2)
        # 要旋转的左部分为[L + half...mid], 右部分为arr[mid + 1..mid + half]
        # 注意在这里，arr下标是从 0 开始的
        rotate(arr, left + half, mid, mid + half)
        # 旋转完成后，从L开始算起，长度为base-1的部分进行下标连续推
        cycles(arr, left, base - 1, k)
        # 解决了前base - 1 的部分，剩下的部分继续处理
        left = left + base - 1


# arr[left:mid+1] 为左部分，arr[mid+1:right+1] 为右部分,左右部分互换
def rotate(arr, left, mid, right):
    reverse(arr, left, mid)
    reverse(arr, mid + 1, right)
    reverse(arr, left, right)


def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def shuffle2(arr):
    if not arr or len(arr) % 2 != 0: return
    res = []

    left = 0
    right = int(len(arr) / 2)
    while right < len(arr):
        res.append(arr[right])
        res.append(arr[left])
        left += 1
        right += 1

    for i in range(len(arr)):
        arr[i] = res[i]


def wiggle_sort(arr):
    if not arr: return
    # 假设这里是堆排序
    arr.sort()
    if len(arr) % 2 == 0:
        return shuffle(arr)
    return proces(arr, 1, len(arr) - 1)


def wiggle_sort2(arr):
    if not arr: return
    # 假设这里是堆排序
    arr.sort()
    if len(arr) & 1 == 1:
        proces(arr, 1, len(arr) - 1)

    shuffle(arr)
    for i in range(0, len(arr), 2):
        tmp = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = tmp


# print(shuffle(arr))
# print(arr)

import random


def check():
    for i in range(100):
        arr = [int(random.random() * 100) for _ in range(int(random.random() * 10) + 1)]
        arr1 = arr[:]
        arr2 = arr[:]
        shuffle(arr1)
        shuffle2(arr2)
        if arr1 != arr2:
            print("ERROR", arr, arr1, arr2)
    print("OVER")


check()

arr = [i for i in range(10)]
shuffle(arr)
print(arr)
arr2 = [i for i in range(10)]
shuffle2(arr2)
print(arr2)
