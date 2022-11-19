'''
小虎去附近的商店买苹果，奸诈的商贩使用了捆绑交易，只提供 6 个每袋和 8 个每袋的包装，包装不可拆分。可是小虎现在只想购买恰好 n 个苹果，
小虎想购买尽量少的袋数方便携带。如果不能购买恰好 n 个苹果，小虎将不会购买。输入一个整数 n ,表示小虎想购买的苹果，返回最少使用多少袋子。
如果无论如何都不能正好装下，返回 -1.
'''


# 如果剩余苹果 rest 可以装满小袋子，返回小袋子树
# 否则返回 -1
def min_bag_base6(rest):
    return int(rest / 6) if rest % 6 == 0 else -1


def min_bags(apple):
    if apple < 0: return -1
    bg6 = -1
    bg8 = int(apple / 8)
    rest = apple - 8 * bg8
    while bg8 >= 0 and rest < 24:
        rest_use6 = min_bag_base6(rest)
        if rest_use6 != -1:
            bg6 = rest_use6
            break
        bg8 -= 1
        rest = apple - 8 * bg8

    return -1 if bg6 == -1 else bg6 + bg8


def min_bags2(apple):
    if apple < 0 or apple % 2 != 0: return -1
    if apple < 18:
        tmp = {0: 0, 6: 1, 8: 1, 12: 2, 14: 2, 16: 2}
        return tmp[apple] if apple in tmp else -1
    return int((apple - 18) / 8) + 3

    return -1 if bg6 == -1 else bg6 + bg8


# for i in range(100):
#     print(i, min_bags(i), min_bags2(i))

print("-" * 100)
'''
给定一个正整数 N，表示有 N 份青草统一堆放在仓库里。有一只牛和一只羊，牛先吃，羊后吃，他两个轮流吃草。不管是牛还是羊，
每一轮能吃的草量必须是：1,4,16,64...(4的某次方)。谁最先把草吃完，谁获胜。假设牛和羊都绝顶聪明，都想赢，都会做出理性的决定。
根据唯一的参数 N，返回谁会盈。
'''


def winner1(n):
    # n: 0  1  2  3  4
    # 赢 后 先  后 先 先
    if n < 5: return "后手" if n == 0 or n == 2 else "先手"
    # n > 5
    base = 1  # 先手决定吃的草

    while base <= n:
        # 当前一共 n 份草，先手吃掉的是 base 份，n - base 是留个后手的草
        # 母过程中的先手，在子过程里就是 后手
        if winner1(n - base) == "后手":
            return "先手"
        if base > int(n / 4):
            break
        base *= 4
    return "后手"


def winner2(n):
    if n % 5 == 0 or n % 5 == 2:
        return "后手"
    return "先手"


for i in range(50):
    print(i, winner1(i), winner2(i))
