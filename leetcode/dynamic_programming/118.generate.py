def generate(num_rows):
    if num_rows <= 1: return [[1]]
    result = [[1]]
    for i in range(1, num_rows):
        new_row = [1]
        for j in range(1,i):
            new_row.append(result[i-1][j - 1] + result[i-1][j])
        new_row.append(1)
        result.append(new_row)
    return result



print(generate(1))
print(generate(2))
print(generate(3))
print(generate(5))