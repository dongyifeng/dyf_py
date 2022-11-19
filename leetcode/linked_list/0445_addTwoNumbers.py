# coding=utf-8


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


def add_two_numbers2(l1, l2):
    reverse_l1 = reverse_list(l1)
    reverse_l2 = reverse_list(l2)
    l1_node = reverse_l1
    l2_node = reverse_l2
    result = ListNode(None)
    res_node = result
    carry = 0
    while l1_node and l2_node:
        sum_node = l1_node.val + l2_node.val + carry
        res_node.next = ListNode(sum_node % 10)
        carry = int(sum_node / 10)
        l2_node = l2_node.next
        l1_node = l1_node.next
        res_node = res_node.next

    node = None
    if l1_node: node = l1_node
    if l2_node: node = l2_node
    if node:
        while node:
            sum_node = node.val + carry
            res_node.next = ListNode(sum_node % 10)
            carry = int(sum_node / 10)
            node = node.next
            res_node = res_node.next

    if carry > 0:
        res_node.next = ListNode(carry)

    return reverse_list(result.next)


l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)

l2 = ListNode(9)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(4)
l2.next.next.next.next = ListNode(4)

foreach_list_node(add_two_numbers2(l1, l2))
