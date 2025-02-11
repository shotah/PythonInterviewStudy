import json

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        results = set()
        duplicates1 = []
        duplicates2 = []
        values = {}
        for idx1, val1 in enumerate(nums):
            if val1 not in duplicates1:
                duplicates1.append(val1)
                for idx2, val2 in enumerate(nums[idx1+1:]):
                    if val2 not in duplicates2:
                        duplicates2.append(val2)
                        for idx3, val3 in enumerate(nums[idx2+1:]):
                            complement = (- val1 - val2 - val3 + target)
                            if complement in values:
                                results.add(tuple(sorted((val1, val2, val3, complement))))
                            values[val3] = idx3
                        values[val2] = idx2
                        duplicates2 = []
        return results


nums = [1,0,-1,0,-2,2]
target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# nums = [2,2,2,2,2]
# target = 8
# Output: [[2,2,2,2]]
print(nums)
s = Solution().fourSum(nums, target)
print(
    s
)
