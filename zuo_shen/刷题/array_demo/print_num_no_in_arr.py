'''
给定一个整数数组 A，长度为 n，有 1 <= A\[i] <= n, 切对于 【1，n】的整数，其中部分整数会重复出现而部分不会出现。实现算法找到【1，n】中所有未出现在 A 中的整数。

提示：尝试实现 O(n) 的时间复杂度和 O(1) 的空间复杂度（返回值不计入空间复杂度）。

输入：【1,3,4,3】

输出：2
'''


def print_num_no_in_arr(arr):
    if not arr or len(arr) < 2: return

    # 争取做到，i 位置上，放的数是 i + 1
    for num in arr:
        modify(num, arr)

    # i位置上的数不是 i+1，i+1 就是缺的数
    for i in range(len(arr)):
        if i + 1 != arr[i]:
            print(i + 1)


def modify(value, arr):
    while arr[value - 1] != value:
        tmp = arr[value - 1]
        arr[value - 1] = value
        value = tmp


print_num_no_in_arr([1, 3, 4, 3])
