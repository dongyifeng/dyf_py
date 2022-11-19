# 对数器

# 要测试的方法 a
def insertion_sort(array):
    if not array or len(array) < 2: return

    for i in range(len(array)):
        j = i - 1
        while j >= 0 and array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            j -= 1


# 标准方法 b
def expect(array):
    array.sort()


import random


def random_array_generator(max_size, max_value):
    size = int(random.random() * max_size)
    return [int(random.random() * max_value) - int(random.random() * max_value) for _ in range(size)]


def check():
    test_time = 100
    max_size = 100
    max_value = 100
    succeed = True
    for i in range(test_time):
        array1 = random_array_generator(max_size, max_value)
        array2 = array1[:]
        insertion_sort(array1)
        expect(array2)
        if array1 != array2:
            succeed = False
            break
    print("Nick" if succeed else "Fucking fucked")


array = [1, 4, 3, 2, 6, 5]
insertion_sort(array)
print("insertion_sort", array)

array = [1, 4, 3, 2, 6, 5]
expect(array)
print("expect", array)

# for i in range(100):
#     print(random_array_generator(10, 100))


check()
