# 350. 两个数组的交集 II

def intersection3(nums1, nums2):
    nums1.sort()
    nums2.sort()
    index1 = 0
    index2 = 0
    result = list()
    while index1 < len(nums1) and index2 < len(nums2):
        if nums1[index1] == nums2[index2]:
            result.append(nums2[index2])
            index2 += 1
            index1 += 1
        elif nums1[index1] > nums2[index2]:
            index2 += 1
        elif nums1[index1] < nums2[index2]:
            index1 += 1
    return result


print(intersection3([1, 2, 2, 1], [2, 2]))
print(intersection3([4, 9, 5], [9, 4, 9, 8, 4]))
