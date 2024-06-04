# https://emre.me/coding-patterns/modified-binary-search/

# How to identify?

# This approach is quite useful to solve the problems whenever 
# we are given a sorted Array or Linked List or Matrix, 
# and we are asked to find a certain element.

# This pattern describes an efficient way to handle all 
# problems involving Binary Search.


# LeetCode 704 - Binary Search [easy]

# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.

# Example 1:

# Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
# Note:

# You may assume that all elements in nums are unique.
# n will be in the range [1, 10000].
# The value of each element in nums will be in the range [-9999, 9999].


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

# Time Complexity: O(log N) where N is the total elements in the given array.

# Space Complexity: O(1)
