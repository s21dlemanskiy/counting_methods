import matplotlib.pyplot as plt
import numpy as np


def plot_result(x_arr, y_arr, function):
    for i in x_arr:
        pass
        # print(function(i))
    x = []
    y = []
    for i in np.arange(min(x_arr) - 1, max(x_arr) + 1, 0.1):
        x += [i]
        y += [function(i)]
    for i in range(len(x_arr)):
        plt.plot(x_arr[i], y_arr[i], 'ro', ms=15, mfc='r')
    plt.plot(x, y)
    plt.show()