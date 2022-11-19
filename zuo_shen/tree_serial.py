# 二叉树序列化与反序列化

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_serial(head):
    res = []
    pres(head, res)
    return res


def pres(head, res):
    if not head:
        res.append(None)
    else:
        res.append(head.val)
        pres(head.left, res)
        pres(head.right, res)


def build_by_pre_queue(pre_list):
    if not pre_list: return
    return preb(pre_list)


def preb(pre_list):
    val = pre_list.pop(0)
    if not val: return
    node = TreeNode(val)
    node.left = preb(pre_list)
    node.right = preb(pre_list)
    return node


def inb(pre_list):
    val = pre_list.pop(0)
    if not val: return
    left_node = preb(pre_list)
    node = TreeNode(val)
    node.left = left_node
    node.right = preb(pre_list)
    return node


def postb(pre_list):
    val = pre_list.pop(0)
    if not val: return
    left_node = preb(pre_list)
    right_node = preb(pre_list)

    node = TreeNode(val)
    node.left = left_node
    node.right = right_node
    return node


def level_serial(head):
    res = []
    if not head:
        res.append(None)
        return res
    # 在加入队列时，序列化
    res.append(head.val)
    queue = [head]
    while queue:
        node = queue.pop(0)
        if node.left:
            res.append(node.left.val)
            queue.append(node.left)
        else:
            res.append(None)

        if node.right:
            res.append(node.right.val)
            queue.append(node.right)
        else:
            res.append(None)
    return res


def build_by_level_queue(level_list):
    if not level_list: return
    head = generate_node(level_list.pop(0))
    queue = []
    if head:
        queue.append(head)
    while queue:
        node = queue.pop(0)
        node.left = generate_node(level_list.pop(0))
        node.right = generate_node(level_list.pop(0))
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return head


def generate_node(val):
    if val:
        return TreeNode(val)




head = TreeNode(1)
head.left = TreeNode(1)
head.left.right = TreeNode(1)

print("level_serial", level_serial(head))
item = build_by_level_queue(level_serial(head))
print(item)
# head = build_by_pre_queue(pre_serial(head))
# print(head)
