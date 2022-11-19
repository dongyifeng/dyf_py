def unique_paths(m, n):
    matrix = [[0] * (n + 1)] * (m + 1)
    matrix[1][1] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
    return matrix[-1][-1]


def unique_paths2(m, n):
    array = [0] * (m + 1)
    array[1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            array[j] = array[j - 1] + array[j]
    return array[-1]


print(unique_paths(3, 7))
print(unique_paths(3, 2))
print(unique_paths(7, 3))
print(unique_paths(3, 3))

print("-" * 100)

print(unique_paths2(3, 7))
print(unique_paths2(3, 2))
print(unique_paths2(7, 3))
print(unique_paths2(3, 3))
