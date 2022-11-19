class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.k = k
        self.l = 0
        self.head = ListNode(None)
        self.tail = None

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull(): return

        node = ListNode(value, self.head.next)
        self.head.next = node

        if self.tail:
            self.tail.next = node
        else:
            self.tail = node
        self.l += 1

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull(): return
        node = ListNode(value)
        if self.tail:
            self.tail.next = node
        if not self.head.next:
            self.head.next = node
        self.tail = node
        node.next = self.head.next
        self.l += 1

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty(): return
        if self.l == 1:
            self.head.next = None
            self.tail = None
            return
        self.head.next = self.head.next.next
        self.tail.next = self.head.next
        self.l -= 1

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty(): return
        if self.l == 1:
            self.head.next = None
            self.tail = None
            return
        node = self.head
        while node:
            if node.next == self.tail:
                break
            node = node.next
        node.next = node.next.next
        self.tail = node
        self.tail.next = self.head.next
        self.l -= 1

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.l <= 0: return None
        return self.head.next

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.l <= 0: return None
        return self.tail

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


def foreach_list_node(head):
    node = head
    node_set = set()
    while node:
        if node in node_set:
            break
        node_set.add(node)
        print(node.val, "->"),
        node = node.next
    print("")


circularDeque = MyCircularDeque(3)
circularDeque.insertLast(1)
circularDeque.insertLast(2)
circularDeque.insertFront(3)
circularDeque.insertFront(4)
print(circularDeque.getFront().val)
print(circularDeque.getRear().val)
print(circularDeque.isEmpty())
print(circularDeque.isFull())
circularDeque.deleteFront()
circularDeque.deleteFront()
circularDeque.deleteFront()
# circularDeque.deleteLast()
# circularDeque.deleteLast()
# circularDeque.deleteLast()
# circularDeque.deleteLast()

foreach_list_node(circularDeque.head.next)
