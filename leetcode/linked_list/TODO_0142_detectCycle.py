# coding=utf-8
print '''
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。
'''

# 未完成

from LinkedList import *

def detectCycle(head):
    if not head or not head.next: return
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        if fast == slow:
            return slow
        slow = slow.next


l1 = ListNode(3)
l2 = ListNode(2)
l1.next = l2
l1.next.next = ListNode(0)
l1.next.next.next = ListNode(-4)
l1.next.next.next.next = l2

print detectCycle(l1)
