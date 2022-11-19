def can_partition(nums):
    if len(nums) < 2: return False
    if len(nums) == 2:
        return nums[0] == nums[1]
    num_sum = sum(nums)
    if num_sum % 2 != 0:
        return False

    middle_sum = int(num_sum / 2)
    middle = int(len(nums) / 2)
    print(middle_sum)
    for sub_list_len in range(1, middle + 1):
        for margin in range(len(nums) - sub_list_len - 1):
            if generate_list(nums, sub_list_len, margin, middle_sum):
                return True
    return False


def generate_list(nums, count, margin, target):
    for i in range(len(nums)):
        tmp = [nums[i]]
        for j in range(i + margin + 1, min(i + count + margin, len(nums))):
            tmp.append(nums[j])
        if len(tmp) == count:
            if target == sum(tmp):
                return True

    return False


import random


def generator_random_array(max_value, max_size):
    return [int(random.random() * max_value) + 1 for _ in range(int(random.random() * max_size))]


def check():
    max_value = 10
    max_size = 10
    for i in range(50):
        arr = generator_random_array(max_value, max_size)
        res1 = can_partition(arr)
        res2 = can_partition2(arr)
        if res1 != res2:
            print("ERROR", res1, res2, arr)
    print("OVER!")


# check()

# print(can_partition([1, 5, 11, 5]))
# print(can_partition([1, 2, 3, 5]))
# print(can_partition([1, 2]))
# print(can_partition([2, 2, 1, 1]))
print(can_partition([2, 6, 6, 7, 7, 7, 7, 10]))
print(can_partition2([2, 6, 6, 7, 7, 7, 7, 10]))

# print(generate_list([1, 5, 11, 5], 1, 0))
#
# print(generate_list([1, 5, 11, 5], 2, 0))
# print(generate_list([1, 5, 11, 5], 2, 1))
# print(generate_list([1, 5, 11, 5], 2, 2))
