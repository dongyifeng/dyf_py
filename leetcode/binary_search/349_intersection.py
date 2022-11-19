# 求交集
def intersection(nums1, nums2):
    return set(nums1) & set(nums2)


def intersection2(nums1, nums2):
    nums1_set = set(nums1)
    return set([item for item in nums2 if item in nums1_set])


class BloomFilter:
    def __init__(self, nums):
        self.data = 0
        for num in nums:
            self.add(num)

    def contains(self, num):
        return (self.data >> (num - 1)) & 1 == 1

    def add(self, num):
        self.data |= 1 << (num - 1)


def intersection2_1(nums1, nums2):
    bloom_filter = BloomFilter(nums1)
    return set([item for item in nums2 if bloom_filter.contains(item)])


def intersection3(nums1, nums2):
    nums1.sort()
    nums2.sort()
    index1 = 0
    index2 = 0
    result = set()
    while index1 < len(nums1) and index2 < len(nums2):
        if nums1[index1] == nums2[index2]:
            result.add(nums2[index2])
            index2 += 1
            index1 += 1
        elif nums1[index1] > nums2[index2]:
            index2 += 1
        elif nums1[index1] < nums2[index2]:
            index1 += 1
    return result


print(intersection2_1([1, 2, 2, 1], [2, 2]))
print(intersection2_1([4, 9, 5], [9, 4, 9, 8, 4]))
