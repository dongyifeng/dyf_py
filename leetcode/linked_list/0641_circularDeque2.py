class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.k = k
        self.l = 0
        self.data = [None] * self.k
        self.head = -1
        self.tail = -1

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull(): return

        index = self.head % self.k
        self.data[index] = value
        self.head -= 1
        self.l += 1

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull(): return
        self.tail += 1

        self.data[self.tail % self.k] = value
        self.l += 1

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty(): return
        index = (self.head + 1) % self.k
        self.data[index] = None
        self.head += 1
        self.l -= 1

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty(): return
        self.data[self.tail % self.k] = None
        self.tail -= 1
        self.l -= 1

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty(): return -1
        index = (self.head + 1) % self.k
        return self.data[index]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty(): return -1
        return self.data[self.tail % self.k]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.l <= 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.l >= self.k


# ["MyCircularDeque","insertFront","insertLast","getFront","insertLast","getFront","insertFront","getRear","getFront","getFront","deleteLast","getRear"]
# [[5],[7],[0],[],[3],[],[9],[],[],[],[],[]]


circularDeque = MyCircularDeque(5)

circularDeque.insertFront(7)
circularDeque.insertLast(0)
circularDeque.insertLast(3)
circularDeque.insertFront(9)
circularDeque.deleteLast()
print("data", circularDeque.data)
print("head", circularDeque.head)
print("tail", circularDeque.tail)
print(circularDeque.getRear())

# circularDeque.insertFront(3)
# circularDeque.insertFront(4)
#
# print(circularDeque.data)
# print("tail", circularDeque.tail)
# print("head", circularDeque.head)
#
# print(circularDeque.getFront())
# print(circularDeque.getRear())
#
# print(circularDeque.isEmpty())
# print(circularDeque.isFull())
#
# circularDeque.deleteFront()
# circularDeque.deleteFront()
# circularDeque.deleteFront()
#
# print(circularDeque.data)
# print(circularDeque.isEmpty())
# print(circularDeque.isFull())
#
# circularDeque.insertLast(2)
# circularDeque.insertLast(3)
# circularDeque.deleteLast()
#
# print(circularDeque.data)
# print(circularDeque.head)
# print(circularDeque.tail)

# circularDeque.deleteFront()
# circularDeque.deleteFront()
# print(circularDeque.data)
# circularDeque.deleteLast()
# circularDeque.deleteLast()
# circularDeque.deleteLast()
# circularDeque.deleteLast()

# foreach_list_node(circularDeque.head.next)
