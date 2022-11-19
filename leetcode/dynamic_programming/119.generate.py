def generate(num_rows):
    if num_rows <= 0: return [1]
    lash_row = [1]
    for i in range(1, num_rows+1):
        new_row = [1]
        for j in range(1, i):
            new_row.append(lash_row[j - 1] + lash_row[j])
        new_row.append(1)
        lash_row = new_row
    return lash_row


print(generate(1))
print(generate(2))
print(generate(3))
print(generate(5))
