class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        values = {}
        for idx, num in enumerate(numbers):
            val = target - num
            if val in values:
                return [values[val], idx + 1]
            values[num] = idx + 1


numbers = [2,7,11,15]
target = 9
# [1, 2]
numbers = [2,3,4]
target = 6

s = Solution().twoSum(numbers, target)
print(s)
