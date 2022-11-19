def check(matrix, mid):
    n = len(matrix)
    i = n - 1
    j = 0
    num = 0
    while i >= 0 and j < n:
        if matrix[i][j] <= mid:
            # 累加当前列
            num += i + 1
            j += 1
        else:
            i -= 1

    return num


def check2(matrix, mid):
    n = len(matrix)
    i = n - 1
    j = 0
    num = 0
    while i >= 0 and j < n:
        if matrix[i][j] <= mid:
            j += 1
        else:
            # 累加当前行
            num += j
            i -= 1

    return num


matrix = [
    [1, 3, 5, 7, 9, 11],
    [2, 4, 6, 8, 10, 12],
    [3, 5, 7, 9, 11, 13],
    [4, 6, 8, 10, 12, 14],
    [5, 7, 9, 11, 13, 15],
    [6, 8, 10, 12, 14, 16],
]
print(check2(matrix, 8))


def kth_smallest(matrix, k):
    left = matrix[0][0]
    right = matrix[-1][-1]

    while left <= right:
        mid = left + ((right - left) >> 1)

        num = check(matrix, mid)
        if num >= k:
            right = mid - 1
        else:
            left = mid + 1
    return left

# print(kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
# print(kth_smallest([[-5]], 1))
# print(kth_smallest([[1, 2], [1, 3]], 3))
