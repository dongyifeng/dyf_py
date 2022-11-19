# coding=utf-8
print('''
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

现有一个链表 -- head = [4,5,1,9]，它可以表示为:



 

示例 1:

输入: head = [4,5,1,9], node = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], node = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
 

说明:

链表至少包含两个节点。
链表中所有节点的值都是唯一的。
给定的节点为非末尾节点并且一定是链表中的一个有效节点。
不要从你的函数中返回任何结果。'''


      '''
      删除结点 node
      
      正常情况删除结点需要知道父结点。
      这里无法获取父节点：
      将 node.next 中 val 拷贝到node 中，将 node.next 结点删除。
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

def delete_node(head, val):
    dump = ListNode(None, head)
    node = dump
    while node.next:
        if node.next.val == val:
            node.next = node.next.next
            return dump.next
        node=node.next
    return dump.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
foreach_list_node(delete_node(l1,1))
