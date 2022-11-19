# coding=utf-8
print '''
栈
'''


class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    # 返回栈顶元素
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


'''
调单递增栈
'''


class MonotoneIncreasingStack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    # 返回栈顶元素
    def peek(self):
        return self.items[-1]

    def push(self, item):
        while not self.is_empty() and self.peek() < item:
            self.pop()
        self.items.append(item)

    def pop(self):
        self.items.pop()


'''
调单递减栈
'''


class MonotoneDecreasingStack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    # 返回栈顶元素
    def peek(self):
        return self.items[-1]

    def push(self, item):
        while not self.is_empty() and self.peek() > item:
            self.pop()
        self.items.append(item)

    def pop(self):
        self.items.pop()


if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push("1")
    my_stack.push("2")
    my_stack.push("3")

    print my_stack.pop()
    print my_stack.pop()

    stack = MonotoneDecreasingStack()
    for i in [3, 4, 2, 6, 4, 5, 2, 3]:
        stack.push(i)
    print stack.items
