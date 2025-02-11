from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return [i for i, n in enumerate(nums) if n == target]


# For testing
assert Solution().targetIndices([1, 2, 3, 4, 5], 3) == [2]
assert Solution().targetIndices([1, 2, 3, 4, 5], 6) == []
assert Solution().targetIndices([1, 2, 3, 4, 5], 5) == [4]

print("PASSED")
