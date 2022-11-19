class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(node):
    if node is None: return
    stack = [node]
    while stack:
        p = stack.pop()
        print(p.val)

        if p.right: stack.append(p.right)
        if p.left: stack.append(p.left)

# 后续遍历：没有利用额外的栈
def pos2(head):
    if not head: return
    stack = [head]
    while stack:
        node = stack[-1]
        if node.left and head != node.left and head != node.right:
            stack.append(node.left)
        elif node.right and head != node.right:
            stack.append(node.right)
        else:
            print(stack.pop().val)
            head = node


head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)
head.right.left = TreeNode(6)
head.right.right = TreeNode(7)

print("先序遍历")
preorder(head)
