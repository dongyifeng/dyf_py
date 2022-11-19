'''
如何判断一个二叉树是完全二叉树?
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_cbt(head):
    if not head: return True

    queue = [head]
    leaf = False
    while queue:
        node = queue.pop(0)
        left = node.left
        right = node.right

        # 如果遇到了不双全的节点之后，又发现当前节点居然有孩子
        if (leaf and (left or right)) \
                or (not left and right):
            return False

        if left:
            queue.append(left)
        if right:
            queue.append(right)

        if not left or not right:
            leaf = True

    return True
