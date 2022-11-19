'''
给定一个数组 arr ，长度为 N 且每个值都是正数，代表 N 个人的体重。再给定一个正数 limit ， 代表一艘船的载重。以下是坐船规则：

1. 每艘船最多只能做两人
2. 乘客的体重和不能超过 limit。

返回如果同时让这 N 个人过河最少需要几条船。
'''


def min_boat(arr, limit):
    arr.sort()
    res = left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[right] > limit: return -1

        res += 1
        if left == right:
            break
        if arr[left] + arr[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
    return res


print(min_boat([1, 1, 3, 3, 3, 4, 4, 5, 5, 5, 5, 7, 7, 9, 9, 9], 10))
print(min_boat([1, 1, 3, 3, 3, 4, 4, 5, 5, 5, 7, 7, 9, 9, 9], 10))
