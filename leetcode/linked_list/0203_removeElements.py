# coding=utf-8
print(
    '''
    删除链表中等于给定值 val 的所有节点。
    
    示例:
    
    输入: 1->2->6->3->4->5->6, val = 6
    输出: 1->2->3->4->5''')


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


def remove_elements(head, val):
    dump = ListNode(None)
    dump.next = head

    node = dump
    while node and node.next:
        if node.next.val == val:
            node.next = node.next.next
        else:
            node = node.next
    return dump.next


linked_list = ListNode(1)
linked_list.next = ListNode(2)
linked_list.next.next = ListNode(6)
linked_list.next.next.next = ListNode(3)
linked_list.next.next.next.next = ListNode(4)
linked_list.next.next.next.next.next = ListNode(5)
linked_list.next.next.next.next.next.next = ListNode(6)

foreach_list_node(remove_elements(linked_list, 6))
