class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Info:
    def __init__(self, is_balaced, height):
        self.is_balaced = is_balaced
        self.height = height


def is_balanced(head):
    return process(head).is_balaced


def process(head):
    # 空树是平衡二叉树
    if not head:
        return Info(True, 0)
    # 向左树和右树收集信息
    left_info = process(head.left)
    right_info = process(head.right)

    # 根据子树的信息，组合出自己的信息
    height = max(left_info.height, right_info.height) + 1
    is_balance = True
    if not left_info.is_balaced or right_info.is_balaced or abs(left_info.height - right_info.height) > 2:
        is_balance = False
    return Info(is_balance, height)
