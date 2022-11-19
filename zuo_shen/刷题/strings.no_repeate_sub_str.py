def max_unique(string):
    map = {string[0]: 0}
    array = [1] * len(string)
    max_value = 1

    for i in range(1, len(string)):
        if string[i] not in map or map[string[i]] < i - 1 - array[i - 1]:
            array[i] = array[i - 1] + 1
        else:
            array[i] = i - map[string[i]]

        max_value = max(max_value, array[i])
        map[string[i]] = i

    return max_value


def max_unique2(string):
    map = {string[0]: 0}
    max_value = 1
    pre = -1

    for i in range(1, len(string)):
        pre = max(pre, map.get(string[i], -1))
        max_value = max(max_value, i - pre)
        map[string[i]] = i

    return max_value


print(max_unique("abcabcbb"))
print(max_unique("bbbbb"))
print(max_unique("pwwkew"))

print("-" * 1000)

print(max_unique2("abcabcbb"))
print(max_unique2("bbbbb"))
print(max_unique2("pwwkew"))
