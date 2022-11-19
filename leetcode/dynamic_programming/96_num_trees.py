import math


def num_trees(n):
    if n <= 1: return 1
    return 1 + 2 ** (n - 1)


print(num_trees(3))
print(num_trees(1))

print()
