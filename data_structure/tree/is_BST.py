'''
给定一棵二叉树的头节点 head，返回这棵二叉树是不是搜索二叉树 ?
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Info:
    def __init__(self, is_bst, max_value, min_value):
        self.is_bst = is_bst
        self.max_value = max_value
        self.min_value = min_value


def is_bst(head):
    return process(head).is_bst


def process(x):
    if not x: return

    left_data = process(x.left)
    right_data = process(x.right)

    min_value = x.val
    max_value = x.val

    if left_data:
        min_value = min(min_value, left_data.min_value)
        max_value = max(max_value, left_data.max_value)

    if right_data:
        min_value = min(min_value, right_data.min_value)
        max_value = max(max_value, right_data.max_value)

    is_bst = True
    # 排除
    if left_data and (not left_data.is_bst or left_data.max_value >= x.val):
        is_bst = False
    if right_data and (not right_data.is_bst or x.val >= right_data.max_value):
        is_bst = False

    return Info(is_bst, max_value, min_value)
