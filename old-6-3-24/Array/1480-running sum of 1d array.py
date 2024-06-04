from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sums = []
        for num in nums:
          if len(running_sums):
            running_sums.append(running_sums[-1] + num)
          else:
            running_sums.append(num)
        return running_sums

nums = [1,2,3,4]
s = Solution()
print(s.runningSum(nums))

