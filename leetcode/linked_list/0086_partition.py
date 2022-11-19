# coding=utf-8
print
'''给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
'''


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


def partition(head, x):
    if not head or not head.next: return head

    dump = ListNode(0)
    dump.next = head

    new_node = new_head = ListNode(0)
    node = dump
    while node and node.next:
        if node.next.val < x:
            # 从 head 链表上删除，并添加到 new_head 最后
            new_node.next = node.next
            node.next = node.next.next
            new_node = new_node.next
        else:
            node = node.next

    # 将 new_head 链表和 head 链表 拼接
    new_node.next = dump.next
    return new_head.next


l2 = ListNode(1)
l2.next = ListNode(4)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(2)
l2.next.next.next.next = ListNode(5)
l2.next.next.next.next.next = ListNode(2)

foreach_list_node(partition(l2, 3))
