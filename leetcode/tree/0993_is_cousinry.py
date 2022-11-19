'''
993. 二叉树的堂兄弟节点

在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。

如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。

我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。

只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。

示例 1：

输入：root = [1,2,3,4], x = 4, y = 3
输出：false


示例 2：
输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
输出：true

示例 3：
输入：root = [1,2,3,null,4], x = 2, y = 3
输出：false
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find(root, x):
    stack = [(root, None)]
    depth = 0
    while stack:

        tmp = []
        for node, parent in stack:
            if node.val == x:
                return depth, parent
            if node.left: tmp.append((node.left,node))
            if node.right: tmp.append((node.right,node))
        depth += 1
        stack = tmp
    return None


def isCousins(root, x: int, y: int) -> bool:
    x_depth, x_parent = find(root, x)
    y_depth, y_parent = find(root, y)
    print("x_parent", x_depth, x_parent.val)
    print("y_parent", y_depth, y_parent.val)

    if x_depth and y_depth and x_depth == y_depth and x_parent and y_parent and x_parent != y_parent:
        return True
    return False


def maxDepth(root):
    if not root: return 0

    l_depth = maxDepth(root.left)
    r_depth = maxDepth(root.right)
    return max(l_depth, r_depth) + 1


def maxDepth2(root):
    if not root: return 0
    res = 0
    stock = [root]
    while stock:
        tmp = []
        for node in stock:
            if node.left: tmp.append(node.left)
            if node.right: tmp.append(node.right)
        stock = tmp
        res += 1

    return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

print(isCousins(root, 4, 3))

# print(maxDepth(root))
# print(maxDepth2(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(5)

# print(maxDepth(root))
# print(maxDepth2(root))

print(isCousins(root, 4, 5))

print(isCousins(root, 2, 3))
