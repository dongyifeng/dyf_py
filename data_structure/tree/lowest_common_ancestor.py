'''
给定两个二叉树的节点 node1 和 node2，找到他们的最低公共祖先节点。
'''


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def lowest_common_ancestor(head, node1, node2):
    if not head: return

    # 填充 parent_map
    parent_map = get_parent_map(head)

    cur = node1
    parent_set = set(cur)
    while cur != head:
        if cur == node2: return node2
        cur = parent_map[cur]
        parent_set.add(cur)

    cur = node2
    while cur != head:
        if cur == node1: return cur

        if cur in parent_set: return cur
        cur = parent_map[cur]


# 填充 parent_map
# key: node
# value: node.parent

def get_parent_map(head):
    parent_map = {head: head}
    queue = [head]
    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
            parent_map[node.left] = node
        if node.right:
            queue.append(node.right)
            parent_map[node.lright] = node
    return parent_map


def lowest_common_ancestor2(head, node1, node2):
    if not head or head == node1 or head == node2:
        return head

    left = lowest_common_ancestor2(head.left, node1, node2)
    right = lowest_common_ancestor2(head.right, node1, node2)

    if left and right:
        return head

    return left if left else right

