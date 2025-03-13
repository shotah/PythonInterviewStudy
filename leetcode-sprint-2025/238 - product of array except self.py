# 238. Product of Array Except Self
# Hint
# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.


# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
# import math


# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         result = []
#         for i, num in enumerate(nums):
#             l = nums.copy()
#             l.pop(i)
#             result.append(math.prod(l))
#         return result


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = 1
        output = []
        # create list of products of all elements to the left of each element
        for num in nums:
            output.append(result)
            result *= num
        result = 1
        # Start at top and walk backwards, for each element in output entry
        # multiply by the product of all elements to the right of each element
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= result
            result *= nums[i]
        return output


# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

nums = [-1, 1, 0, -3, 3]
expected = [0, 0, 9, 0, 0]
print("Actual:  ", Solution().productExceptSelf(nums))
print("Expected:", expected)
