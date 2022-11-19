# coding=utf-8
print '''
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
'''


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.min = None

    def is_empty(self):
        return len(self.items) == 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.items.append(x)
        self.min = min(x, self.min) if self.min is not None else x

    def pop(self):
        """
        :rtype: None
        """
        if self.is_empty(): return None
        x = self.items.pop()
        if self.is_empty():
            self.min = None
            return x
        if x <= self.min:
            self.min = min(self.items)
        return x

    def top(self):
        """
        :rtype: int
        """
        if self.items:
            return self.items[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


minStack = MinStack()
minStack.pop()
minStack.getMin()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# print minStack.getMin()  # 返回 -3.
# minStack.pop()
# print minStack.top()  # 返回 0.
# print minStack.getMin()  # 返回 -2.
