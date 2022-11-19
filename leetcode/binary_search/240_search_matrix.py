def search_matrix(matrix, target):
    for i in range(len(matrix)):
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if matrix[i][mid] == target:
                return True
            if matrix[i][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    return False


matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 5
print(search_matrix(matrix, target))

print("-"*10)
def search_matrix2(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    x = 0
    y = n - 1
    while x < m and y >= 0:
        print(matrix[x][y])
        if matrix[x][y] == target:
            return True
        if matrix[x][y] > target:
            y -= 1
        else:
            x += 1

    return False

matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 20
print(search_matrix2(matrix, target))

# target = 20
# print(search_matrix(matrix,target))
