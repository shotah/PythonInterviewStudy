import json

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        if len(nums) < 4: return []
        results = set()
        values = {}
        nums.sort()
        counter = 0
        result = nums[0] + nums[1] + nums[2]
        for idx in range(len(nums) - 2):
            a_pointer = idx + 1
            b_pointer = len(nums) - 1
            print(f"pointers: {a_pointer}, {b_pointer}")
            while a_pointer < b_pointer and counter < len(nums)-1:
                counter += 1
                cur_sum = nums[idx] + nums[a_pointer] + nums[b_pointer]
                print(f"sum: {cur_sum} = {nums[idx]} + {nums[a_pointer]} + {nums[b_pointer]}")
                diff = -target -cur_sum
                print(f"diff: {diff} = -{target} -{cur_sum}")
                if diff in values:
                    results.add(tuple(sorted((nums[idx], nums[a_pointer], nums[b_pointer], diff))))
                if abs(cur_sum - target) < abs(result - target):
                    result = cur_sum
                values[nums[a_pointer]] = a_pointer
                values[nums[b_pointer]] = b_pointer
                if cur_sum < target:
                    a_pointer += 1
                elif cur_sum > target:
                    b_pointer -= 1
                print(json.dumps(values))
        return results


nums = [1,0,-1,0,-2,2]
target = 0
print(nums)
s = Solution().fourSum(nums, target)
print(
    s
)
