# coding=utf-8
print
'''
给出一个以头节点 head 作为第一个节点的链表。链表中的节点分别编号为：node_1, node_2, node_3, ... 。

每个节点都可能有下一个更大值（next larger value）：对于 node_i，如果其 next_larger(node_i) 是 node_j.val，那么就有 j > i 且  node_j.val > node_i.val，而 j 是可能的选项中最小的那个。如果不存在这样的 j，那么下一个更大值为 0 。

返回整数答案数组 answer，其中 answer[i] = next_larger(node_{i+1}) 。

注意：在下面的示例中，诸如 [2,1,5] 这样的输入（不是输出）是链表的序列化表示，其头节点的值为 2，第二个节点值为 1，第三个节点值为 5 。

示例 1：

输入：[2,1,5]
输出：[5,5,0]
示例 2：

输入：[2,7,4,3,5]
输出：[7,0,5,5,0]
示例 3：

输入：[1,7,5,1,9,2,5,1]
输出：[7,9,9,9,0,5,0,0]
 

提示：

对于链表中的每个节点，1 <= node.val <= 10^9
给定列表的长度在 [0, 10000] 范围内
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def next_larger_nodes(head):
    if not head: return []

    node = head
    result = []
    while node:
        tmp = node.next
        has = False
        while tmp:
            if tmp.val > node.val:
                result.append(tmp.val)
                has = True
                break
            tmp = tmp.next
        if not has: result.append(0)
        node = node.next
    return result


def next_larger_nodes2(head):
    if not head: return []

    # 将链表的数据存储在数组中
    data_list = []
    while head:
        data_list.append(head.val)
        head = head.next

    # 栈中存储的是元素的下标，并且从栈底到栈顶元素在集合中对应的
    # 值是从大到小的
    stack = []
    result = [0] * len(data_list)
    for i in range(len(data_list)):
        while stack and data_list[stack[-1]] < data_list[i]:
            # 如果栈顶元素对应的值小于当前值，说明栈顶元素遇到了比他小的
            index = stack.pop()
            result[index] = data_list[i]
        stack.append(i)
    return result


l1 = ListNode(2)
l1.next = ListNode(7)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)
l1.next.next.next.next = ListNode(5)

# print(next_larger_nodes(l1))
print(next_larger_nodes2(l1))
