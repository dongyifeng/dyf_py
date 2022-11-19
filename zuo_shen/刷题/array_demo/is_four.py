def is_four(arr):
    count1 = count2 = count4 = 0

    for item in arr:
        if item % 4 == 0:
            count4 += 1
            continue
        if item % 2 == 0:
            count2 += 1
            continue
        count1 += 1

    # arr 全部是奇数
    if count1 == len(arr):
        return False

    if count1 == 0:
        return True

    # return count4 >= count1 - 1 + (1 if count2 > 0 else 0)
    return count4 >= count1 - (0 if count2 > 0 else 1)


# print(is_four([1, 2, 4]))
# print(is_four([1, 2, 2, 4]))
print(is_four([3, 3, 4]))
