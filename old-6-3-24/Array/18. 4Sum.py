class Solution:
    def fourSum(self, nums, target):
        result = []
        nums_len = len(nums)
        # Guard clause to exit if there isn't enough numbers to complete the task
        if nums_len <= 3:
            return result
        nums.sort()
        a_idx = 0
        # Loops for index A to start moving Right
        while a_idx < nums_len:
            # Increment and skip if greater than 0 and is the same as the last entry. 
            if a_idx > 0 and nums[a_idx] == nums[a_idx - 1]:
                a_idx += 1
                continue
            b_idx = a_idx + 1
            # Loops for index B to start moving Right
            while b_idx < nums_len:
                # Increment and skip if greater than A index + 1 and is the same as the last entry. 
                if b_idx > a_idx + 1 and nums[b_idx] == nums[b_idx - 1]:
                    b_idx += 1
                    continue
                c_idx = b_idx + 1
                d_idx = nums_len - 1
                while c_idx < d_idx:
                    # Increment and skip if greater than B index + 1 and is the same as the last entry. 
                    if c_idx > b_idx + 1 and nums[c_idx] == nums[c_idx - 1]:
                        c_idx += 1
                        continue
                    # Decrement and skip if smaller than length -1 and is the same as the last entry. 
                    if d_idx < nums_len - 1 and nums[d_idx] == nums[d_idx + 1]:
                        d_idx -= 1
                        continue
                    cur_sum = nums[a_idx] + nums[b_idx] + nums[c_idx] + nums[d_idx]
                    # Found a working set:
                    if cur_sum == target:
                        result.append([nums[a_idx], nums[b_idx], nums[c_idx], nums[d_idx]])
                        c_idx += 1
                    # Not a working set, sum is less than target move c index right
                    elif cur_sum < target:
                        c_idx += 1
                    # Not a working set, sum is greater than target move d index left
                    else:
                        d_idx -= 1
                # Move b index Right
                b_idx += 1
            # Move a index Right
            a_idx += 1
        return result


nums = [1, 0, -1, 0, -2, 2]
target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# nums = [2,2,2,2,2]
# target = 8
# Output: [[2,2,2,2]]
print(nums)
s = Solution().fourSum(nums, target)
print(s)
