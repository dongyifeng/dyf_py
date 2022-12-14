# coding=utf-8
print('''
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
''')


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


def middle_node(head):
    if not head or not head.next: return head
    fast = slow = head
    while fast and fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    return slow
    # return slow.next if fast.next else slow


# 从链表中间断开。成两个链表
# 翻转其中一个链表。
# 逐个比较两个链表是否相等
def is_palindrome(head):
    if not head: return True
    m_node = middle_node(head)
    new_linked_list = m_node.next
    m_node.next = None

    right_sub = reverse_list(new_linked_list)

    left_node = head
    right_node = right_sub
    while left_node and right_node:
        if left_node.val != right_node.val:
            return False
        left_node = left_node.next
        right_node = right_node.next
    return True


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(2)
l1.next.next.next.next = ListNode(1)
print(is_palindrome(l1))

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(1)
print(is_palindrome(l2))

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(2)
l2.next.next.next = ListNode(1)
print(is_palindrome(l2))