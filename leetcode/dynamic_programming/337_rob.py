# 337. 打家劫舍 III
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rob(root):
    return max(robInternal(root))


def robInternal(root):
    if not root: return (0, 0)
    left_select, left_no_select = robInternal(root.left)
    right_select, right_no_select = robInternal(root.right)

    select = root.val + left_no_select + right_no_select
    no_select = max(left_select, left_no_select) + max(right_select, right_no_select)
    return (select, no_select)


root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(3)
root.right.right = TreeNode(1)
print(rob(root))
