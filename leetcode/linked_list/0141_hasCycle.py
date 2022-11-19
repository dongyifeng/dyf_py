# coding=utf-8
print('''
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。


 

进阶：

你能用 O(1)（即，常量）内存解决此问题吗？
''')


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    pos = -1
    if not head or not head.next: return pos
    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        pos += 1
        if fast == slow:
            return pos
        slow = slow.next

    return -1

node = ListNode(-4)
l2 = ListNode(3)
l2.next = ListNode(2)
l2.next.next = ListNode(0)
l2.next.next.next = node
node.next = l2.next

l1 = ListNode(1)
l1.next = ListNode(2)

print(has_cycle(l1))
print(has_cycle(l2))
