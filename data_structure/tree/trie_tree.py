class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.data = None
        self.children = {}

    def is_data_node(self):
        return self.data is not None

    def is_leaf_node(self):
        return len(self.children) == 0


class Trie:
    def __init__(self):
        self.root = TrieNode("/")

    def insert(self, text):
        if not text: return
        p = self.root
        for char in text:
            if char not in p.children:
                p.children[char] = TrieNode(char)
            p = p.children[char]
        p.data = text

    def find_node(self, pattern):
        if not pattern: return
        p = self.root
        for char in pattern:
            if char not in p.children: return
            p = p.children[char]
        return p

    def find(self, pattern):
        node = self.find_node(pattern)
        if node: return node.data

    def prefix_find(self, pattern):
        node = self.find_node(pattern)
        if not node: return
        res = []
        for k, v in node.children.items():
            self.drill_down(v, res)

        return res

    def drill_down(self, node, res):
        if node.data:
            res.append(node.data)
        for k, v in node.children.items():
            self.drill_down(v, res)

    def delete(self, pattern):
        if not pattern: return

        # 查找要删除的节点
        p = self.root
        stack = [p]
        for char in pattern:
            if char not in p.children: return
            p = p.children[char]
            stack.append(p)
        if not p.data or p.data != pattern: return
        # 删除数据
        p.data = None

        # 删除路径
        node = stack.pop()
        while stack:
            parent = stack.pop()
            if not node.is_leaf_node() or node.is_data_node() or node.char not in parent.children:
                break
            parent.children.pop(node.char)
            node = parent


trie_tree = Trie()
trie_tree.insert("zgpn")
trie_tree.insert("中兴通讯")
trie_tree.insert("中国银行")
trie_tree.insert("中国平安")
trie_tree.insert("中信证券")
trie_tree.insert("平安银行")


print(trie_tree.prefix_find("中"))

trie_tree.delete("中国平安")

print(trie_tree.prefix_find("中"))
