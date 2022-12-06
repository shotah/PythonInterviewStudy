# https://emre.me/coding-patterns/top-k-numbers/

# How to identify?
# If the problem asking us to find the top / smallest / frequent K elements 
# among a given set, we need to think about Top K Numbers pattern.

# While solving the problems, we are going to use 
# Heap data structure to keep track of K elements.


# Problem: K-th Largest Element
# LeetCode 215 - Kth Largest Element in an Array [medium]

# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Example 1:

# Input: [3, 2, 1, 5, 6, 4] and k = 2
# Output: 5
# Example 2:

# Input: [3, 2, 3, 1, 2, 4, 5, 5, 6] and k = 4
# Output: 4
# Note:

# You may assume k is always valid, 1 ≤ k ≤ array’s length.

from heapq import heappop, heappush

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []
        for i in range(k):
            heappush(min_heap, nums[i])
        print(min_heap)
        for i in range(k, len(nums)):
            print(i)
            if nums[i] > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, nums[i])
        print(min_heap)
        return min_heap[0]

# Input: [3, 2, 3, 1, 2, 4, 5, 5, 6] and k = 4
# Output: 4

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
s = Solution().findKthLargest(nums, k)
print(s)

# Time Complexity: O(N log K).

# Space Complexity: O(K)
