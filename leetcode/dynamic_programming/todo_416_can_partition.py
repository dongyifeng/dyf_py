# 416. 分割等和子集

# TODO
def can_partition(nums):
    n = len(nums)
    if n < 2: return False
    s = sum(nums)
    if s % 2 != 0: return False
    left_sum = 0
    for num in sorted(nums):
        left_sum += num
        s -= num
        if s == left_sum: return True
    return False

#
# def can_partition2(nums):
#     n = len(nums)
#     if n < 2: return False
#     s = sum(nums)
#     if s % 2 != 0: return False
#
#     for margin in range(n / 2):
#
#
#
#
#
#     left_sum = 0
#     for num in sorted(nums):
#         left_sum += num
#         s -= num
#         if s == left_sum: return True
#     return False


# print(can_partition([1, 5, 11, 5]))
# print(can_partition([1, 2, 3, 5]))
print(can_partition([1, 1, 2, 2]))
