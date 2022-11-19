def radix_sort(nums):
    if len(nums) < 2: return
    l = len(str(max(nums)))

    i = 0
    while i < l:
        buckets = [[] for i in range(10)]
        for x in nums:
            buckets[int(x / (10 ** i)) % 10].append(x)

        print("buckets", buckets)

        nums.clear()
        for bucket in buckets:
            for y in bucket:
                nums.append(y)
        i += 1
        print("nums", nums)
    return nums


nums = [123, 23, 156, 34, 345, 678, 100]
print(radix_sort(nums))
