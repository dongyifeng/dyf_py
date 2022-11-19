# coding:utf-8


import heapq
import sys


def foreach_list_node(head):
    tmp = head
    while tmp:
        print(tmp.val)
        tmp = tmp.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


# 采用冒泡选取最小队列
def mergeKLists1(lists):
    if not lists: return
    node = head = ListNode(0)
    while True:
        min_li = ListNode(sys.maxsize)
        k = 0
        for i in range(len(lists)):
            li = lists[i]
            if not li: continue
            if li < min_li:
                min_li = li
                k = i
        if min_li.val != sys.maxsize:
            node.next = min_li
            node = node.next
            min_li = min_li.next
            lists[k] = min_li
        lists = [li for li in lists if li]
        if len(lists) <= 1: break

    if lists:
        node.next = lists[0]
    return head.next


# 采用最小堆选取最小队列
def mergeKLists2(lists):
    if not lists: return
    node = head = ListNode(0)
    heap = lists
    heapq.heapify(heap)
    while heap:
        li = heapq.heappop(heap)
        node.next = li
        node = node.next
        li = li.next
        if li:
            heapq.heappush(heap, li)

    return head.next


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)

lists = [l1, l2, l3]

# print(l1<l3)

foreach_list_node(mergeKLists1(lists))

# foreach_list_node(mergeKLists2(lists))


# from Queue import PriorityQueue
#
# q = PriorityQueue()
# q.put(1)
# q.put(5)
# q.put(4)
# q.put(3)
#
# print q.task_done()
