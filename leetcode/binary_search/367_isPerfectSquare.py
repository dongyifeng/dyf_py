import math


def is_perfect_square(num):
    return math.pow(int(math.sqrt(num)), 2) == num


def is_perfect_square2(num):
    if  num==1:return True
    start = 2
    end = num
    while start <= end:
        mid = (start + end) >> 1
        tmp = mid * mid
        if tmp == num: return True
        if tmp < num:
            start = mid + 1
        else:
            end = mid - 1
    return False


print(is_perfect_square2(9))
print(is_perfect_square2(10))
