'''
【题目】给定一个单链表的头节点 head，节点的值类型是整型，再给定一个整型 pivot。实现一个调整链表的函数，将链表调整为左边部分都小于 pivot 的节点，中间部分都是值等于 pivot 的节点，右边部分都是值大于 pivot 的节点。


【进阶】在实现原问题功能的基础上增加如下的要求

- 调整后所有小于 pivot 的节点之间的相对顺序和调整前一样
- 调整后所有等于 pivot 的节点之间的相对顺序和调整前一样
- 调整后所有大于 pivot 的节点之间的相对顺序和调整前一样
- 时间复杂度请达到 O(N)，额外空间复杂度达到 O(1)
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linked_list_partition(head, pivot):
    if not head: return

    nums = []
    node = head
    while node:
        nums.append(node.val)
        node = node.next

    partition(nums, pivot)

    node = head
    for num in nums:
        node.val = num
        node = node.next
    return head


def partition(nums, pivot):
    less = -1
    more = len(nums)

    i = 0
    while i < more:
        if nums[i] < pivot:
            less += 1
            swap(nums, less, i)
            i += 1
        elif nums[i] == pivot:
            i += 1
        else:
            more -= 1
            swap(nums, i, more)


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


def print_linked_list(head):
    if not head: return
    nums = []
    node = head
    while node:
        nums.append(node.val)
        node = node.next
    print(nums)


def linked_list_partition2(head, pivot):
    if not head: return
    small_head = None
    small_tail = None
    equal_head = None
    equal_tail = None
    big_head = None
    big_tail = None

    node = head
    while node:
        if node.val < pivot:
            if not small_head:
                small_head = node
                small_tail = node
            else:
                small_tail.next = node
                small_tail = node
        elif node.val == pivot:
            if not equal_head:
                equal_head = node
                equal_tail = node
            else:
                equal_tail.next = node
                equal_tail = node
        else:
            if not big_head:
                big_head = node
                big_tail = node
            else:
                big_tail.next = node
                big_tail = node

        node = node.next

    # small and equal reconnect
    # 如果有小于区
    if small_head:
        small_tail.next = equal_head

        # 下一步，谁去连大于区域的头，谁就变成 equal_tail
        equal_tail = equal_tail if equal_tail else small_tail

    # equal_tail 不为空：存在小于区域或者存在等于区域
    # 如果都不存在，equal_tail 为 null，也不需要连接了
    if equal_tail:
        equal_tail.next = big_head

    if small_head:
        return small_head
    if equal_head:
        return equal_head
    return big_head


head = ListNode(4)
head.next = ListNode(6)
head.next.next = ListNode(3)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(8)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next.next.next = ListNode(9)




linked_list_partition2(head, 5)
print_linked_list(head)
