# coding=utf-8

print ('''反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL''')
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


l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(4)
l2.next.next.next.next = ListNode(5)

foreach_list_node(l2)
print ("反：")
foreach_list_node(reverse_list(l2))
