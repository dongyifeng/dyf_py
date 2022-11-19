import copy


def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums: return []
    result = [[]]

    nums.sort()
    exist = set()
    for item in nums:
        for k in copy.deepcopy(result):
            k.append(item)
            t_k=tuple(k)
            if t_k in exist:
                continue
            exist.add(t_k)
            result.append(k)

    return result

print(subsets([1, 2, 3]))
print(subsets([1, 2, 2]))
print(subsets([4,4,4,1,4]))