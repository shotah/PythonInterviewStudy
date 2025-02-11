class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = set()
        duplicates = []
        values = {}
        # starts main look to evaluate:
        for idx, val1 in enumerate(nums):
            if val1 not in duplicates:
                duplicates.append(val1)
                # loops through remaining list:
                for val2 in nums[idx+1:]:
                    complement = - val1 - val2
                    if complement in values and values[complement] == idx:
                        results.add(tuple(sorted((val1, val2, complement))))
                    values[val2] = idx
        return results

numbers = [-1,0,1,2,-1,-4]
# [[-1,-1,2],[-1,0,1]]
s = Solution().threeSum(numbers)
print(s)
