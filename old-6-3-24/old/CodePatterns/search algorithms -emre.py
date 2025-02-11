# https://emre.me/algorithms/search-algorithms/

# Linear Search Implementation

# In short we can say that, performance of Linear Search is O(1) 
# for the best case and O(N) for the average case and worst case.

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
  
# Binary Search Implementation without Recursion

# So, we can say that, performance of Binary search is O(1) 
# for the best case and O(logN) for the average case and 
# worst case which is much better than Linear Search!

def binary_search(arr, key):
    start = 0
    end = len(arr)
    while start < end:
        mid = (start + end)//2
        if arr[mid] > key:
            end = mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            return mid
    return -1

# Binary Search Implementation with Recursion
def recursive_binary_search(arr, start, end, key):
    if not start < end:
        return -1
    mid = (start + end) // 2
    if arr[mid] < key:
        return recursive_binary_search(arr, mid + 1, end, key)
    elif arr[mid] > key:
        return recursive_binary_search(arr, start, mid, key)
    else:
        return mid
