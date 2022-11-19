def maximal_square(matrix):
    row_count = len(matrix)
    column_count = len(matrix[0])
    res = [[int(matrix[i][j]) for j in range(column_count)] for i in range(row_count)]
    res.insert(0, [0] * column_count)
    for row in res:
        row.insert(0, 0)

    result = 0
    for i in range(1, row_count + 1):
        for j in range(1, column_count + 1):
            if matrix[i - 1][j - 1] == "1":
                res[i][j] = min(res[i - 1][j], res[i][j - 1], res[i - 1][j - 1]) + 1
                result = max(result, res[i][j])

    return result * result


def maximal_square2(matrix):
    row_count = len(matrix)
    column_count = len(matrix[0])
    array = [0] * (column_count + 1)

    result = 0
    for i in range(1, row_count + 1):
        left = 0
        left_top = 0
        for j in range(1, column_count + 1):
            if matrix[i - 1][j - 1] == "1":
                tmp = min(array[j], left_top, left) + 1
                left_top = array[j]
                array[j] = left = tmp
            else:
                left_top = array[j]
                array[j] = left = 0
            result = max(result, tmp)
        print(i, array, left, left_top)

    return result * result


matrix = [["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "0", "0"], ]
print(maximal_square(matrix))

matrix = [["1", "1", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["0", "0", "0", "0", "0"],
          ["1", "1", "1", "1", "1"],
          ["1", "1", "1", "1", "1"]]
print(maximal_square(matrix))

matrix = [["1"], ["0"], ["1"], ["1"], ["1"], ["1"], ["0"]]
print(maximal_square(matrix))

matrix = [["1"]]
print(maximal_square(matrix))
