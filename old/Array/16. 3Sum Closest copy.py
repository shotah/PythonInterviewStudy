class Solution:
  def threeSumClosest(self, nums, target):
    if len(nums) < 3: return
    nums.sort()
    result = nums[0] + nums[1] + nums[2]
    for idx in range(len(nums) - 2):
        left = idx + 1
        right = len(nums) - 1
        while left < right:
            cur_sum = nums[idx] + nums[left] + nums[right]
            if cur_sum == target:
                return cur_sum
            if abs(cur_sum - target) < abs(result - target):
                result = cur_sum
            if cur_sum < target:
                left += 1
            elif cur_sum > target:
                right -= 1
    return result

nums = [-1,2,1,-4]
target = 1
# 2
# nums = [0,0,0]
# target = 1
# 0
# nums = [0,1,2]
# target = 0
# 3
nums = [1,1,1,1]
target = 0
# 3
nums = [1,1,1,1]
target = -100
# 3
nums = [1,1,1,0]
target = -100
# 2
# nums = [4,0,5,-5,3,3,0,-4,-5]
# target = -2
# # -2


nums = [-13,592,-501,770,-952,-675,322,-829,-246,657,608,485,-112,967,-30,182,-969,559,-286,-64,24,365,-158,701,535,-429,-217,28,948,-114,-536,-711,693,23,-958,-283,-700,-672,311,314,-712,-594,-351,658,747,949,70,888,166,495,244,-380,-654,454,-281,-811,-168,-839,-106,877,-216,523,-234,-8,289,-175,920,-237,-791,-976,-509,-4,-3,298,-190,194,-328,265,150,210,285,-176,-646,-465,-97,-107,668,892,612,-54,-272,-910,557,-212,-930,-198,38,-365,-729,-410,932,4,-565,-329,-456,224,443,-529,-428,-294,191,229,112,-867,-163,-979,236,-227,-388,-209,984,188,-549,970,951,-119,-146,801,-554,564,-769,334,-819,-356,-724,-219,527,-405,-27,-759,722,-774,758,394,146,517,870,-208,742,-782,336,-364,-558,-417,663,-914,536,293,-818,847,-322,408,876,-823,827,167]
target = 7175
# 2921

s = Solution().threeSumClosest(nums, target)
print(s)

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
