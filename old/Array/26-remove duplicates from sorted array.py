from typing import List

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i in reversed(range(1,len(nums))):
            if nums[i] == nums[i-1]:
                nums.pop(i)
        return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
print(s.removeDuplicates(nums))

