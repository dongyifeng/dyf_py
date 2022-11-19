class ListNode:
    def __init__(self, key="", val=0, next=None, prior=None):
        self.key = key
        self.val = val
        self.next = next
        self.prior = prior

# 有 bug
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = ListNode(None)
        self.map = {}
        self.max_node = ListNode("", None)

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.map:
            tmp = self.list.next
            node = ListNode(key, 1, next=tmp, prior=self.list)
            if tmp: tmp.prior = node
            self.list.next = node
            return

        node = self.map[key]
        node.val += 1
        if node.val > self.max_node.val:
            self.max_node = node

        if node.val > node.next.val:
            self.change(node, node.next)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.map: return
        node = self.map[key]
        node.val += 1
        if node.val <= 0:
            if key == self.max_node.key:
                self.max_node = node.prior
            del self.map[key]
            self.remove(node)
            return
        if node.val < node.prior.val:
            if key == self.max_node.key:
                self.max_node = node.prior
            self.swap(node.prior, node)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.max_node:
            return self.max_node.key
        return ""

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.list.next:
            return self.list.next.key
        return ""

    def swap(self, node, node_next):
        node_prior = node.prior
        if node_next.next:
            node.next = node_next.next
            node.prior = node_next
            node_next.next.prior = node

            node_prior.next = node_next
            node_next.next = node
            node_next.prior = node_prior
            return
        # node_next 为尾结点
        node_prior.next = node_next
        node_next.prior = node_prior
        node_next.next = node

        node.prior = node_next
        node.next = None

    def remove(self, node):
        node.prior.next = node.next
        if node.next:
            node.next.prior = node.prior




node = ListNode("key_1", 1)
node.next = ListNode("key_2", 2)
node.next.prior = node
node.next.next = ListNode("key_3", 3)
node.next.next.prior = node.next
node.next.next.next = ListNode("key_4", 4)
node.next.next.next.prior = node.next.next
#
# print(node.next.val)
print(node.next.next.val)

# change(node.next.next, node.next.next.next)
remove(node.next.next.next)
print()

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
