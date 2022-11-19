# 账户合并
# 给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其余元素是 emails 表示该账户的邮箱地址。
#
# 现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。
#
# 合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。账户本身可以以任意顺序返回。


# 输入：
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# 输出：
# [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# 解释：
# 第一个和第三个 John 是同一个人，因为他们有共同的邮箱地址 "johnsmith@mail.com"。
# 第二个 John 和 Mary 是不同的人，因为他们的邮箱地址没有被其他帐户使用。
# 可以以任何顺序返回这些列表，例如答案 [['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']，
# ['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']] 也是正确的。


def account_merge(accounts):
    tmp = False
    for i in range(len(accounts)):
        if len(accounts[i]) == 0: continue
        name_i = accounts[i][0]
        for j in range(i + 1, len(accounts)):
            if len(accounts[j]) == 0: continue
            name_j = accounts[j][0]
            if name_i != name_j: continue
            emails_i = set(accounts[i][1:])
            emails_j = set(accounts[j][1:])

            intersection_set = emails_i & emails_j
            if intersection_set:
                accounts[i] = [name_i] + list(emails_i | emails_j)
                accounts[j] = []
                tmp = True

    accounts = [item for item in accounts if item]
    if tmp: return account_merge(accounts)
    return [[item[0]] + sorted(set(item[1:])) for item in accounts if item]


class DisjointSet:
    def __init__(self, node_count):
        self.parent = [None] * node_count
        self.rank = [-1] * node_count

    def find_root(self, x):
        x_root = x
        while self.parent[x_root]:
            x_root = self.parent[x_root]
        return x_root

    def union(self, x, y):
        x_root = self.find_root(x)
        y_root = self.find_root(y)
        if x_root == y_root:
            return False
        self.parent[x_root] = y_root


def account_merge2(accounts):
    email_name_map = {}
    for item in accounts:
        name = item[0]
        emails = set(item[1:])
        for email in emails:
            email_name_map[email] = name

    disjoint_set = DisjointSet(len(email_name_map))





accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]

# accounts = [["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"],
#             ["David", "David4@m.co", "David5@m.co"],
#             ["David", "David2@m.co", "David3@m.co"], ["David", "David1@m.co", "David2@m.co"]]
# accounts = [["Hanzo", "Hanzo2@m.co", "Hanzo3@m.co"], ["Hanzo", "Hanzo4@m.co", "Hanzo5@m.co"],
#             ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co"],
#             ["Hanzo", "Hanzo3@m.co", "Hanzo4@m.co"], ["Hanzo", "Hanzo7@m.co", "Hanzo8@m.co"],
#             ["Hanzo", "Hanzo1@m.co", "Hanzo2@m.co"],
#             ["Hanzo", "Hanzo6@m.co", "Hanzo7@m.co"], ["Hanzo", "Hanzo5@m.co", "Hanzo6@m.co"]]

# accounts = [["Lily", "Lily4@m.co", "Lily5@m.co"], ["Lily", "Lily8@m.co", "Lily9@m.co"],
#             ["Lily", "Lily15@m.co", "Lily16@m.co"], ["Lily", "Lily19@m.co", "Lily20@m.co"],
#             ["Lily", "Lily6@m.co", "Lily7@m.co"], ["Lily", "Lily10@m.co", "Lily11@m.co"],
#             ["Lily", "Lily5@m.co", "Lily6@m.co"], ["Lily", "Lily13@m.co", "Lily14@m.co"],
#             ["Lily", "Lily9@m.co", "Lily10@m.co"], ["Lily", "Lily1@m.co", "Lily2@m.co"],
#             ["Lily", "Lily3@m.co", "Lily4@m.co"], ["Lily", "Lily2@m.co", "Lily3@m.co"],
#             ["Lily", "Lily11@m.co", "Lily12@m.co"], ["Lily", "Lily7@m.co", "Lily8@m.co"],
#             ["Lily", "Lily12@m.co", "Lily13@m.co"], ["Lily", "Lily18@m.co", "Lily19@m.co"],
#             ["Lily", "Lily17@m.co", "Lily18@m.co"], ["Lily", "Lily16@m.co", "Lily17@m.co"],
#             ["Lily", "Lily14@m.co", "Lily15@m.co"], ["Lily", "Lily0@m.co", "Lily1@m.co"]]

new_account = account_merge(accounts)
for item in new_account:
    print(item)

a = [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
     ["Mary", "mary@mail.com"],
     ["John", "johnnybravo@mail.com"]]
