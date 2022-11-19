'''
一棵二叉树原本是搜索二叉树，但是其中有两个节点调换了位置，使得这棵二叉树不再是搜索二叉树，请找到这两个错误节点并返回。
已知二叉树中所有节点的值都不一样，给定二叉树的头节点 head，返回一个长度为 2 的二叉树节点类型数组 errs，errs[0] 表示一个错误节点，errs[1] 表示另一个错误节点。
进阶：
如果在原问题中得到了两个错误节点，我们当然可以通过交换两个节点值的方式让整棵二叉树重新成为搜索二叉树。但是现在要求你不能这么做，而是在结构上完全交换两个节点的位置，请实现调整的函数。
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


global pre
pre = None


def find_error_node(root: TreeNode):
    global pre
    pre = None
    err = [None, None]
    inorder3(root, err)
    return err


def inorder3(node, err):
    global pre
    if node:
        inorder3(node.left, err)
        if pre and pre.val > node.val:
            err[1] = node
            if not err[0]: err[0] = pre

        pre = node
        inorder3(node.right, err)


def inorder(node, first, second):
    if node:
        first, second = inorder(node.left, first, second)
        if node.left and node.left.val > node.val:
            second = node
            if not first: first = node.left
        first, second = inorder(node.right, first, second)
        if node.right and node.right.val < node.val:
            second = node.right
            if not first: first = node
    return first, second


def find_error_node2(root: TreeNode):
    if not root: return
    stack = []
    first = None
    second = None
    pre = None
    while root or stack:
        # 从根节点开始，一直找它的左子树
        if root:
            stack.append(root)
            root = root.left
        else:
            # while结束表示当前节点node为空，即前一个节点没有左子树了
            root = stack.pop()
            if pre and pre.val > root.val:
                second = root
                if not first: first = pre

            pre = root
            # 开始查看它的右子树
            root = root.right
    return first, second


def modify_error_node(root: TreeNode):
    first, second = find_error_node2(root)
    first.val, second.val = second.val, first.val


def inorder2(root: TreeNode):
    if not root: return
    stack = []
    res = []
    while root or stack:
        # 从根节点开始，一直找它的左子树
        if root:
            stack.append(root)
            root = root.left
        else:
            # while结束表示当前节点node为空，即前一个节点没有左子树了
            root = stack.pop()
            res.append(root.val)
            # 开始查看它的右子树
            root = root.right
    return res


#
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(2)
root.left.left = TreeNode(1)
root.right.right = TreeNode(5)
first, second = find_error_node(root)
print(first.val, second.val)
first, second = find_error_node2(root)
print(first.val, second.val)
# modify_error_node(root)
print(inorder2(root))

print('-' * 100)
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(4)
root.left.left = TreeNode(1)
root.right.right = TreeNode(2)
first, second = find_error_node(root)
print(first.val, second.val)
first, second = find_error_node2(root)
# modify_error_node(root)
print(first.val, second.val)
print(inorder2(root))

print('-' * 100)
root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(4)
root.left.left = TreeNode(1)
root.right.right = TreeNode(5)
first, second = find_error_node(root)
print(first.val, second.val)
first, second = find_error_node2(root)
# modify_error_node(root)
print(first.val, second.val)
print(inorder2(root))
