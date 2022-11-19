'''
给定一棵二叉树的头节点 head，返回这棵二叉树中最大的二叉搜索子树的头节点
'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Info:
    def __init__(self, is_all_sbt, max_value, min_value, max_head: TreeNode, max_sub_sbt_size):
        self.is_all_sbt = is_all_sbt
        self.max_value = max_value
        self.min_value = min_value
        self.max_head = max_head
        self.max_sub_sbt_size = max_sub_sbt_size


def max_sub_bst_head(head):
    if not head: return
    return process(head).max_head


def process(node: TreeNode):
    if not node: return

    left_info = process(node.left)
    right_info = process(node.right)

    max_sub_sbt_size = 0
    max_value = node.val
    min_value = node.val
    max_head = node

    if left_info:
        max_value = left_info.max_value
        min_value = left_info.min_value
        max_head = left_info.max_head
        max_sub_sbt_size = left_info.max_sub_sbt_size

    if right_info:
        max_head = right_info if max_sub_sbt_size < right_info.max_sub_sbt_size else max_head
        max_value = max(max_value, right_info.max_value)
        min_value = min(min_value, right_info.min_value)
        max_sub_sbt_size = max(left_info.max_sub_sbt_size, right_info.max_sub_sbt_size)

    is_all_sbt = False
    # 空树也是 SBT
    # (not left_info or (left_info.is_all_sbt and left_info.max_value < node.val)) ：左树为空 or (左树是SBT and left_info.max_value < node.val)
    # (not right_info or (right_info.is_all_sbt and right_info.min_value > node.val))：右树为空 or (右树是SBT and right_info.min_value > node.val)
    if (not left_info or (left_info.is_all_sbt and left_info.max_value < node.val)) and (
            not right_info or (right_info.is_all_sbt and right_info.min_value > node.val)):
        is_all_sbt = True
        max_head = node

    return Info(is_all_sbt, max_value, min_value, max_head, max_sub_sbt_size)
