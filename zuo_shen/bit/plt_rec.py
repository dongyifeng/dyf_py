'''
'''
import matplotlib.pyplot as plt

color = ["maroon", "green", "orange", "yellow"]


def plt_rec(arr):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    i = 0
    for x1, y1, x2, y2 in arr:
        rect = plt.Rectangle((x1 * 0.1, y1 * 0.1), (x2 - x1) * 0.1, (y2 - y1) * 0.1, color=color[i], alpha=0.5)
        i += 1
        ax.add_patch(rect)
    plt.show()


arr = [(3, 3, 8, 6),(5, 1, 7, 4), (4, 1, 7, 5), (4, 3, 6, 5) ]
plt_rec(arr)
