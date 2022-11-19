# coding=utf-8
"二叉搜索树迭代器"

'''
实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。
调用 next() 将返回二叉搜索树中的下一个最小的数。
示例：

BSTIterator iterator = new BSTIterator(root);
iterator.next();    // 返回 3
iterator.next();    // 返回 7
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 9
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 15
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 20
iterator.hasNext(); // 返回 false
 

提示：
next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.data = []
        self.index = -1
        self.count = 0
        if root is None: return
        stack = []
        p = root
        # 非递归：中序遍历
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            self.data.append(p.val)
            p = p.right
        self.count = len(self.data)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        self.index += 1
        return self.data[self.index]

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.index < (self.count - 1)


root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

# bst_iterator = BSTIterator(root)
# print(bst_iterator.next())
# print(bst_iterator.next())
# print(bst_iterator.hasNext())
# print(bst_iterator.next())
# print(bst_iterator.hasNext())
# print(bst_iterator.next())
# print(bst_iterator.hasNext())
# print(bst_iterator.next())
# print(bst_iterator.hasNext())


class BSTIterator2(object):

    def __init__(self, root):
        self.cur = root
        self.stack = []

    def next(self):
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left

        self.cur = self.stack.pop()
        ret = self.cur.val
        self.cur = self.cur.right
        return ret

    def hasNext(self):
        return not self.cur or not self.stack


bst_iterator = BSTIterator2(root)
print(bst_iterator.next())
print(bst_iterator.next())
print(bst_iterator.hasNext())
print(bst_iterator.next())
print(bst_iterator.hasNext())
print(bst_iterator.next())
print(bst_iterator.hasNext())
print(bst_iterator.next())
print(bst_iterator.hasNext())