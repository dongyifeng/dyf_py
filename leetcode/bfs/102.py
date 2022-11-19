class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    if not root: return []
    q = [(root, 0)]
    result = []
    while q:
        node, level = q.pop()
        if len(result) <= level:
            result.append([node.val])
        else:
            result[level].append(node.val)
        if node.right:
            q.append((node.right, level + 1))
        if node.left:
            q.append((node.left, level + 1))

    return result


root = TreeNode(val=3)
root.left = TreeNode(val=9)
root.right = TreeNode(val=20)
root.right.left = TreeNode(val=15)
root.right.right = TreeNode(val=7)

print(level_order(root))
