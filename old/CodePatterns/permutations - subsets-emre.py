# https://emre.me/coding-patterns/subsets/

# How to identify?

# If the problem description involves dealing with Permutations 
# and Combinations of a given set of elements or subsets, 
# you should think about Subsets pattern which is very 
# useful to solve these kinds of problems.

# This pattern describes an efficient Breadth First Search (BFS) 
# approach to handle all these problems.


# LeetCode 78 - Subsets [medium]

# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1, 2, 3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1, 2, 3],
#   [1, 3],
#   [2, 3],
#   [1, 2],
#   []
# ]

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        # loop for nums to insert first nums:
        for num in nums:
            # To get all additional variations loop through potential subsets:
            for i in range(len(subsets)):
                # merge arrays, even if subset array does not exist:
                val = subsets[i] + [num]
                # append to results:
                subsets.append(val)
        # return results
        return subsets

nums = [1,2,3]
s = Solution().subsets(nums)
print(s)
# Time Complexity: O(2N) since, in each step, number of subsets doubles.

# Space Complexity: O(2N)
