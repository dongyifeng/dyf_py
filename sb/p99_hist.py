import pandas as pd

import matplotlib.pyplot as plt


def run(path):
    data = []
    for line in open(path, "r"):
        try:
            data.append(int(line.strip()))
        except Exception as err:
            print(err)
    plt.hist(data, bins=500)
    plt.xlabel('cost')
    plt.ylabel('count')
    plt.show()


run("/Users/dongyf/Desktop/sled_rank_total_v2")
