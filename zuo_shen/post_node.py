class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def get_successor_node(node, head):
    if not head or not node: return
    res = []
    inorder(head, res)
    for i in range(res):
        if res[i] == node:
            break
    if i >= len(res) - 1:
        return
    return res[i + 1]


def inorder(node, res):
    if node:
        inorder(node.left)
        res.append(node)
        inorder(node.right)


def get_successor_node2(node):
    if not node: return
    if node.right:
        return get_left_most(node.right)

    parent = node.parent
    while parent and parent.right == node:
        node = parent
        parent = node.parent
    return parent


def get_left_most(node):
    if not node: return
    while node.left:
        node = node.left
    return node


def get_successor_node3(node):
    if not node: return
    if node.left:
        return get_right_most(node.left)

    parent = node.parent
    while parent and parent.left == node:
        node = parent
        parent = node.parent
    return parent


def get_right_most(node):
    if not node: return
    while node.right:
        node = node.right
    return node