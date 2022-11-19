def my_sqrt(x):
    left = 0
    right = x
    while left <= right:
        mid = left + ((right - left) >> 1)
        tmp = mid * mid
        if tmp == x:
            return mid
        if tmp < x:
            left = mid + 1
        else:
            right = mid - 1

    return left - 1



print(my_sqrt(4))
print(my_sqrt(6))
print(my_sqrt(8))
print(my_sqrt(9))
print(my_sqrt(10))
