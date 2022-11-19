# 4. 寻找两个正序数组的中位数
# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
# 进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

# 示例 1：
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2

# 示例 2：
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

# 示例 3：
# 输入：nums1 = [0,0], nums2 = [0,0]
# 输出：0.00000
#
# 示例 4：
# 输入：nums1 = [], nums2 = [1]
# 输出：1.00000
#
# 示例 5：
# 输入：nums1 = [2], nums2 = []
# 输出：2.00000
import sys


def find_median_sorted_arrays(nums1, nums2):
    total = len(nums1) + len(nums2)

    index = int(total / 2)
    if total % 2 == 0:
        index -= 1
    nums1.append(sys.maxsize)
    nums2.append(sys.maxsize)

    i = j = 0
    s1 = None
    for k in range(len(nums1) + len(nums2)):
        if nums1[i] > nums2[j]:
            j += 1
            if k == index:
                s1 = nums2[j - 1]
                break

        else:
            i += 1
            if k == index:
                s1 = nums1[i - 1]
                break

    if total % 2 == 1: return s1

    s2 = nums2[j] if nums1[i] > nums2[j] else nums1[i]
    return (s1 + s2) / 2


print(find_median_sorted_arrays([1, 3], [2]))
print(find_median_sorted_arrays([], [1]))
print(find_median_sorted_arrays([2], []))
#
print(find_median_sorted_arrays([1, 2], [3, 4]))

print(find_median_sorted_arrays([], [2, 3]))
print(find_median_sorted_arrays([1, 2], [-1, 3]))
