# coding=utf-8
print(
    '''
    编写一个程序，找到两个单链表相交的起始节点。
    
    如下面的两个链表：
    
    
    在节点 c1 开始相交。
    
    
    示例 1：
    
    输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
    输出：Reference of the node with value = 8
    输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
     
    
    示例 2：
    
    输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    输出：Reference of the node with value = 2
    输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
     
    
    示例 3：
    
    输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
    输出：null
    输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
    解释：这两个链表不相交，因此返回 null。
     
    
    注意：
    
    如果两个链表没有交点，返回 null.
    在返回结果后，两个链表仍须保持原有的结构。
    可假定整个链表结构中没有循环。
    程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
    ''')


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def link_list_len(head):
    last_node = head
    length = 0
    while last_node:
        last_node = last_node.next
        length += 1
    return (length, last_node)


def get_intersection_node(headA, headB):
    if not headA or not headB: return
    if headA == headB: return headA

    # 计算链表A 的长度
    length_a, last_note_a = link_list_len(headA)
    length_b, last_note_b = link_list_len(headB)
    if last_note_a != last_note_b: return

    fast = headA if length_a >= length_b else headB
    slow = headB if length_a >= length_b else headA
    margin = abs(length_a - length_b)
    for i in range(margin):
        fast = fast.next
    while True:
        if fast == slow: return fast
        fast = fast.next
        slow = slow.next


common = ListNode(8)
common.next = ListNode(4)
common.next.next = ListNode(5)

l1 = ListNode(4)
l1.next = ListNode(1)
l1.next.next = common

l2 = ListNode(5)
l2.next = ListNode(0)
l2.next.next = ListNode(1)
l2.next.next.next = common

print(get_intersection_node(l1, l2).val)
