def peak_index_in_mountain_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] < arr[left + 1]:
            left += 1
        if arr[right - 1] > arr[right]:
            right -= 1
    return left


def peak_index_in_mountain_array2(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return mid
        if arr[mid] < arr[mid + 1] and arr[mid] > arr[mid - 1]:
            left = mid + 1
        else:
            right = mid - 1
    return left


print(peak_index_in_mountain_array2([0, 1, 0]))
print(peak_index_in_mountain_array2([1, 3, 5, 4, 2]))
print(peak_index_in_mountain_array2([0, 10, 5, 2]))
print(peak_index_in_mountain_array2([3, 4, 5, 1]))
print(peak_index_in_mountain_array2([24, 69, 100, 99, 79, 78, 67, 36, 26, 19]))
