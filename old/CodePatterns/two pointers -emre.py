# https://emre.me/coding-patterns/two-pointers/

# How to identify?

# So we want to be able to identify the problems that Two Pointers pattern works.

# The problem involve sorted arrays (or Linked Lists), a set of pair elements, 
# or a triplet or even a subarray.
# There is a target value to match or 
# duplicates to be removed.

# Most of these type of problems can be solved in O(N) time complexity 
# and O(1) or O(N) space complexity.


# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# Two Pointers Solution
def twoSum(self, nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        if target > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum
    return [-1, -1]
  
# Time Complexity: O(N) where N is the number of elements in the input array (nums).
# Space Complexity: O(1), algorithm runs in constant space.

# An Alternative Solution
def twoSum(self, nums: List[int], target: int) -> List[int]:
    num_map = {}  # to store numbers and their indices
    for i, num in enumerate(nums):
        if target - num in num_map:
            return [num_map[target - num], i]
        else:
            num_map[nums[i]] = i
    return [-1, -1]
# Time Complexity: O(N) where N is the number of elements in the input array (nums).
# Space Complexity: O(N), in the worst case, we will be pushing N numbers to HashMap.
