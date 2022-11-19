class Employee:
    def __init__(self, happy, subordinates):
        self.happy = happy
        self.subordinates = subordinates


class Info:
    def __init__(self, yes, no):
        # X 来，整棵树 happy 值
        self.yes = yes
        # X 不来，整棵树 happy 值
        self.no = no


def max_happy(head):
    if not head: return 0
    return process(head).max_sub_sbt_size


def process(X):
    if not X: return Info(X.happy, 0)

    yes = X.happy
    no = 0
    # 遍历
    for item in X.subordinates:
        info = process(item)
        # X 来的 happy 值
        yes += info.no
        # X 不来的 happy 值
        no += max(info.yes, info.no)

    return Info(yes, no)
