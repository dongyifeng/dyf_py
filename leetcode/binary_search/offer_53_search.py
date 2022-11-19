'''
剑指 Offer 53 - I. 在排序数组中查找数字 I

统计一个数字在排序数组中出现的次数。
'''


def search(nums, target):
    left = 0
    right = len(nums) - 1
    pos = -1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if nums[mid] == target:
            pos = mid
            break
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if pos == -1: return 0

    res = 1
    left = mid - 1
    right = mid + 1
    while 0 <= left or right < len(nums):

        if 0 <= left and nums[left] == target:
            res += 1
            left -= 1
            continue
        if right < len(nums) and nums[right] == target:
            res += 1
            right += 1
            continue

        break
    return res


print(search([5, 7, 7, 8, 8, 10], 8))
print(search([5, 7, 7, 8, 8, 10], 6))
print(search([2, 2], 2))
print(search([1, 4], 4))
