import matplotlib.pyplot as plt

import math

def run(path):
    data = []
    for line in open(path, "r"):
        try:
            data.append(int(line.strip()))
        except Exception as err:
            print(err)
    print("len",len(data))
    print("max",max(data))
    print("min",min(data))

    plt.plot([item for item in range(len(data))], data)
    plt.xlabel('index')
    plt.ylabel('ms')
    plt.show()


run("/Users/dongyf/Desktop/p99_all")
