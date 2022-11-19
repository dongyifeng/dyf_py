class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(head):
    print("binary tree")
    print_in_order(head, 0, "H", 17)
    print()


def print_in_order(head, height, to, length):
    if not head: return
    print_in_order(head.right, height + 1, "v", length)

    val = to + str(head.val) + to
    len_m = len(val)
    len_l = (length - len_m) / 2
    len_r = length - len_m - len_l
    val = get_space(len_l) + val + get_space(len_r)
    print(get_space(height * length) + val)

    print_in_order(head.left, height + 1, "^", length)


def get_space(num):
    return " " * int(num)


head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)
head.right.left = TreeNode(6)
head.right.right = TreeNode(7)

head.left.right.left = TreeNode(8)
head.left.right.right = TreeNode(9)

print_tree(head)
