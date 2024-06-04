# https://emre.me/data-structures/heaps/

# Time Complexity
# Average and Worst Case time complexites of the heap data structure is as follows.

# Operation	Average	Worst Case
# Search	O(n)	O(n)
# Insert	O(1)	O(log n)
# Delete	O(log n)	O(log n)
# Peek	O(1)	O(1)

# What is a Heap?
# A heap is a special Tree-based data structure in which the tree is a 
# complete Binary Tree in which each level has all of its nodes. 
# The exception to this is the bottom level of the tree, which we 
# fill in from left to right.

# It is called;

# Min Heap, if each parent node is less than or equal to its child node
# Max Heap, if each parent node is greater than or equal to its child node
# The heap above is called a Min Heap since, each value of nodes is less than or equal to the value of child nodes.

# Implementation

# min_heapify() and build_min_heap()
def get_left_child(i):
    return 2 * i + 1

def get_right_child(i):
    return 2 * i + 2

def min_heapify(arr, i):
    left = get_left_child(i)
    right = get_right_child(i)
    smallest = i

    if left < len(arr) and arr[i] > arr[left]:
        smallest = left
    if right < len(arr) and arr[smallest] > arr[right]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, smallest)

# and now we can repeatedly call min_heapify() function in order to build a Min Heap.

def build_min_heap(arr):
    for i in reversed(range(len(arr)//2)):
        min_heapify(arr, i)
        
# max_heapify() and build_max_heap()
def max_heapify(arr, i):
    left = get_left_child(i)
    right = get_right_child(i)
    largest = i

    if left < len(arr) and arr[left] > arr[largest]:
        largest = left
    if right < len(arr) and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest)

# and now we can repeatedly call max_heapify() function in order to build a Max Heap.

def build_max_heap(arr):
    for i in reversed(range(len(arr)//2)):
        max_heapify(arr, i)
