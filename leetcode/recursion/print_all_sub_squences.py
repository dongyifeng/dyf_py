'''
打印一个字符串的全部子序列，包括空字符串

'''


def print_all_sub_squences(string):
    process([], string, 0)


def process(char_array, string, i):
    if i == len(string):
        print(''.join(char_array))
        return

    process(char_array, string, i + 1)
    char_array = char_array[:]
    char_array.append(string[i])
    process(char_array, string, i + 1)


def print_all_sub_squences2(string):
    process2([s for s in string], 0)


def process2(char_array, i):
    if i == len(char_array):
        print(''.join(char_array))
        return

    # 要 char_array[i]
    process2(char_array, i + 1)

    # 不要 char_array[i]
    tmp = char_array[i]
    char_array[i] = ''
    process2(char_array, i + 1)
    # 还原 char_array
    char_array[i] = tmp


print_all_sub_squences("abc")

print("-" * 100)
print_all_sub_squences2("abc")


# str[ i... ] 范围上，所有的字符，都可以在 i 位置上，后续都去尝试
# str[ 0...i-1 ] 范围上，是之前做的选择
# 请把所有的字符串形成的全排列，加入到 res 里去
def print_all(string):
    if not string: return
    char_array = [s for s in string]
    res = set()
    process3(char_array, 0, res)
    return res


def process3(char_array, i, res):
    if i == len(char_array):
        res.add(''.join(char_array))
        return

    for j in range(i, len(char_array)):
        char_array[i], char_array[j] = char_array[j], char_array[i]
        process3(char_array, i + 1, res)
        char_array[i], char_array[j] = char_array[j], char_array[i]


print(print_all("aabc"))


def print_all2(string):
    if not string: return
    char_array = [s for s in string]
    res = []
    process4(char_array, 0, res)
    return res


def process4(char_array, i, res):
    if i == len(char_array):
        res.append(''.join(char_array))
        return

    # 字符串只有小写字母：也可以替换成 set
    seen = [False] * 26
    for j in range(i, len(char_array)):
        index = ord(char_array[j]) - ord("a")
        if not seen[index]:
            seen[index] = True
            char_array[i], char_array[j] = char_array[j], char_array[i]
            process4(char_array, i + 1, res)
            char_array[i], char_array[j] = char_array[j], char_array[i]


print(print_all2("aabc"))
