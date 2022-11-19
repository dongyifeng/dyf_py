import random


class Node:
    def __init__(self, value, max_level):
        self.value = value
        self.next_nodes = [self] * max_level

    def __lt__(self, other):
        return self.key < other

    def __eq__(self, other):
        return self.key == other

    def __ge__(self, other):
        return self.key > other


class SkipList:
    def __init__(self):
        self.level_count = 1
        self.head = Node

    def find(self, value):
        p = self.head
        for i in range(self.level_count - 1, -1, -1):
            while p.next_nodes[i] and p.next_nodes[i].value < value:
                p = p.next_nodes[i]

        if p.next_nodes[0] and p.next_nodes[0].value == value:
            return p.next_nodes[0].value

    def insert(self, value):
        level = self.get_random_level()

        new_node = Node(value, level)
        update_arr = [self.head] * level
        p = self.head

        for i in range(level - 1, -1, -1):
            while p.next_nodes[i] and p.next_nodes[i].value < value:
                p = p.next_nodes[i]
            update_arr[i] = p

        # 加入 new_node
        for i in range(level):
            new_node.next_nodes[i] = update_arr[i].next_nodes[i]
            update_arr[i].next_nodes[i] = new_node

        self.level_count = max(self.level_count, level)

    def delete(self, value):
        update_arr = [None] * self.level_count
        p = self.head
        for i in range(self.level_count - 1, -1, -1):
            p = p.next_nodes[i]
            update_arr[i] = p

        if p.next_nodes and p.next_nodes[0].value == value:
            for i in range(self.level_count - 1, -1, -1):
                if update_arr[i].next_nodes[i] and update_arr[i].next_nodes[i].value == value:
                    update_arr[i].next_nodes[i] = update_arr[i].next_nodes[i].next_nodes[i]

    def expand_head(self, level):
        n = len(self.head)
        if level < n:
            return
        for _ in range(level - n):
            self.head.next_nodes.append(Node())

    def get_random_level(self):
        res = 1
        while int(random.random() * 2) != 0:
            res += 1
        return res
