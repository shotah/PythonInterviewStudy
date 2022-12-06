# https://emre.me/coding-patterns/sliding-window/

# How to identify?

# So we want to be able to identify the problems that sliding window pattern works.

# The problem involves a data structure that is ordered and 
# iterable like arrays, strings, etc.

# The problem is asking to find a subrange in an array/string, 
# contiguous longest, shortest, average or target value.
# There is an apparent naive or brute force solution that 
# runs in O(N2), O(2N) or some other large time complexity.

# The amazing thing about sliding window problems is that most 
# of the time they can be solved in O(N) time and O(1) space complexity.


# Example:

# Input: [1, 12, -5, -6, 50, 3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# Brute Force Solution
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average = 0.0

        for i in range(len(nums) - k + 1):
            _sum = 0.0  # find sum of next k elements

            for j in range(i, i + k):
                _sum += nums[j]

            average = _sum / k  # calculate the average of selected k elements
            max_average = max(max_average, average)  # update max_average

            if len(nums) == 1:  # if there is only 1 element in nums
                return average

        return max_average

# Sliding Window Solution
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        average = []
        _sum, start = 0, 0
        for end in range(len(nums)):
            _sum += nums[end]  # add the next element

            if end >= k - 1:
                average.append(_sum / k)  # calculate the average
                _sum -= nums[start]  # subtract the element going out
                start += 1  # slide the window

        return max(average)
