#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Info:
    def __init__(self, is_all_bst, max_sub_sbt_size):
        self.is_all_bst = is_all_bst
        self.max_sub_sbt_size = max_sub_sbt_size


def max_sub_bst_size(head):
    if not head: return 0
    return process(head).max_sub_sbt_size


def process(X):
    if not X: return
    left_info = process(X.left)
    right_info = process(X.right)

    max_sub_sbt_size = 0
    if left_info:
        max_sub_sbt_size = left_info.max_sub_sbt_size

    if right_info:
        max_sub_sbt_size = max(max_sub_sbt_size, left_info.max_sub_sbt_size)

    is_all_bst = False
    if left_info.is_all_bst if left_info else True \
    and right_info.is_all_bst if right_info else True\
    and X.left.value < X.vale if X.left else True \
    and X.right.value > X.vale if X.right else True:
        is_all_bst = True
        max_sub_sbt_size = left_info.max_sub_sbt_size if left_info else 0
        + right_info.max_sub_sbt_size if right_info else 0
        + 1
    return Info(is_all_bst, max_sub_sbt_size)
