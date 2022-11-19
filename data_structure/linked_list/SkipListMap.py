import random


class Node:
    def __init__(self, key, value, max_level):
        self.value = value
        self.key = key
        self.next_nodes = [None] * max_level

    def __lt__(self, other):
        return self.key < other

    def __eq__(self, other):
        return self.key == other

    def __ge__(self, other):
        return self.key > other


class SkipListMap:
    def __init__(self):
        self.head = Node(-1, -1, 1)

    def insert(self, key, value):
        self.insert_level(key, value, self.get_random_level())

    def insert_level(self, key, value, level):
        self.expand_head(level)

        new_node = Node(key, value, level)

        update_arr = [self.head] * len(self.head.next_nodes)
        p = self.head

        n = len(self.head.next_nodes)
        for i in range(n - 1, -1, -1):
            while p.next_nodes[i] and p.next_nodes[i].key < key:
                p = p.next_nodes[i]
            update_arr[i] = p

        # 加入 new_node
        for i in range(level):
            new_node.next_nodes[i] = update_arr[i].next_nodes[i]
            update_arr[i].next_nodes[i] = new_node

    def delete(self, key):
        n = len(self.head.next_nodes)
        update_arr = [None] * n
        p = self.head
        # 查找需要更新结点
        for i in range(n - 1, -1, -1):
            while p.next_nodes[i] and p.next_nodes[i].key < key:
                p = p.next_nodes[i]
            update_arr[i] = p

        # 删除节点
        if p.next_nodes and p.next_nodes[0].value != key: return

        # 删除节点
        for i in range(n - 1, -1, -1):
            if update_arr[i].next_nodes[i] and update_arr[i].next_nodes[i].value == key:
                update_arr[i].next_nodes[i] = update_arr[i].next_nodes[i].next_nodes[i]

    def expand_head(self, level):
        n = len(self.head.next_nodes)
        if level < n:
            return
        for _ in range(level - n):
            self.head.next_nodes.append(None)

    def get_random_level(self):
        res = 1
        while int(random.random() * 2) != 0:
            res += 1
        return res

    def find(self, key):
        p = self.head
        for i in range(len(self.head.next_nodes) - 1, -1, -1):
            while p.next_nodes[i] and p.next_nodes[i].key < key:
                p = p.next_nodes[i]

        return p

    def __contains__(self, item):
        node = self.find(item)
        return node.next_nodes[0] and node.next_nodes[0].key == item

    def first(self):
        return self.head.next_nodes[0].key

    def last(self):
        p = self.head
        n = len(self.head.next_nodes)
        for i in range(n - 1, -1, -1):
            while p.next_nodes[i]:
                p = p.next_nodes[i]

        return p.key

    def floor(self, key):
        node = self.find(key)
        if node.next_nodes[0] and node.next_nodes[0].value == key:
            return key
        return node.key

    def ceiling(self, key):
        node = self.find(key)
        if node.next_nodes[0] and node.next_nodes[0].value == key:
            return key

        if node.next_nodes[0]:
            return node.next_nodes[0].key


skipList = SkipListMap()
skipList.insert_level(3, None, 3)
skipList.insert_level(10, None, 2)
skipList.insert_level(15, None, 4)
skipList.insert_level(20, None, 6)
skipList.insert_level(30, None, 1)
skipList.insert_level(40, None, 4)
skipList.insert_level(50, None, 5)
skipList.insert_level(70, None, 2)
skipList.insert_level(100, None, 6)

print(40 in skipList)
print(60 in skipList)

print(skipList.first())
print(skipList.last())
print("-" * 100)
print(skipList.ceiling(50))
print(skipList.ceiling(60))

print(skipList.floor(50))
print(skipList.floor(60))
