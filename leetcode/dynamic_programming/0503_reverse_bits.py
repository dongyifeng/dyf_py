def reverse_bits(num):
    str_num = str(bin(num))[2:]
    print(str_num)
    one_len = 0
    one_len_list = []
    for i in range(len(str_num)):
        if str_num[i] == "1":
            one_len += 1
        else:
            one_len_list.append(one_len)
            one_len = 0
    if one_len > 0:
        one_len_list.append(one_len)

    if len(one_len_list) == 1: return one_len_list[0] + 1

    res = 0
    for i in range(1, len(one_len_list)):
        res = max(one_len_list[i - 1] + one_len_list[i] + 1, res)
    return res


print(reverse_bits(1775))
print(reverse_bits(7))
print(reverse_bits(0))
