# https://emre.me/coding-patterns/k-way-merge/

# How to identify?

# If the problem giving K sorted arrays and asks us to perform a sorted traversal 
# of all the elements of all arrays, we need to think about K-way Merge pattern.

# While solving the problems, we are going to use Heap data structure 
# to keep track of all elements in K arrays.


# Problem: Merge K Sorted Lists
# LeetCode 23 - Merge k Sorted Lists [hard]

# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# K-way Merge Solution

from heapq import heappop, heappush

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class ListNodeExtension(ListNode):
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        ListNode.__lt__ = ListNodeExtension.__lt__
        min_heap = []
        for root in lists:
            if root is not None:
                heappush(min_heap, root)

        head = tail = ListNode(0)
        while min_heap:
            tail.next = heappop(min_heap)
            tail = tail.next
            if tail.next:
                heappush(min_heap, tail.next)
        return head.next

# Time Complexity: O(N log K) where N is the total number of elements in all the K input arrays.

# Space Complexity: O(K)
