# coding=utf-8
print('''
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3
''')


# from LinkedList import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def foreach_list_node(head):
    node = head
    while node:
        print(node.val, "->"),
        node = node.next
    print("")


def delete_duplicates(head):
    if not head: return head

    # 找到重复数据
    repeated_data = set()
    node = head
    while node and node.next:
        if node.val == node.next.val:
            node.next = node.next.next
            repeated_data.add(node.val)
        else:
            node = node.next

    # 删除重复数据
    dump = ListNode(None)
    dump.next = head
    node = dump
    while node and node.next:
        # 删除
        if node.next.val in repeated_data:
            node.next = node.next.next
        else:
            node = node.next

    return dump.next


def delete_duplicates2(head):
    dump = ListNode(None)
    dump.next = head
    node = dump
    while node.next and node.next.next:
        if node.next.val == node.next.next.val:
            # 连续删除
            x = node.next.val
            while node.next and node.next.val == x:
                node.next = node.next.next
        else:
            node = node.next
    return dump.next


l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(3)
l2.next.next.next.next = ListNode(4)
l2.next.next.next.next.next = ListNode(4)
l2.next.next.next.next.next.next = ListNode(5)
l2.next.next.next.next.next.next.next = ListNode(5)

# foreach_list_node(delete_duplicates(l2))
foreach_list_node(delete_duplicates2(l2))
