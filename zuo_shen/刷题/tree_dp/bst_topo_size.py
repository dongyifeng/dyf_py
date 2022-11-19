'''
给定一棵二叉树的头节点 head，已知所有节点的值都不一样，返回其中最大的且符合搜索二叉树的最大拓扑结构的大小。
拓扑结构：不是子树，只要能连起来的结构都算。
'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bst_topo_size(head: TreeNode):
    if not head: return 0

    res = max_topo(head, head)
    res = max(res, bst_topo_size(head.left))
    res = max(res, bst_topo_size(head.right))
    return res


def max_topo(head: TreeNode, node: TreeNode):
    if head and node and is_bst_node(head, node, node.val):
        return max_topo(head, node.left) + max_topo(head, node.right) + 1
    return 0


def is_bst_node(head: TreeNode, node: TreeNode, value):
    if not head: return False
    if head == node: return True
    return is_bst_node(head.left if head.val > value else head.right, node, value)


class Record:
    def __init__(self, left: TreeNode, right: TreeNode):
        self.left = left
        self.right = right


def bst_topo_size2(head: TreeNode):
    map = {}
    return pos_order(head, map)


def pos_order(head: TreeNode, map):
    if not head: return 0

    left_info = pos_order(head.left, map)
    right_info = pos_order(head.right, map)
    modify_map(head.left, head.val, map, True)
    modify_map(head.right, head.val, map, False)
    # 修改后的值
    left_record = map.get(head.left, None)
    right_record = map.get(head.right, None)

    left_bst = 0 if not left_record else left_record.left + left_record.right + 1
    right_bst = 0 if not right_record else right_record.left + right_record.right + 1
    map[head] = Record(left_bst, right_bst)
    return max(left_bst + right_bst + 1, max(left_info, right_info))


# 返回值是要减掉的贡献记录
def modify_map(node: TreeNode, val, map, is_left):
    if not node or node not in map: return 0

    record = map.get(node)
    # 左节点或者右节点不满足搜索二叉树
    if (is_left and node.val > val) or (not is_left and node.val < val):
        map.pop(node)
        # node 要被删除，所以他的贡献记录需要删掉
        return record.left + record.right + 1
    else:
        minus = modify_map(node.right if is_left else node.left, val, map, is_left)
        if is_left:
            record.right -= minus
        else:
            record.left -= minus
        map[node] = record
        return minus


import random


def generator_random_arr(max_size):
    num = range(int(random.random() * max_size) + 1)
    n = len(num)
    return random.sample(num, int(random.random() * n) + 1)


def insert(root, data):
    # 查找插入位置
    temp = root
    while temp:
        p = temp
        temp = temp.left if data < temp.val else temp.right

    if data < p.val:
        p.left = TreeNode(data)
    else:
        p.right = TreeNode(data)


def generator_bst(arr):
    root = None
    for item in arr:
        if not root:
            root = TreeNode(item)
            continue

        insert(root, item)
    return root


def check():
    max_size = 10
    for i in range(1000):
        arr = generator_random_arr(max_size)
        root1 = generator_bst(arr)
        root2 = generator_bst(arr)

        res1 = bst_topo_size(root1)
        res2 = bst_topo_size2(root2)

        # print("int", res1, res2)
        if res1 != res2:
            print("ERROR", res1, res2, arr)
    print("OVER")


check()
