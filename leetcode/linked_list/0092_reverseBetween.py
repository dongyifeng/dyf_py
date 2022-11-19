# coding=utf-8
print (
'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
''')


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

    return new_link_lisk.next


def reverse_between(head, m, n):
    if not head or not head.next or n <= m: return head
    dump = ListNode(None)
    dump.next = head

    # 截取合适子链表
    end_node = dump
    start_node = None
    for i in range(n):
        if i == m - 1:
            start_node = end_node
        end_node = end_node.next

    temp = end_node.next
    end_node.next = None
    # 翻转子链表
    start1, end1 = reverse_list(start_node.next)

    # 将原链表与翻转后的链表：拼接在一起
    start_node.next = start1
    end1.next = temp
    return dump.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)

foreach_list_node(reverse_between(l1, 2, 4))
