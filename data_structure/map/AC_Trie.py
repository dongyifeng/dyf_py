class AcNode:
    def __init__(self):
        self.data = None
        self.children = {}
        # 当节点为结束结点时，模式串的长度
        self.length = -1
        # 失败指针
        self.fail = None


class AC:
    def __init__(self):
        self.root = AcNode()

    def add(self, word):
        p = self.root
        for char in word:
            # 只有结束结点才写入 data
            if char not in p.children:
                p.children[char] = AcNode()
            p = p.children[char]
        p.data = word
        p.length = len(word)

    def build_failure_pointer(self):
        queue = [self.root]
        while queue:
            p = queue.pop(0)
            for key, pc in p.children.items():
                q = p.fail
                while q:
                    qc = q.children.get(key, None)
                    if qc:
                        pc.fail = qc
                        break
                    q = q.fail
                if q is None:
                    pc.fail = self.root
                queue.append(pc)

    def match(self, text):
        res = []
        p = self.root
        for i, char in enumerate(text):
            # 一个新 char ，通过 fail 寻找合适 node，开始查询
            while char not in p.children and p != self.root:
                p = p.fail

            # 如果没有匹配，从 root 开始。
            p = p.children[char] if char in p.children else self.root
            tmp = p
            while tmp != self.root:
                if tmp.data is not None:
                    pos = i - tmp.length + 1
                    print('匹配起始下标' + str(pos) + ";长度:" + str(tmp.length))
                    res.append(tmp.data)
                tmp = tmp.fail
        return res


if __name__ == "__main__":
    ac = AC()
    # 加载敏感词表
    ac.add("基金")
    ac.add("相关基金")
    ac.add("关基")

    ac.add("相关")

    ac.build_failure_pointer()
    text = "白酒相关基金"
    print(ac.match(text))
