def hanoi(n):
    if n <= 0: return
    func(n, "左", "右", "中")


def func(i, start, end, other):
    if i == 1:
        print("Move 1 from " + start + " to " + end)
        return
    func(i - 1, start, other, end)
    print("Move " + str(i) + " from" + start + " to " + end)
    func(i - 1, other, end, start)


hanoi(3)
