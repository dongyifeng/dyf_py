# 双指针
def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left, right]
        if sum < target:
            left += 1
        if sum > target:
            right -= 1


print(two_sum([1, 2, 4, 6, 10], 8))
print(two_sum([2, 3, 4], 6))
print(two_sum([-1, 0], -1))

# 二分查找
def two_sum2(numbers, target):
    n = len(numbers)
    for i in range(n):
        left = i + 1
        right = n - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            sum = numbers[mid] + numbers[i]
            if sum == target:
                return [i, mid]
            if sum < target:
                left = mid + 1
            if sum > target:
                right = mid - 1


print("-" * 100)
print(two_sum2([1, 2, 4, 6, 10], 8))
print(two_sum2([2, 3, 4], 6))
print(two_sum2([-1, 0], -1))
