def manacher_demo(s):
    # 处理字符串
    s -> str #a#b#c#

    pArr=[]
    R = ?
    C = ?

    for i in range(len(str)):
        if i in R 外部：
            从 i 开始往两边暴力扩展;
            更新 R
            更新 C
        else:
            if i' 回文区彻底在 [L,R] 内：
                pArr[i]=pArr[i']
            elif i' 回文区有一部分在 [L,R] 内 :
                pArr[i] = R - i
            else:
                从 R 之外的字符开始，往外扩，然后确定 pArr[i] 的答案；
                第一步扩失败了，R 不变
                否则 R 变大