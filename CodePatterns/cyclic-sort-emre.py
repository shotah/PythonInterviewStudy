# https://emre.me/coding-patterns/cyclic-sort/


# How to identify?

# This approach is quite useful when dealing with numbers 
# in a given range and asking to find the duplicates/missing ones etc.

# When the problem involving arrays containing numbers in a 
# given range, you should think about Cyclic Sort pattern.


# Example 1:

# Input: [3, 0, 1]
# Output: 2
# Example 2:

# Input: [9, 6, 4, 2, 3, 5, 7, 0, 1]
# Output: 8

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        start = 0
        while start < len(nums):
            num = nums[start]
            if num < len(nums) and num != start:
                nums[start], nums[num] = nums[num], nums[start]
            else:
                start += 1
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

nums = [5,1,3,4,0]
s = Solution().missingNumber(nums)
print(s)

# Time Complexity: O(N) + O(N - 1) which is asymptotically equivalent to O(N)

# Space Complexity: O(1), algorithm runs in constant space.
