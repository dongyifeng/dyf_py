# coding=utf-8
print
'''
给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。

删除完毕后，请你返回最终结果链表的头节点。

 

你可以返回任何满足题目要求的答案。

（注意，下面示例中的所有序列，都是对 ListNode 对象序列化的表示。）

示例 1：

输入：head = [1,2,-3,3,1]
输出：[3,1]
提示：答案 [1,2,1] 也是正确的。
示例 2：

输入：head = [1,2,3,-3,4]
输出：[1,2,4]
示例 3：

输入：head = [1,2,3,-3,-2]
输出：[1]
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


'''
只需要求出前缀和，对于前缀和相同的项，那他们中间的部分即是可以消除掉的，
比如以 [1, 2, 3, -3, 4] 为例，其前缀和数组为 [1, 3, 6, 3, 7] ，我们发现有两项均为 3，则 6 和 第二个 3 所对应的原数组中的数字是可以消掉的。
换成链表其实也是一样的思路，把第一个 3 的 next 指向第二个 3 的 next 即可
'''


def remove_zero_sum_sublists(head):
    if not head or not head.next: return head
    # 因为头结点也有可能会被消掉，所以这里加一个虚拟节点作为头结点
    dumpy = ListNode(0)
    dumpy.next = head
    p = dumpy

    prefix_sum = {}
    s = 0
    while p:
        s += p.val
        if s in prefix_sum:
            prefix_sum[s].next = p.next
        else:
            prefix_sum[s] = p
        p = p.next
    return dumpy.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(-3)
l1.next.next.next = ListNode(3)
l1.next.next.next.next = ListNode(1)

foreach_list_node(remove_zero_sum_sublists(l1))
