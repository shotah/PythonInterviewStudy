from typing import List


# class Solution:
#     def getAverages(self, nums: List[int], k: int) -> List[int]:
#         averages = [-1] * len(nums)
#         if k == 0:
#             return nums

#         window_size = 2 * k + 1
#         n = len(nums)

#         if window_size > n:
#             return averages

#         window_sum = sum(nums[:window_size])
#         averages[k] = window_sum // window_size

#         for i in range(window_size, n):
#             window_sum = window_sum - nums[i - window_size] + nums[i]
#             averages[i - k] = window_sum // window_size

#         return averages


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        res = [-1] * len(nums)
        sum_len = 2 * k + 1
        if len(nums) < sum_len:
            return res
        rolling_sum = sum(nums[:sum_len])
        res[k] = int(rolling_sum / sum_len)
        for i in range(k + 1, len(nums) - k):
            rolling_sum = rolling_sum - nums[i - k - 1] + nums[i + k]
            res[i] = int(rolling_sum / sum_len)
        return res


print("Test 1")
s = Solution()
r = s.getAverages([1, 2, 3, 4, 5], 2)
print(r)  # [-1, -1, 3, -1, -1]

print("Test 2")
r = s.getAverages([10000], 0)
print(r)  # [-10000]

print("Test 3")
r = s.getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3)
print(r)  # [-1,-1,-1,5,4,4,-1,-1,-1]
