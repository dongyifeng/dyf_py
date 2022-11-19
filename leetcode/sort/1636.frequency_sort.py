def frequency_sort(nums):
    tmp = dict()
    for item in nums:
        tmp[item] = tmp.get(item, 0) + 1

    res = []
    for value, count in sorted(tmp.items(), key=lambda x: (x[1], -x[0])):
        res += [value] * count
    return res


from collections import Counter
def frequency_sort2(nums):
    tmp = Counter(nums)

    res = []
    for value, count in sorted(tmp.items(), key=lambda x: (x[1], -x[0])):
        res += [value] * count
    return res

print(frequency_sort2([1, 1, 2, 2, 2, 3]))
print(frequency_sort2([2, 3, 1, 3, 2]))
print(frequency_sort2([-1, 1, -6, 4, 5, -6, 1, 4, 1]))
