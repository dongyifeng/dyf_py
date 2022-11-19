
'''
【题目】一种特殊的单链表节点描述如下

```python
class Node:
def __init__(self,value,next,rand):
 self.value = value
 self.next = next
 self.rand = rand
```

rand 指针是单链表节点结构中新增的指针，rand 可能指向链表中的任意一个节点，也可能指向 null。给定一个由 Node 节点类型组成的无环单链表的头节点 head，请实现一个函数完成这个链表的复制，并返回复制的新链表的头节点。

【要求】时间复杂度为 O(N)，额外空间复杂度O(1)

'''


class ListNode:
    def __init__(self, val=0, next=None, rand=None):
        self.val = val
        self.next = next
        self.rand = rand


def copy_linked_list_rand(head):
    if not head: return
    node_map = {}
    node = head
    while node:
        node_map[node] = ListNode(node.val)
        node = node.next

    node = head

    while node:
        node_map[node].next = node_map.get(node.next, None)
        node_map[node].rand = node_map.get(node.rand, None)
        node = node.next
    return node_map[head]


def copy_linked_list_rand2(head):
    if not head: return
    node = head
    while node:
        node.next = ListNode(node.val, node.next)
        node = node.next.next

    node = head
    new_node = node.next
    while node:
        new_node.rand = node.rand.next if node.rand else None
        node = node.next.next
        new_node = new_node.next.next if new_node.next else None

    node = head
    res = node.next
    new_node = res
    while node:
        node.next = node.next.next if node.next else None
        new_node.next = new_node.next.next if new_node.next else None
        new_node = new_node.next
        node = node.next

    return res


def print_linked_list(head):
    if not head: return
    nums = []
    node = head
    while node:
        nums.append(node.val)
        node = node.next
    print(nums)


head = ListNode(1)
head.next = ListNode(2)
head.next.rand = head
head.next.next = ListNode(3)

node = copy_linked_list_rand(head)

node = copy_linked_list_rand2(head)

print_linked_list(copy_linked_list_rand2(head))
