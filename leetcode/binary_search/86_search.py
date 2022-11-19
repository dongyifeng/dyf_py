# 81. 搜索旋转排序数组 II
def search(nums, target):
    for item in nums:
        if item == target: return True
    return False


#
# print(search([2, 5, 6, 0, 0, 1, 2], 0))
# print(search([2, 5, 6, 0, 0, 1, 2], 3))
print(search([1, 0, 1, 1, 1], 0))
# print(search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2))
