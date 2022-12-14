# coding=utf-8
print('''给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
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


def reorder_list(head):
    if not head or not head.next: return head

    array = []
    node = head
    while node:
        array.append(node)
        node = node.next

    start = 0
    end = len(array) - 1
    result = ListNode(None)
    node = result
    while start <= end:
        node.next = array[start]
        node.next.next = array[end]
        node = node.next.next
        start += 1
        end -= 1
    node.next = None
    return result.next


print("=" * 100)


# 寻找中间结点
def middle_node(head):
    if not head or not head.next: return head
    fast = slow = head
    while fast and fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    # return slow.next if fast.next else slow
    return slow


# 链表翻转
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


def reorder_list2(head):
    if not head or not head.next: return head
    # 获取中介节点
    m_node = middle_node(head)
    new_link_list = m_node.next
    m_node.next = None
    # 翻转链表
    new_link_list = ListNode(0, reverse_list(new_link_list))

    raw_link_list = ListNode(0, head)
    node = result_link_list = ListNode(0)
    while new_link_list.next:
        # 拼接奇数结点
        node.next = raw_link_list.next
        raw_link_list.next = raw_link_list.next.next

        # 拼接偶数结点
        node.next.next = new_link_list.next
        new_link_list.next = new_link_list.next.next

        node = node.next.next

    if raw_link_list.next:
        node.next = raw_link_list.next

    return result_link_list.next


l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(4)
l2.next.next.next.next = ListNode(5)
l2.next.next.next.next.next = ListNode(6)

foreach_list_node(reorder_list2(l2))

# foreach_list_node(reorder_list(l2))
# foreach_list_node(reorder_list(l1))
