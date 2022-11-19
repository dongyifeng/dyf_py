'''
请把一段纸条竖着放在桌子上，然后从纸条的下边向上对折 1 次，压出折痕后展开。此时折痕是凹下去的。即折痕凸起的方向指向纸条的背面。如果从纸条的下边向上方连续对折 2  次，压出的折痕后展开，此时有 3 条折痕，从上到下依次是：下折痕，下折痕，上折痕。
给定一个输入参数 N，代表纸条从下边向上方连续对折 N 次。请从上向下打印所有折痕的方向。
例如：N = 1 时，打印 down
例如：N = 2 时，打印 down down up
'''


def print_all_folds(N):
    print_process(1, N, True)


# i 是节点的层数
# N 二叉树总共的层数
# down == true 凹；down == false 凸
def print_process(i, N, down):
    if i > N: return
    print_process(i + 1, N, True)
    print("凹" if down else "凸")
    print_process(i + 1, N, False)


print_all_folds(3)
