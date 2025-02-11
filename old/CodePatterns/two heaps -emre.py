# https://emre.me/coding-patterns/two-heaps/

# How to identify?

# This approach is quite useful when dealing with the problems 
# where we are given a set of elements such that we can divide them into two parts.

# To be able to solve these kinds of problems, 
# we want to know the smallest element in one part 
# and the biggest element in the other part. 
# Two Heaps pattern uses two Heap data structure 
# to solve these problems; a Min Heap to find the 
# smallest element and a Max Heap to find the biggest element.


# For example:

# [2, 3, 4], the median is 3

# [2, 3], the median is (2 + 3) / 2 = 2.5

# Design a data structure that supports the following two operations:

# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
# Example:

# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2

# Two Heaps Solution
# brute force

from heapq import heappush, heappop


class MedianFinder:
    def __init__(self):
        self.max_heap = []  # containing first half of numbers
        self.min_heap = []  # containing second half of numbers

    def addNum(self, num: int) -> None:
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        # either both heaps will have equal number of elements or max-heap will have one more element
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        # we have even number of elements, take the average of middle two elements
        if len(self.max_heap) == len(self.min_heap):
            return -self.max_heap[0] / 2.0 + self.min_heap[0] / 2.0
        # we have odd number of elements, the first element in max-heap is the median element
        return -float(self.max_heap[0])

# Time Complexity: O(log N) for addNum() and O(1) for findMedian().
# Space Complexity: O(N)
