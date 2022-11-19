# coding=utf-8
print('''给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3''')


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
    node = head
    while node and node.next:
        if node.val == node.next.val:
            node.next = node.next.next
        else:
            node = node.next
    return head


l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(3)
l2.next.next.next.next = ListNode(4)
l2.next.next.next.next.next = ListNode(4)
l2.next.next.next.next.next.next = ListNode(5)

foreach_list_node(delete_duplicates(l2))
