'''
两个链表相交

【题目】给定两个可能有环也可能无环的单链表，头结点 head1 和 head2。请实现一个函数，如果两个链表相交，请返回相交的第一个节点。如果不相交，返回 null。

【要求】如果两个链表长度之和为 N ，时间复杂度请达到 O(N)，额外空间复杂度请达到 O(1)
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_intersect_node(head1, head2):
    if not head1 or not head2: return

    node1_set = set()
    node = head1
    while node:
        # 有环,遍历完毕
        if node in node1_set:
            break
        node1_set.add(node)
        node = node.next

    node2_set = set()
    node = head2
    while node:
        # 有环,遍历完毕
        if node in node2_set:
            break
        # 与链表1 相交 node
        if node in node1_set:
            return node
        node2_set.add(node)
        node = node.next


def get_intersect_node2(head1, head2):
    if not head1 or not head2: return

    loop1 = get_loop_node(head1)
    loop2 = get_loop_node(head2)

    if not loop1 and not loop2:
        no_loop(head1, head2)
    elif loop1 and loop2:
        return both_loop(head1, loop1, head2, loop2)


def get_loop_node(head):
    if not head: return

    fast = head
    node = head
    while fast and fast.next:
        node = node.next
        fast = fast.next.next
        if node == fast: break

    if node != fast: return

    fast = head
    while fast != node:
        fast = fast.next
        node = node.next
    return node


def no_loop(head1, head2):
    n = 0
    node1 = head1
    while node1.next:
        node1 = node1.next
        n += 1

    node2 = head2
    while node2.next:
        node2 = node2.next
        n -= 1

    if node1 != node2: return

    node1 = head1 if n > 0 else head2
    node2 = head2 if n > 0 else head1

    n = abs(n)
    while n > 0:
        node1 = node1.next
        n -= 1

    while node1 != node2:
        node2 = node2.next
        node1 = node1.next

    return node1


def both_loop(head1, loop1, head2, loop2):
    # 情景二
    if loop2 == loop1:
        n = 0

        node1 = head1
        while node1 != loop1:
            node1 = node1.next
            n += 1

        node2 = head2
        while node2 != loop1:
            node2 = node2.next
            n -= 1

        if node1 != node2: return

        node1 = head1 if n > 0 else head2
        node2 = head2 if n > 0 else head1

        n = abs(n)
        while n > 0:
            node1 = node1.next
            n -= 1

        while node1 != node2:
            node2 = node2.next
            node1 = node1.next
        return node1

    # 如果两个链表相交，那么从 loop1 一定能走到 loop2
    node1 = loop1.next
    while node1 != loop1:
        # 情景三
        if node1 == loop2:
            return node1
        node1 = node1.next

    # 情景一


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(7)

print(get_intersect_node(head, head2))
print(get_intersect_node2(head, head2))


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(7)
head2.next.next.next = head.next

print(get_intersect_node(head, head2).val)
print(get_intersect_node2(head, head2))

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next.next

head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(7)
head2.next.next.next = ListNode(8)
head2.next.next.next.next = head2.next

print(get_intersect_node(head, head2))
print(get_intersect_node2(head, head2))

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next.next

head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(7)
head2.next.next.next = ListNode(8)
head2.next.next.next.next = head.next

print(get_intersect_node(head, head2).val)
print(get_intersect_node2(head, head2).val)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next.next

print("get_loop_node", get_loop_node(head).val)

head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(7)
head2.next.next.next = ListNode(8)
head2.next.next.next.next = head.next.next.next

print(get_intersect_node(head, head2).val)
print(get_intersect_node2(head, head2).val)
