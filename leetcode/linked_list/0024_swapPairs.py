# coding=utf-8
print '''给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
'''

from LinkedList import *

def swapPairs(head):
    if not head or not head.next : return head
    dump = ListNode(0)
    dump.next = head

    p = dump
    while p and p.next and p.next.next:
        end = p.next.next
        p.next.next = end.next
        end.next = p.next
        p.next = end
        p = p.next.next

    return dump.next


l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(4)

foreachListNode(swapPairs(l2))
