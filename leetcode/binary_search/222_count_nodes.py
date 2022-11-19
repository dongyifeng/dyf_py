class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_nodes(root):
    if not root: return 0
    left = count_nodes(root.left)
    right = count_nodes(root.right)
    return left + right + 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)

print(count_nodes(root))
