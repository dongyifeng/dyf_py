# 给定一棵二叉树的头节点 head，任何两个节点之间都存在距离，返回整棵二叉树的最大距离。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Info:
    def __init__(self, height, distance):
        self.height = height
        self.distance = distance


def max_distance(head):
    return process(head).distance


def process(head):
    if not head:
        return Info(0, 0)

    left_info = process(head.left)
    right_info = process(head.right)

    height = max(left_info.height, right_info.height) + 1
    distance = max(max(left_info.distance, right_info.distance), left_info.height + right_info.height + 1)
    return Info(height, distance)
