# https://emre.me/coding-patterns/knapsack/


# How to identify?
# 0/1 Knapsack pattern is very useful to solve the famous Knapsack problem 
# by using Dynamic Programming techniques.

# Knapsack problem is all about optimization. 
# For example, given a set of items, each with a weight and a value, 
# determine the number of each item to include in a collection so that the 
# total weight is less than or equal to a given limit and the total value 
# is as large as possible.

# We are using top-down Memoisation or bottom-up Tabulation technique 
# to solve these problems efficiently.


# Note:

# Each of the array element will not exceed 100. The array size will not exceed 200.

# Example 1:

# Input: [1, 5, 11, 5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: [1, 2, 3, 5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

# Brute Force Solution
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        
        if s % 2 != 0:
            return False
        
        return self.can_partition_recursive(nums, s/2, 0)
    
    def can_partition_recursive(self, nums, sum, current_index):
        if sum == 0:
            return True
        
        if len(nums) == 0 or current_index >= len(nums):
            return False
        
        if nums[current_index] <= sum:
            if (self.can_partition_recursive(nums, sum - nums[current_index], current_index + 1)):
                return True
        
        return self.can_partition_recursive(nums, sum, current_index + 1)
# Time Complexity: O(2N) where N represents the total number.

# Space Complexity: O(N) which will be used to store recursion stack
    
# Top-down Dynamic Programming with Memoization
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        
        if s % 2 != 0:
            return False
        
        # initialize two-dimensional dp array, -1 for default
        dp = [[-1 for x in range(int(s/2)+1)] for y in range(len(nums))]
        
        if self.can_partition_recursive(dp, nums, int(s / 2), 0) == 1:
            return True  # return True for 1
        else:
            return False  # return False for 0
        
    def can_partition_recursive(self, dp, nums, sum, current_index):
        if sum == 0:
            return 1
        
        if len(nums) == 0 or current_index >= len(nums):
            return 0
        
        if dp[current_index][sum] == -1:  # if we have not processed this sub-problem
                if nums[current_index] <= sum:
                    if self.can_partition_recursive(dp, nums, sum - nums[current_index], current_index + 1) == 1:
                        dp[current_index][sum] = 1
                        return 1

                # recursive call after excluding the number at the current_index
                dp[current_index][sum] = self.can_partition_recursive(dp, nums, sum, current_index + 1)

        return dp[current_index][sum]
# Time Complexity: O(N * S) where N represents the total numbers and S is the total sum of all numbers.

# Space Complexity: O(N * S)

# Bottom-up Dynamic Programming with Tabulation
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        s = sum(nums)
        
        if s % 2 != 0:
            return False
        
        s = int(s / 2)
        dp = [[False for x in range(s + 1)] for y in range(len(nums))]
        
        # populate s = 0 columns
        for i in range(0, len(nums)):
            dp[i][0] = True
            
        # form a subset only when the required sum is equal to its value
        for j in range(1, s + 1):
            dp[0][j] = nums[0] == j
        
        # process all subsets for all sums
        for i in range(1, len(nums)):
            for j in range(1, s + 1):
                # if we can get the sum 'j' without the number at index 'i'
                if dp[i - 1][j]:
                    dp[i][j] = dp[i - 1][j]
                    
                # else if we can find a subset to get the remaining sum
                elif j >= nums[i]:
                    dp[i][j] = dp[i - 1][j - nums[i]]
        
        # the bottom-right corner will have our answer
        return dp[len(nums) - 1][s]
# Time Complexity: O(N * S) where N represents the total numbers and S is the total sum of all numbers.

# Space Complexity: O(N * S)
