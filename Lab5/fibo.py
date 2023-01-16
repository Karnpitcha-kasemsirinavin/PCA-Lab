import time
import numpy as np
from matplotlib import pyplot as plt

list_input = input().split(",")


def plot_time(arr):

    xaxis_arr = []
    yaxis_arr = []

    for ele in arr:
        '''x is points, y is time'''
        xaxis_arr.append(ele[0])
        yaxis_arr.append(ele[1])

    xaxis = np.array(xaxis_arr)
    yaxis = np.array(yaxis_arr)

    plt.plot(xaxis, yaxis, marker='o', markersize=2, color="blue")
    plt.show()


def fib(n):

    if n <= 1:
        return n

    else:
        f = fib(n-1)+fib(n-2)

    return f


runtime = []

for ele in list_input:

    start = time.time()

    if int(ele) <= 0:
        print("Enter a positive number")
    else:
        print("Fibonacci:")
        print(fib(int(ele)))

    end = time.time()

    runtime.append([ele, end-start])

plot_time(runtime)



