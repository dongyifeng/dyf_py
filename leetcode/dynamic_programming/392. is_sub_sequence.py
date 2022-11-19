def is_sub_sequence(s, t):
    if len(s) > len(t): return False
    s_i = 0
    for i in range(len(t)):
        if s_i==len(s):return True
        if t[i] == s[s_i]:
            s_i += 1
    return s_i == len(s)


print(is_sub_sequence("abc", "ahbgdc"))
print(is_sub_sequence("axc", "ahbgdc"))
