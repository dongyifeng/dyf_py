def search_matrix(matrix, target):
    left = 0
    right = len(matrix) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if matrix[mid][0] == target:
            return True
        if matrix[mid][0] < target:
            left = mid + 1
        else:
            right = mid - 1
    row = left - 1

    left = 0
    right = len(matrix[row]) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if matrix[row][mid] == target:
            return True
        if matrix[row][mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
print(search_matrix(matrix, 3))

print(search_matrix(matrix, 13))
