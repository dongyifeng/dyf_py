# coding:utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def toString(l1):
    while l1:
        print(l1.val, '->', )
        l1 = l1.next


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    curr = head = ListNode(0)
    carry = 0
    while l1 is not None or l2 is not None:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        sum = val1 + val2 + carry
        carry = int((sum) / 10)
        curr.next = ListNode(sum % 10)
        curr = curr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if carry > 0:
        curr.next = ListNode(carry)
    return head.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

toString(l1)
print("-" * 50)
toString(l2)

print("-" * 50)
toString(addTwoNumbers(l1, l2))
