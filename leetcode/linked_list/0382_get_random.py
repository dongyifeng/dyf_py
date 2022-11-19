class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import random


def get_len(head):
    if not head: return 0
    res = 0
    node = head
    while node:
        res += 1
        node = node.next
    return res


def get_random(head):
    length = get_len(head)
    index = random.randint(0, length - 1)
    i = 0
    node = head
    while i < index and node:
        i += 1
        node = node.next
        if i == index: return node
    return node


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)

res = [0] * 6
for i in range(100):
    index = get_random(l1).val
    res[index] += 1
print([num/100.0 for num in res])
