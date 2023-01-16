# def heapify(input_arr, i):
#     upper_index = i  # index
#     left_index = 2 * i + 1
#     right_index = 2 * i + 2
#
#     if left_index < len(input_arr) and input_arr[upper_index] < input_arr[left_index]:
#         upper_index = left_index  # set left as upper
#
#     if right_index < len(input_arr) and input_arr[upper_index] < input_arr[right_index]:
#         upper_index = right_index  # set right as upper
#
#     if upper_index != i:  # index of upper is change, new upper
#         input_arr[i], input_arr[upper_index] = input_arr[upper_index], input_arr[i]  # swap
#
#         heapify(input_arr, upper_index)  # if swap check again
#
#
# def heapsort(arr):
#     n = len(arr)
#
#     for num in range(n // 2 - 1, 0, -1):  # start, stop, step
#         print(num)
#         heapify(arr, num)
#
#
# if __name__ == '__main__':
#     arr = [12, 5, 13, 9, 6, 7, 22]
#
#     # Function call
#     heapsort(arr)
#     N = len(arr)
#
#     print("Sorted array is")
#     for ele in arr:
#         print(ele, end=" ")

import math


def buildheap(heap, size):
    for num in range(size):
        print("heap:")
        print(heap)
        reheapup(heap, num)


def reheapup(heap, new_index):
    parent_index = math.ceil((new_index - 2) / 2)  # roundup

    print("parent index: " + str(parent_index))
    print("index: " + str(new_index))

    if parent_index >= 0 and heap[new_index] > heap[parent_index]:
        swap_v = heap[parent_index]
        heap[parent_index] = heap[new_index]
        heap[new_index] = swap_v

        reheapup(heap, parent_index)


if __name__ == '__main__':
    arr = [8, 19, 23, 32, 45, 56, 78, 100]

    # Function call
    buildheap(arr, len(arr))
    N = len(arr)

    print("Sorted array is")
    for ele in arr:
        print(ele, end=" ")

