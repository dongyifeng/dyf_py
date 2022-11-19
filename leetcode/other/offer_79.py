import copy


def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums: return []
    result = [[]]
    
    for item in nums:
        for k in copy.deepcopy(result):
            k.append(item)
            result.append(k)

    return result


print(subsets([1, 2, 3]))
print(subsets([1, 2, 2]))
