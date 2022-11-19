def can_jump(nums):
    if len(nums) <= 1: return True
    n = len(nums)

    stack = [0]
    used = set()
    while stack:
        index = stack.pop()
        if index >= n - 1: return True
        if index in used: continue
        stack += [j + index for j in range(1, nums[index] + 1)]
        used.add(index)
    return False


print(can_jump([2, 3, 1, 1, 4]))
print(can_jump([2, 3, 1, 1, 0]))
print(can_jump([3, 2, 1, 0, 4]))
print(can_jump([0]))
print(can_jump([2, 0]))
print(can_jump([0, 2, 3]))
