class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(root, target):
    prefix_sum = [0]
    rst = []

    def dfs(root, target, prefix_sum):
        if not root: return 0
        prefix_sum.append(prefix_sum[-1] + root.val)
        rst.append(condition(prefix_sum, target))

        dfs(root.left, target, prefix_sum[::])
        dfs(root.right, target, prefix_sum[::])

    dfs(root, target, prefix_sum)
    return sum(rst)


def condition(prefix_sum, target):
    if not prefix_sum: return 0
    if len(prefix_sum) == 1:
        return 1 if prefix_sum[0] == target else 0

    rst = 0
    if prefix_sum[-1] == target:
        rst += 1
    for i in range(1, len(prefix_sum) - 1):
        if prefix_sum[-1] - prefix_sum[i] == target:
            rst += 1

    return rst


# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(-3)
#
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(2)
# root.right.right = TreeNode(11)
#
# root.left.left.left = TreeNode(2)
# root.left.left.right = TreeNode(-2)
# root.left.right.right = TreeNode(1)
#
# print(path_sum(root, 8))
#
# root = TreeNode(0)
# root.left = TreeNode(1)
# root.right = TreeNode(1)
#
# print(path_sum(root, 1))


# root = TreeNode(5)
# root.left = TreeNode(4)
# root.right = TreeNode(8)
#
# root.left.left = TreeNode(11)
# root.left.left.left = TreeNode(7)
# root.left.left.right = TreeNode(2)
#
# root.right.right = TreeNode(4)
# root.right.left = TreeNode(13)
#
# root.right.right.right = TreeNode(1)
# root.right.right.left = TreeNode(5)

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)

root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(-1)

root.left.left.left = TreeNode(0)
root.left.left.right = TreeNode(1)
root.left.right.left = TreeNode(-1)
root.left.right.right = TreeNode(0)
root.right.left.left = TreeNode(-1)
root.right.left.right = TreeNode(0)
root.right.right.left = TreeNode(1)
root.right.right.right = TreeNode(0)

print(path_sum(root, 2))
