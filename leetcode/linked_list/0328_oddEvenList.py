# coding=utf-8
print('''
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:

输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
示例 2:

输入: 2->1->3->5->6->4->7->NULL
输出: 2->3->6->7->1->5->4->NULL
说明:

应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
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


'''
1. 在奇数位（i 为偶数），将 next （偶数位的结点），加入新的链表，从原链表中删除
2. 将两个链表拼接在一起
'''


def odd_even_list(head):
    if not head or not head.next: return head
    dummy = ListNode(None, head)
    # 偶数链表
    even_list = ListNode(None)

    even_node = even_list
    node = dummy.next
    i = 0
    while node and node.next:
        if i % 2 == 0:
            even_node.next = node.next
            node.next = node.next.next
            even_node = even_node.next
        else:
            node = node.next
        i += 1
    even_node.next = None

    # 链表拼接
    node.next = even_list.next
    return dummy.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)

foreach_list_node(odd_even_list(l1))
