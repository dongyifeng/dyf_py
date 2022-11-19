class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_width(head):
    if not head: return
    queue = [head]
    # 节点：节点所属的层
    level_map = {head: 1}
    # 当前节点所属的层
    cur_level = 1
    # 当前层的节点数
    cur_level_nodes = 0
    res = 0
    # 层遍历
    while queue:
        cur = queue.pop(0)
        cur_node_level = level_map.get(cur)
        if cur.left:
            level_map[cur.left] = cur_node_level + 1
            queue.append(cur.left)
        if cur.right:
            level_map[cur.right] = cur_node_level + 1
            queue.append(cur.right)

        if cur_node_level == cur_level:
            cur_level_nodes += 1
        else:
            res = max(res, cur_level_nodes)
            cur_level_nodes = 1
            cur_level += 1
    return max(res, cur_level_nodes)


def max_width_no_map(head):
    if not head: return
    queue = [head]
    # 当前层，最右节点
    cur_end = head
    # 下一层，最右节点
    next_end = None
    # 当前层的节点数
    cur_level_nodes = 0
    res = 0
    # 层遍历
    while queue:
        cur = queue.pop(0)
        if cur.left:
            queue.append(cur.left)
            next_end = cur.left
        if cur.right:
            queue.append(cur.right)
            next_end = cur.right

        cur_level_nodes += 1
        # 当 cur 是最右节点时，next_end 正好是下一层的最右节点
        if cur == cur_end:
            res = max(res, cur_level_nodes)
            cur_level_nodes = 0
            cur_end = next_end
    return res


head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)
head.right.left = TreeNode(6)
head.right.right = TreeNode(7)

head.left.right.left = TreeNode(8)
head.left.right.right = TreeNode(9)

print(max_width(head))
print(max_width_no_map(head))
