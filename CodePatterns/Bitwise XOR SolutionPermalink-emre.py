# https://emre.me/coding-patterns/bitwise-xor/


# How to identify?

# Knowing XOR properties well opens some surprising doors in 
# your problem solving skills. To be able to identify 
# XOR related problems are mostly coming from previous 
# experiences. But if you need to eliminate the same 
# numbers from an integer array, using Bit Manipulation 
# Tricks is extremely helpful.


# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2, 2, 1]
# Output: 1
# Example 2:

# Input: [4, 1, 2, 1, 2]
# Output: 4

# Bitwise XOR Solution
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = 0
        for i in nums:
            num ^= i
        return num
    
# Problem: Single Number III
# Example:

# Input:  [1, 2, 1, 3, 2, 5]
# Output: [3, 5]
# Note:

# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

# Bitwise XOR Solution
class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        # XOR of all numbers in the given list
        n1xn2 = 0
        for num in nums:
            n1xn2 ^= num
        # rightmost bit which is 1
        rightmost_bit = 1
        while rightmost_bit & n1xn2 == 0:
            rightmost_bit = rightmost_bit << 1
        num1, num2 = 0, 0
        for num in nums:
            if num & rightmost_bit != 0:  # the bit is set
                num1 ^= num
            else:  # the bit is not set
                num2 ^= num
        return [num1, num2]

# Time Complexity: O(N) where N is the total number of elements in the input array.

# Space Complexity: O(1)
