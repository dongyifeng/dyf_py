def climb_stairs(n):
    if n <= 3: return n
    return climb_stairs(n - 1) + climb_stairs(n - 2)


def climb_stairs2(n):
    if n <= 3: return n
    data = [i for i in range(3)] + [None] * (n - 3)
    for i in range(3, n):
        data[i] = data[i - 1] + data[i - 2]
    return data[-1]


def climb_stairs3(n):
    if n <= 3: return n
    prev_1 = 1
    prev_2 = 2
    for i in range(2, n):
        result = prev_1 + prev_2
        prev_1=prev_2
        prev_2=result
    return result




print(climb_stairs(3))
print(climb_stairs2(3))
print(climb_stairs3(3))
