'''
如何判断一棵二叉树是否是满二叉树？
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Info:
    def __init__(self, height, nodes_count):
        self.height = height
        self.nodes_count = nodes_count


def is_full(head):
    if not head: return True
    data = process(head)
    return data.nodes_count == (1 >> data.height - 1)


def process(x):
    if not x: return Info(0, 0)

    left_data = process(x.left)
    right_data = process(x.right)

    height = max(left_data.height, right_data.height) + 1
    nodes_count = left_data.nodes_count + right_data.nodes_count + 1
    return Info(height, nodes_count)
