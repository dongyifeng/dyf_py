def ways_to_step(n):
    if n < 3: return n
    if n == 3: return 4

    return (ways_to_step(n - 1) + ways_to_step(n - 2) + ways_to_step(n - 3)) % 1000000007


def ways_to_step2(n):
    if n < 3: return n
    if n == 3: return 4

    s1 = 1
    s2 = 2
    s3 = 4
    for i in range(3, n):
        s4 = (s1 + s2 + s3) % 1000000007
        s1 = s2
        s2 = s3
        s3 = s4
    return s4


print(ways_to_step2(61))
print(ways_to_step(3))
