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


n1 = 1
n2 = 1
count = 1
runtime = []

for ele in list_input:

    start = time.time()

    if int(ele) <= 0:
        print("Enter positive number")

    elif int(ele) == 1:
        print("Fibonacci: " + "\n" + str(n1))

    else:
        print("Fibonacci: ")
        while count <= int(ele):
            print(n1)
            cal_n = n1 + n2
            n1 = n2
            n2 = cal_n
            count += 1

    end = time.time()

    runtime.append([ele, end - start])

plot_time(runtime)