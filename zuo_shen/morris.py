class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def morris(head):
    if not head:
        return

    cur = head
    while cur:
        most_right = cur.left
        if most_right:
            while most_right.right and most_right.right != cur:
                most_right = most_right.right
            if not most_right:
                most_right.right = cur
                cur = cur.left
                continue
            else:
                most_right.right = None

        cur = cur.right


# 先序遍历
def morris(head):
    if not head:
        return

    cur = head
    while cur:
        most_right = cur.left
        # cur 有左树
        if most_right:
            # 查找左树的的最右节点
            # cur 第一次到达最右节点，那么 most_right.right == null
            # cur 第二次到达最右节点，那么 most_right.right == cur
            while most_right.right and most_right.right != cur:
                most_right = most_right.right
            # 从 while 中出来：most_right 是 cur 左树上的最右节点

            if not most_right.right:
                most_right.right = cur
                print("tmp",most_right.val,'-->',cur.val)
                cur = cur.left
                continue
            else:
                # 此时 most_right.right == cur
                most_right.right = None

        cur = cur.right


def morris_pre(head):
    if not head:
        return

    cur = head
    while cur:
        most_right = cur.left
        # cur 有左树
        if most_right:
            while most_right.right and most_right.right != cur:
                most_right = most_right.right
            # 从 while 中出来：most_right 是 cur 左树上的最右节点

            # cur 有左树时，most_right.right == null 表示第一次经历节点
            if not most_right.right:
                print(cur.val)
                most_right.right = cur
                cur = cur.left
                continue
            else:
                # 此时 most_right.right == cur
                # cur 有左树时，most_right.right == null 表示第二次经历节点
                most_right.right = None
        else:
            # cur 无左树时，只有一次经过，就是本次
            print(cur.val)

        cur = cur.right

def morris_in(head):
    if not head:
        return

    cur = head
    while cur:
        most_right = cur.left
        # cur 有左树
        if most_right:
            while most_right.right and most_right.right != cur:
                most_right = most_right.right
            # 从 while 中出来：most_right 是 cur 左树上的最右节点

            # cur 有左树时，most_right.right == null 表示第一次经历节点
            if not most_right.right:
                most_right.right = cur
                cur = cur.left
                continue
            else:
                # 此时 most_right.right == cur
                # cur 有左树时，most_right.right == null 表示第二次经历节点
                print(cur.val)
                most_right.right = None
        else:
            # cur 无左树时，只有一次经过，就是本次
            print(cur.val)

        cur = cur.right

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)
head.right.left = TreeNode(6)
head.right.right = TreeNode(7)

morris(head)

# print("先序遍历")
# morris_pre(head)
# print("中序遍历")
# morris_in(head)
