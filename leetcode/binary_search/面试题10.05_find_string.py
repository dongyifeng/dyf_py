# 面试题 10.05. 稀疏数组搜索

def find_string(words, s):
    left = 0
    right = len(words) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)

        if words[mid] == "":
            while mid > left and words[mid] == "":
                mid -= 1

        if words[mid] == s: return mid
        if words[mid] > s:
            right = mid - 1
        else:
            left = mid + 1

    return -1

print(find_string(["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""],"ta"))
print(find_string(["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""],"ball"))