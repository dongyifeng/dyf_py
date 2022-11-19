import bisect

a = [1, 3, 5, 5, 7]
index = bisect.bisect_left(a, 2)
# 1
index2 = bisect.bisect_left(a, 4)
# 2
index3 = bisect.bisect_left(a, 5)
# 2
index4 = bisect.bisect_right(a, 5)
# 4

print(index)
print(index2)
print(index3)
print(index4)

# 将 2 插入 a
bisect.insort_left(a, 2)
print(a)
# 将 2 插入 a

bisect.insort_left(a, 5)
print(a)
bisect.insort_right(a, 5)

print(a)


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


a=[grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
print(a)