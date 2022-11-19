class BitMap:
    def __init__(self, max_value):
        self.bitmap = [0] * (int(max_value / 64) + 1)

    def add(self, item):
        index, offset = self.getIndexOffset(item)
        self.bitmap[index] |= 1 << offset

    def remove(self, item):
        index, offset = self.getIndexOffset(item)
        self.bitmap[index] &= ~(1 << offset)

    def __contains__(self, item):
        index, offset = self.getIndexOffset(item)
        res = self.bitmap[index] & (1 << offset)
        return res != 0

    def getIndexOffset(self, item):
        return int(item / 64), item % 64




'''
public static void main(String[] args) {
		System.out.println("测试开始！");
		int max = 10000;
		BitMap bitMap = new BitMap(max);
		HashSet<Integer> set = new HashSet<>();
		int testTime = 10000000;
		for (int i = 0; i < testTime; i++) {
			int num = (int) (Math.random() * (max + 1));
			double decide = Math.random();
			if (decide < 0.333) {
				bitMap.add(num);
				set.add(num);
			} else if (decide < 0.666) {
				bitMap.delete(num);
				set.remove(num);
			} else {
				if (bitMap.contains(num) != set.contains(num)) {
					System.out.println("Oops!");
					break;
				}
			}
		}
		for (int num = 0; num <= max; num++) {
			if (bitMap.contains(num) != set.contains(num)) {
				System.out.println("Oops!");
			}
		}
		System.out.println("测试结束！");
	}
'''



bitmap = BitMap(10)
bitmap.add(1)
bitmap.add(2)
bitmap.add(5)
bitmap.add(7)

print(bitmap.bitmap[0])

print(1 in bitmap)
print(2 in bitmap)
print(3 in bitmap)
print(4 in bitmap)
print(5 in bitmap)
print(7 in bitmap)

