# https://emre.me/algorithms/sorting-algorithms/

# Time Complexities of Sorting Algorithms
# If we are talking about algorithms, then the most important factor which affects our decision process is time and space complexity.

# Algorithm	Time Complexity (Best)	Time Complexity (Average)	Time Complexity (Worst)	Space Complexity
# Bubble Sort	O(n)	O(n2)	O(n2)	O(1)
# Selection Sort	O(n2)	O(n2)	O(n2)	O(1)
# Insertion Sort	O(n)	O(n2)	O(n2)	O(1)
# Merge Sort	O(n log(n))	O(n log(n))	O(n log(n))	O(n)
# Heap Sort	O(n log(n))	O(n log(n))	O(n log(n))	O(1)
# Quick Sort	O(n log(n))	O(n log(n))	O(n2)	O(log(n))
# Radix Sort	O (nk)	O(nk)	O(nk)	O(n+k)
# Tim Sort	O(n)	O(n log(n))	O(n log(n))	O(n)


# Bubble Sort
def bubble_sort(array):
    # We set swapped to True so the loop runs at least once
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                # Swap the elements
                array[i] = array[i + 1]
                array[i + 1] = array[i]
                # Set the flag to True so we'll loop again
                swapped = True
    return array


# Selection Sort
def selection_sort(array):
    for i in range(len(array)):
        # We assume that the first item of the unsorted segment is the smallest
        min_value = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min_value]:
                min_value = j

        # Swap values of the lowest unsorted element with the first unsorted element
        array[i] = array[min_value]
        array[min_value] = array[i]
    return array


# Insertion Sort
def insertion_sort(array):
    # We assume that the first item is sorted
    for i in range(1, len(array)):
        picked_item = array[i]

        # Reference of the index of the previous element
        j = i - 1

        # Move all items to the right until finding the correct position
        while j >= 0 and array[j] > picked_item:
            array[j + 1] = array[j]
            j -= 1

        # Insert the item
        array[j + 1] = picked_item

    return array


# Merge Sort
def merge_sort(array):
    # If the list is a single element, return it
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    # Recursively sort and merge each half
    l_list = merge_sort(array[:mid])
    r_list = merge_sort(array[mid:])

    # Merge the sorted lists into a new one
    return _merge(l_list, r_list)


def _merge(l_list, r_list):
    result = []
    l_index, r_index = 0, 0

    for i in range(len(l_list) + len(r_list)):
        if l_index < len(l_list) and r_index < len(r_list):

            # If the item at the beginning of the left list is smaller, add it to the sorted list
            if l_list[l_index] <= r_list[r_index]:
                result.append(l_list[l_index])
                l_index += 1

            # If the item at the beginning of the right list is smaller, add it to the sorted list
            else:
                result.append(r_list[r_index])
                r_index += 1

        # If we have reached the end of the of the left list, add the elements from the right list
        elif l_index == len(l_list):
            result.append(r_list[r_index])
            r_index += 1

        # If we have reached the end of the of the right list, add the elements from the left list
        elif r_index == len(r_list):
            result.append(l_list[l_index])
            l_index += 1

    return result


# Heap Sort
def get_left_child(i):
    return 2 * i + 1


def get_right_child(i):
    return 2 * i + 2


def max_heapify(arr, n, i):
    left = get_left_child(i)
    right = get_right_child(i)
    largest = i

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # build the max heap
    for i in range(n, -1, -1):
        max_heapify(arr, n, i)

    # extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)

    return arr


# Heap Sort With Heapq
import heapq


def heap_sort(array):
    h = []
    for value in array:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


# Quick Sort
def partition(array, low, high):
    # We select the middle element to be the pivot
    pivot = array[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while array[i] < pivot:
            i += 1

        j -= 1
        while array[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Swap
        array[i], array[j] = array[j], array[i]


def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)


def quick_sort_helper(items, low, high):
    if low < high:
        split_point = partition(items, low, high)
        quick_sort_helper(items, low, split_point)
        quick_sort_helper(items, split_point + 1, high)


# Lomuto partition scheme
def partition(array, low, high):
    pivot = array[high]

    i = low
    j = low
    while j < high:
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1

        j += 1

    # swap
    array[i], array[high] = array[high], array[i]

    return i


def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)


def quick_sort_helper(items, low, high):
    if low < high:
        split_point = partition(items, low, high)
        quick_sort_helper(items, low, split_point - 1)
        quick_sort_helper(items, split_point + 1, high)

# Python’s Built-in Sort Functions
# sort()
# We can change our list to have it’s contents sorted with the sort() method:

arr = [4, 7, 224, 19, 1, 5, 3, 10, 187, 13, 2]
arr.sort()

print(arr)
# Output: [1, 2, 3, 4, 5, 7, 10, 13, 19, 187, 224]

arr.sort(reverse=True)

print(arr)
# Output: [224, 187, 19, 13, 10, 7, 5, 4, 3, 2, 1]

# sorted()
# The sorted() function can sort any iterable object, 
# that includes - lists, strings, tuples, dictionaries, sets, 
# and custom iterators you can create.

arr = [4, 7, 224, 19, 1, 5, 3, 10, 187, 13, 2]
sorted_arr = sorted(arr)

print(sorted_arr)
# Output: [1, 2, 3, 4, 5, 7, 10, 13, 19, 187, 224]
 
reverse_sorted_arr = sorted(arr, reverse=True)

print(reverse_sorted_arr)
# Output: [224, 187, 19, 13, 10, 7, 5, 4, 3, 2, 1]
