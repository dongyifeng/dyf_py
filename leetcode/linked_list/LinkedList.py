# coding:utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def foreachListNode(head):
    node = head
    while node:
        print (node.val, "->"),
        node = node.next
    print ("")


'''
在 position 之后添加 x
'''


def insertNode(head, position, xNode):
    node = head
    while node:
        if node.val == position:
            xNode.next = node.next
            node.next = xNode
            break
        else:
            node = node.next
    return head


def insertNode2(head, position, xNode):
    dump = ListNode(None)
    dump.next = head
    node = dump

    while node and node.next:
        if node.next.val == position:
            xNode.next = node.next
            node.next = xNode
            break
        else:
            node = node.next
    return dump.next


def find(head, k):
    node = head
    while node:
        if node.val == k:
            return node
        else:
            node = node.next
    return


'''
 删除 x ，涉及到 x 的父节点，x 节点，x 的子节点。
 如果删除是第一个节点，需要特殊判断，通过 dump 避免这种判断。
 note.next 中 next 是 图中的箭头，不是一下节点。
'''


def deleteNode(head, x):
    dump = ListNode(None)
    dump.next = head

    while dump and dump.next:
        if dump.next.val == x:
            dump.next = dump.next.next
            break
        else:
            dump = dump.next

    return head


def reverseList(head):
    if not head or not head.next: return head
    dump = ListNode(0)
    dump.next = head

    new_head = ListNode(None)
    tail = head
    while dump and dump.next:
        t = dump.next
        dump.next = dump.next.next
        t2 = new_head.next
        new_head.next = t
        t.next = t2
    return (new_head.next, tail)

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)

# foreachListNode(deleteNode(l1, 5))

# foreachListNode(insertNode(l1, 4, ListNode(6)))

# foreachListNode(insertNode2(l1, 1, ListNode(6)))

# foreachListNode(find(l1, 5))
