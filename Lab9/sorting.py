# Insertion sort

def insertion_sort(input_arr):
    for num in range(1, len(input_arr)):  # don't have to start at 0
        hold = input_arr[num]  # call current value at index

        walker = num - 1  # call pre sorted value

        # compare current value with sorted value
        while walker >= 0 and hold < input_arr[walker]:
            input_arr[walker + 1] = input_arr[walker]  # swap
            walker -= 1

        input_arr[walker + 1] = hold  # locate current value


# a = [5, 9, 0, 11, 100, 22]
#
# print("Insertion: ")
# insertion_sort(a)
# print(a)


def selection_sort(input_arr):
    for num in range(len(input_arr)):
        smallest = num  # set current value as smallest

        for index in range(num + 1, len(input_arr)):
            if input_arr[index] < input_arr[smallest]:  # compare with other unsorted element
                smallest = index

        current_v = input_arr[num]  # assign new value
        input_arr[num] = input_arr[smallest]
        input_arr[smallest] = current_v


# a = [5, 9, 0, 11, 100, 22]
#
# print("Selection: ")
# selection_sort(a)
# print(a)
#

def bubble_sort(input_arr):
    current = 0
    sorted = False

    while current < len(input_arr) and sorted is False:
        walker = len(input_arr) - 1
        sorted = True

        while walker > current:
            if input_arr[walker] < input_arr[walker - 1]:
                current_v = input_arr[walker]
                input_arr[walker] = input_arr[walker - 1]
                input_arr[walker - 1] = current_v

            walker -= 1

        current += 1


a = [5, 9, 0, 11, 100, 22]

print("Bubble: ")
bubble_sort(a)
print(a)

def quick_sort(input_arr, left_index, right_index):

    if left_index >= right_index:
        return

    pivot = input_arr[right_index]
    left = left_index
    right = right_index - 1

    while left <= right:
        # find key on left that should be on the right
        while input_arr[left] < pivot:
            left += 1

        while input_arr[right] > pivot:
            right -= 1

        if left <= right:
            left_v = input_arr[left]
            input_arr[left] = input_arr[right]
            input_arr[right] = left_v

            left += 1
            right -= 1

    left_v = input_arr[left]
    input_arr[left] = input_arr[len(input_arr)-1]
    input_arr[len(input_arr)-1] = left_v

    # check left side of arr
    quick_sort(input_arr, left_index, right)
    # check right side of arr
    quick_sort(input_arr, left, len(input_arr)-1)

a = [5, 9, 0, 11, 100, 22]

print("Quick: ")
quick_sort(a, 0, len(a)-1)
print(a)

def merge_sort():
