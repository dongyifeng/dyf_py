# coding=utf-8

print
'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换
'''


def foreach_list_node(head):
    tmp = head
    while tmp:
        print(tmp.val)
        tmp = tmp.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list2(head):
    if not head or not head.next: return head
    raw_link_list = ListNode(0)
    raw_link_list.next = head

    new_link_lisk = ListNode(None)
    while raw_link_list and raw_link_list.next:
        node = raw_link_list.next
        # 从旧删除 node 节点
        raw_link_list.next = raw_link_list.next.next

        tmp = new_link_lisk.next
        # 将 node 插入新链表
        new_link_lisk.next = node
        node.next = tmp

    return new_link_lisk.next



def reverse_list(head):
    if not head or not head.next: return head
    raw_link_list = ListNode(0)
    raw_link_list.next = head

    new_link_lisk = ListNode(None)
    while raw_link_list and raw_link_list.next:
        node = raw_link_list.next
        # 从旧删除 node 节点
        raw_link_list.next = raw_link_list.next.next

        tmp = new_link_lisk.next
        # 将 node 插入新链表
        new_link_lisk.next = node
        node.next = tmp

    return (new_link_lisk.next, head)


def reverse_k_group(head, k):
    if not head or not head.next or k < 2: return head
    dump = ListNode(0)
    dump.next = head

    node = dump
    while node:
        # 截取长度为 k 的链表
        new_link_list_end = node
        for i in range(k):
            new_link_list_end = new_link_list_end.next
            if not new_link_list_end: return dump.next
        raw_link_list_tail = new_link_list_end.next
        new_link_list_end.next = None

        # 翻转
        new_head, new_tail = reverse_list(node.next)

        # 拼接
        node.next = new_head
        new_tail.next = raw_link_list_tail
        node = new_tail
    return dump.next


l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(4)
l2.next.next.next.next = ListNode(5)

# head, tail = reverseList(l2)

# print tail.val

# foreachListNode(head)
foreach_list_node(reverse_k_group(l2, 2))
# foreach_list_node(reverse_list(l2)[0])
