def breakfast_number(staple, drinks, x):
    staple.sort()
    drinks.sort()
    # print("staple:", staple)
    #
    # print("drinks:", drinks)

    res = 0
    end = len(drinks) - 1
    for i in range(len(staple)):
        if staple[i] >= x: break
        tmp = x - staple[i]
        for j in range(end, -1, -1):
            if drinks[j] <= tmp:
                break
        if staple[i] + drinks[j] <= x:
            res += (j + 1)
        end = j
    return res


def breakfast_number2(staple, drinks, x):
    staple.sort()
    drinks.sort()

    MOD = 1e9 + 7
    res = 0
    end = len(drinks) - 1
    for i in range(len(staple)):
        if staple[i] >= x: break
        tmp = x - staple[i]
        j = find(drinks[::], tmp, end)
        if staple[i] + drinks[j - 1] <= x:
            res += j
            end = j
            res %= MOD
    return res


import sys


def find(nums, k, end):
    if end < 0: return 0
    nums.insert(0, -sys.maxsize)
    nums.append(sys.maxsize)
    left = 0
    right = end + 2
    while left <= right:
        mid = left + ((right - left) >> 1)
        if nums[mid] > k and nums[mid - 1] <= k:
            break

        if nums[mid] > k:
            right = mid - 1
        else:
            left = mid + 1

    nums.remove(-sys.maxsize)
    nums.pop()
    return mid - 1


#
# find([2, 5, 5], 3)
# find([2, 5, 5], 1)
# find([2, 5, 5], 4)
# find([2, 5, 5], 5)
# print("find", find([2, 5, 5], 10))

#
print(breakfast_number([10, 20, 5], [5, 5, 2], 15))
print(breakfast_number([2, 1, 1], [8, 9, 5, 1], 9))
print(breakfast_number([7, 3, 4, 3, 9, 9, 10, 8, 8, 3], [7, 10, 6, 7, 5, 2, 8, 4, 5, 8], 5))

print("-" * 1000)
print("breakfast_number2", breakfast_number2([10, 20, 5], [5, 5, 2], 15))
print("breakfast_number2", breakfast_number2([2, 1, 1], [8, 9, 5, 1], 9))
print("breakfast_number2", breakfast_number2([7, 3, 4, 3, 9, 9, 10, 8, 8, 3], [7, 10, 6, 7, 5, 2, 8, 4, 5, 8], 5))
