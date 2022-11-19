# coding=utf-8
'''
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。
'''

'''
暴力求解：O(n^2)
不满足：时间要求
'''


def findDuplicate(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return nums[i]


'''
将 nums 排序，重复数据一定挨着的，从前向后对别上一个元素是否相等，如果相等，表示重复。
如果对数字进行排序，则任何重复的数字都将与排序后的数组相邻。
'''


def findDuplicate2(nums):
    nums = sorted(nums)
    for i in range(1, len(nums)):
        if nums[i - 1] == nums[i]:
            return nums[i]


'''
通过集合存储之前的出现过元素，当前元素判断存在集合中，如果存在，则表示重复。空间O(n)
不满足：空间 O(1) 的判断。
'''


def findDuplicate3(nums):
    nums_set = set()
    for i in range(len(nums)):
        if nums[i] in nums_set:
            return nums[i]
        nums_set.add(nums[i])


# 将二进制数据：bit 的 index 位设置为 1
def bitAdd(bit, index):
    return bit | 1 << (index - 1)


# 判断二进制数据：bit 的 index 位是否是 1
def exit(bit, index):
    return (bit >> (index - 1)) & 1 == 1


'''
将方案三中，字典替换为，bit 数，通过二进制位上是否为 1，表示其位对应的元素是否存在：比如：0100 表示：3 出现过。
'''


def findDuplicate4(nums):
    bit = 0
    for i in range(len(nums)):
        if (bit >> (nums[i] - 1)) & 1 == 1:
            return nums[i]
        bit |= 1 << (nums[i] - 1)


'''
快慢指针：时间：O(n)；空间：O（1）
0 到 n 个下标，即 key，值为1到n。那么一定 2 个下标对应的值一样，如果把值看做next指针，即值为其后继节点，那么一定有 2 个节点都指到了同一个节点。
这样的问题就跟链表里是否有环一样了，有环就是两个节点指到了同一个节点。
'''


def findDuplicate5(nums):
    fast = 0
    slow = 0
    # 寻找环的结点
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = 0
    while True:
        slow = nums[slow]
        fast = nums[fast]
        if slow == fast:
            break

    return fast


'''
二分查找：时间O(n logn)，空间:O(1)
关键：这道题的关键是对要定位的“数”做二分，而不是对数组的索引做二分。要定位的“数”根据题意在 1 和 n 之间，每一次二分都可以将搜索区间缩小一半。

以 [1, 2, 2, 3, 4, 5, 6, 7] 为例，一共有 8 个数，每个数都在 1 和 7 之间。1 和 7 的中位数是 4，遍历整个数组，统计小于 4 的整数的个数，
至多应该为 3 个，如果超过 3 个就说明重复的数存在于区间 [1,4) （注意：左闭右开）中；否则，重复的数存在于区间 [4,7]（注意：左右都是闭）中。这里小于
4 的整数有 4 个（它们是 1, 2, 2, 3），因此砍掉右半区间，连中位数也砍掉。以此类推，最后区间越来越小，直到变成 1 个整数，这个整数就是我们要找的重复的数。
'''


def findDuplicate6(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) >> 1
        counter = 0
        for item in nums:
            if item <= mid:
                counter += 1
        if counter > mid:
            right = mid
        else:
            left = mid + 1

    return left


# print findDuplicate4([1, 3, 4, 2, 2])
# print findDuplicate4([3, 1, 3, 4, 2])

# print findDuplicate([1, 3, 4, 2, 2])
# print findDuplicate([3, 1, 3, 4, 2])


# print findDuplicate2([1, 3, 4, 2, 2])
# print findDuplicate2([3, 1, 3, 4, 2])
#
# print findDuplicate3([1, 3, 4, 2, 2])
# print findDuplicate3([3, 1, 3, 4, 2])

# print findDuplicate5([1, 3, 4, 2, 2])
# print findDuplicate5([2, 5, 9, 6, 9, 3, 8, 9, 7, 1])

# print(findDuplicate6([3, 1, 3, 4, 2]))
# print(findDuplicate6([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]))

#
# def findDuplicate7(nums):
#     left = 0
#     right = len(nums) - 1
#     nums = sorted(nums)
#     print(nums)
#     while left < right:
#         mid = (left + right) >> 1
#         if nums[mid] < mid + 1:
#             right=mid-1
#         else:
#             left=mid+1
#
#     return nums[left]


def findDuplicate7(nums):
    low = 0
    high = len(nums)-1

    print(nums)
    while low < high:
        mid = (low + high) >> 1
        cut = get_count(mid, nums)
        if cut > mid:
            high = mid
        else:
            low = mid + 1

    return low


def get_count(target, nums):
    res = 0
    for item in nums:
        if item <= target:
            res += 1
    return res


print(findDuplicate5([1, 3, 4, 2, 2]))
print(findDuplicate5([3, 1, 3, 4, 2]))

# print(findDuplicate5([1, 3, 4, 2, 2]))
# print(findDuplicate5([3, 1, 3, 4, 2]))
#
# print(findDuplicate7([1, 3, 4, 2, 2]))
# print(findDuplicate7([3, 1, 3, 4, 2]))
#
# print(findDuplicate7([1, 3, 4, 2, 2]))
# print(findDuplicate7([3, 1, 3, 4, 2]))
#
# print(findDuplicate7([3, 1, 3, 4, 2]))
print(findDuplicate5([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]))
