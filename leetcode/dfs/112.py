class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def has_path_sum(root, target):
    sum = 0
    return has_path_sum2(root, target, sum)


def has_path_sum2(root, target, sum):
    if not root: return False
    sum += root.val
    if not root.left and not root.right:
        return sum == target

    return has_path_sum2(root.left, target, sum) or has_path_sum2(root.right, target, sum)


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

print(has_path_sum(root, 22))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(has_path_sum(root, 5))
