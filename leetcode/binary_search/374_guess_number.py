# 374. 猜数字大小


class Solution(object):
    def __init__(self, num):
        self.num = num

    def guess_number(self, n):
        left = 0
        right = n
        while left < right:
            mid = (left + right) >> 1
            tmp = self.guess(mid)
            if tmp == 0: return mid
            if tmp == -1:
                left = mid + 1
            else:
                right = mid - 1

    def guess(self, pick):
        if pick == self.num: return 0
        if pick < self.num: return -1
        if pick > self.num: return 1


solution = Solution(6)
print(solution.guess_number(10))
