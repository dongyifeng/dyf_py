import sys


class Bucket:
    def __init__(self, start=0, end=sys.maxsize, count=0):
        self.start = start
        self.end = end
        self.count = count


def get_median(file_name):
    return nums


def process(file_name, start, end, mindle, bucket_count,total_count):


    if end -  start < bucket_count:
        return get_median()



    bucket_list = []

    for line in open("fileNam", "r"):
        num = int(line.strip())




def get_median2(nums):
    data.sort()
    n = len(data)
    print(n)
    if n % 2 == 0:
        return (data[int(n / 2)] + data[int(n / 2) - 1]) >> 1

    return data[int(n / 2)]

def get_median2(nums):
    data.sort()
    n = len(data)
    print(n)
    if n % 2 == 0:
        return (data[int(n / 2)] + data[int(n / 2) - 1]) >> 1

    return data[int(n / 2)]


data = [4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 2, 3, 4]

data.sort()
print(data)

print(get_median2(data))
