def length_of_lis(nums):
    n = len(nums)
    if n < 2: return n
    array = [0] * n
    array[0] = 1

    for i in range(1, n):
        tmp = 1
        for j in range(i - 1, -1, -1):
            if nums[i] > nums[j]:
                tmp = max(tmp, array[j] + 1)
        array[i] = tmp
    return max(array)


print(length_of_lis2([10,9,2,5,3,7,101,18]))
print(length_of_lis2([4, 10, 4, 3, 8, 9]))
print(length_of_lis2([0, 1, 0, 3, 2, 3]))
print(length_of_lis2([7, 7, 7, 7, 7, 7, 7]))
