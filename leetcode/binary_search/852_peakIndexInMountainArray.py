def peak_index_in_mountain_array(arr):
    i = 1
    while arr[i - 1] < arr[i]:
        i += 1
    return i - 1


def peak_index_in_mountain_array2(arr):
    left = 1
    right = len(arr) - 2
    while left <= right:
        mid = (left + right) >> 1
        if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
            return mid
        if arr[mid - 1] < arr[mid] and arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1


#
print(peak_index_in_mountain_array([0, 1, 0]))
print(peak_index_in_mountain_array([0, 2, 1, 0]))
print(peak_index_in_mountain_array([0, 10, 5, 2]))
print(peak_index_in_mountain_array([3, 4, 5, 1]))
print(peak_index_in_mountain_array([24, 69, 100, 99, 79, 78, 67, 36, 26, 19]))

print("-" * 100)

print(peak_index_in_mountain_array2([0, 1, 0]))
print(peak_index_in_mountain_array2([0, 2, 1, 0]))
print(peak_index_in_mountain_array2([0, 10, 5, 2]))
print(peak_index_in_mountain_array2([3, 4, 5, 1]))
print(peak_index_in_mountain_array2([24, 69, 100, 99, 79, 78, 67, 36, 26, 19]))
