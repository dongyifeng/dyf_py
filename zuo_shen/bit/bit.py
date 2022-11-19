def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(a, b)


def swap2(array, a, b):
    array[a] = array[a] ^ array[b]
    array[b] = array[a] ^ array[b]
    array[a] = array[a] ^ array[b]
    print(array)


swap(2, 2)
swap2([1, 2], 1, 1)


def find_word(array):
    res = 0
    for item in array:
        res ^= item
    return res


print(find_word([1, 1, 2, 3, 3, 4, 4]))


def find_word2(array):
    eor = 0
    for item in array:
        eor ^= item

    right_one = eor & (~eor + 1)
    only_one = 0
    for item in array:
        if right_one & item == 0:
            only_one ^= item

    return only_one, eor ^ only_one


print(find_word2([1, 1, 2, 2, 3, 3, 4, 5, 6, 6]))


def print_bit(num):
    for i in range(31, -1, -1):
        print("0" if num & (1 << i) == 0 else "1", end="")
    print()


print_bit(4)


def add(num1, num2):
    res = num1 ^ num2
    k = num1 & num2

    if k != 0:
        res = add(res, k << 1)

    return res


def add2(num1, num2):
    sum = num1
    while num2 != 0:
        sum = num1 ^ num2
        num2 = (num1 & num2) << 1
        num1 = sum
    return sum


def jian(num1, num2):
    return add(num1, (~num2 + 1))


print("add", add2(7, -6))
# print((~6 + 1))
print("jian", jian(7, 6))
