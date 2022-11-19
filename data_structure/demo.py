def print_all_sub_squences(string):
    process([], string, 0)


def process(char_array, string, i):
    if i == len(string):
        print(''.join(char_array))
        return

    # 不要 string[i]
    process(char_array, string, i + 1)
    # 拷贝数组
    char_array = char_array[:]
    # 要 string[i]
    char_array.append(string[i])
    process(char_array, string, i + 1)


print_all_sub_squences("abc")
