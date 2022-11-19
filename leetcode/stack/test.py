# coding=utf-8
print('''
给定数据 A = [5,3,7,4],返回数组L，L[i] 表示：第i个数向左遍历的第一个比它小的元素的位置
A = [ 5,3,7,4 ]
L : [ 0,0,2,2 ]
''')


def run(a):
    l = [0] * len(a)
    stack = []
    for i in range(len((a))):
        # 找到 stack 顶元素比 a[i] 小的第一个元素
        while len(stack) > 0 and a[stack[-1]] > a[i]:
            stack.pop()
        # 如果不为空，栈顶元素就是，a[i] 左边第一个比它小的元素的位置
        if len(stack) > 0:
            l[i] = stack[-1] + 1
        # 由于 a[stack.peek()] < a[i] ,此处 push 保持了单调递增的性质
        stack.append(i)
    return l


print(run([5, 3, 7, 4]))
