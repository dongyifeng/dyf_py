'''
完美洗牌
'''


def perfect_shuffle(arr):
    mid = int(len(arr) / 2)

    left_0 = 0
    cur = mid
    last_data = arr[mid]

    # tmp = (right_0 ,arr[right_0])
    for i in range(1, mid + 1):

        if cur >= mid:
            cur = cur - (3 - i + 1)
            tmp = arr[cur]
            arr[cur] = last_data
            last_data = tmp

            cur = cur + i
            tmp = arr[cur]
            arr[cur] = last_data
            last_data = tmp
        else:
            cur = cur + i
            tmp = arr[cur]
            arr[cur] = last_data
            last_data=tmp

            cur = cur - (3 - i + 1)
            tmp = arr[cur]
            arr[cur] = last_data
            last_data = tmp

    # left = left_0 + i
    # right = right_0 - (3 - i + 1)
    # print(i, 3 - i + 1)
    # print("ssss", left, right)

    print(arr)


arr = ["a", "b", "c", "d", "e", "f"]
perfect_shuffle(arr)
