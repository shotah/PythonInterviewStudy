class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        checked_nums = {}
        for idx, num in enumerate(nums):
            test_target = target - num
            if test_target in checked_nums:
                return [checked_nums[test_target], idx]
            else:
                checked_nums[num] = idx


