class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root):
    if not root: return []
    stack = [(root, 0)]
    result = []
    while stack:
        node, level = stack.pop()
        if len(result) <= level:
            result.append([node.val])
        else:
            if level % 2 == 0:
                result[level].insert(0, node.val)
            else:
                result[level].append(node.val)

        if node.right:
            stack.insert(0, (node.right, level + 1))
        if node.left:
            stack.insert(0, (node.left, level + 1))

    return result


root = TreeNode(val=3)
root.left = TreeNode(val=9)
root.right = TreeNode(val=20)
root.right.left = TreeNode(val=15)
root.right.right = TreeNode(val=7)

print(zigzag_level_order(root))

root = TreeNode(val=1)
root.left = TreeNode(val=2)
root.right = TreeNode(val=3)
root.left.left = TreeNode(val=4)
root.right.right = TreeNode(val=5)

print(zigzag_level_order(root))
