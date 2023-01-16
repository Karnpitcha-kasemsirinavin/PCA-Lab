import math
import random as rd
from matplotlib import pyplot as plt
import time
import numpy as np


class Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __repr__(self):
        return "".join(["(", str(self.x), ",", str(self.y), ")"])

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def distance(self, other):
        cal_dis = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return cal_dis


def generate_point(amount):

    list_point = []
    for index in range(0, amount):
        x = rd.randint(-1000, 1000)
        y = rd.randint(-1000, 1000)

        # plt.plot(x, y, marker='o', markersize=2, color="blue")
        list_point.append(Point(x, y))

    return list_point


def findcloset(arr):

    min_dis = 100000000
    points = []

    for index in range(len(arr)):
        for j in range(index + 1, len(arr)):
            distance = arr[index].distance(arr[j])

            if distance < min_dis:
                points = []
                min_dis = distance
                points.append([arr[index], arr[j]])

            elif distance == min_dis:
                points.append([arr[index], arr[j]])

    print(min_dis, points)


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


'''======================================================================='''

'''Setup'''
plt.rcParams['figure.figsize'] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

'''Graph axes values'''
plt.xlim(100, 10000)
plt.ylim(0, 60)

num_point = input('Number of points (Ex.100,200): ').split(",")
num_point = [int(i) for i in num_point]
time_list = []

if num_point == 1:
    print("Error")

else:

    for ele in num_point:

        point_list = generate_point(ele)
        '''Start calculating'''
        '''seconds'''
        start = time.time()
        findcloset(point_list)
        end = time.time()
        time_list.append([ele, end - start])


'''-------------------------------------------------------------------------'''

plot_time(time_list)
