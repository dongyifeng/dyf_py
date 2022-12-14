# coding=utf-8
"翻转一棵二叉树"

'''
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 通过前序遍历翻转
def preInvertTree(root):
    if root is None: return
    root.right, root.left = root.left, root.right
    preInvertTree(root.left)
    preInvertTree(root.right)
    return root


# 通过中序遍历翻转
def inInvertTree(root):
    if root is None: return
    preInvertTree(root.left)
    root.right, root.left = root.left, root.right
    preInvertTree(root.left)
    return root


# 通过后序遍历翻转
def postInvertTree(root):
    if root is None: return
    preInvertTree(root.left)
    preInvertTree(root.left)
    root.right, root.left = root.left, root.right
    return root


# 通过层遍历翻转
def layerInvertTree(root):
    if root is None: return

    queue = [root]
    while queue:
        p = queue.pop(0)
        p.right, p.left = p.left, p.right
        if p.right: queue.append(p.right)
        if p.left: queue.append(p.left)
    return root
