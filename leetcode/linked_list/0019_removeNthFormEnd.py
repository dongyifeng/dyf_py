# coding:utf-8

'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 链表快慢指针:O(n)
# 技巧一：快慢指针
# 技巧二：哑变量：省去了删除节点是头结点的判断
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy
    # fast 指针先走 n + 1 步
    for i in range(n + 1):
        fast = fast.next

    # fast 与 slow 间隔 n 个元素，fast 和 slow 同时走到终点。
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next


def foreach_list_node(head):
    tmp = head
    while tmp:
        print(tmp.val)
        tmp = tmp.next


def remove_nth_from_end1(head, n):
    l = 0
    tmp = head
    while tmp:
        l += 1
        tmp = tmp.next

    tmp = head
    for i in range(l - n - 1):
        tmp = tmp.next
    tmp.next = tmp.next.next
    return head


def remove_nth_from_end2(head, n):
    stack = []
    tmp = head
    while tmp:
        stack.append(tmp)
        tmp = tmp.next

    for i in range(n + 1):
        tmp = stack.pop()
    tmp.next = tmp.next.next
    return head


print("---")
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
foreach_list_node(l1)
print("---")
foreach_list_node(remove_nth_from_end(l1, 2))

print("---")
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
# foreach_list_node(remove_nth_from_end(l1, 1))
# foreach_list_node(remove_nth_from_end2(l1, 1))
foreach_list_node(remove_nth_from_end1(l1, 1))
