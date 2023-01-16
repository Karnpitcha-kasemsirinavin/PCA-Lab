from matplotlib import pyplot as plt
import random as rd
import math

'''Setup'''
plt.rcParams['figure.figsize'] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

'''Coordinate'''
# x = [4]
# y = [3]

'''Graph axes values'''
plt.xlim(-500, 500)
plt.ylim(-500, 500)

def generate_point(input_point):

    list_point = []
    for index in range(0, input_point):
        x = rd.randint(-500, 500)
        y = rd.randint(-500, 500)

        plt.plot(x, y, marker='o', markersize=2, color="blue")
        list_point.append((x, y))

    return list_point


def cal_dis(arr):

    print(arr)
    distance_dict = {}

    for i in range(len(arr)):
        for j in range(1, len(arr)):

            distance = math.sqrt(abs(arr[i][0] - arr[j][0])**2
                                 + abs(arr[i][1] - arr[j][1])**2)

            if max(distance_dict) < distance:

            elif max(distance_dict) == distance:
                pass

num_point = int(input('Number of points: '))
point_list = generate_point(num_point)
cal_dis(point_list)z

