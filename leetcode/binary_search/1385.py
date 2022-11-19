def find_the_distance_value(arr1, arr2, d):
    arr2.sort()
    n = len(arr2)
    res = 0
    for item in arr1:
        lock = True
        for i in range(n):
            tmp = abs(item - arr2[i])
            if tmp <= d:
                lock = False
                break
        if lock:
            res += 1
    return res


def find_the_distance_value(arr1, arr2, d):
    arr2.sort()
    n = len(arr2)
    res = 0
    for item in arr1:
        lock = True

        left = 0
        right = len(arr2) - 1

        while left < right:
            mid = left + ((right - left) >> 1)
            if abs(item - arr2[mid]) <= d:
                lock = False
                break



        if lock:
            res += 1
    return res


print(find_the_distance_value([4, 5, 8], [10, 9, 1, 8], 2))
print(find_the_distance_value([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3))
print(find_the_distance_value([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6))

print(find_the_distance_value([4, -3, -7, 0, -10], [10], 69))
