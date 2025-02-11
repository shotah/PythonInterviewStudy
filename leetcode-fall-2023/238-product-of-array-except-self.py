from typing import List

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         length=len(nums)
#         sol=[1]*length
#         pre = 1
#         post = 1
#         for i in range(length):
#             sol[i] *= pre
#             pre = pre*nums[i]
#             sol[length-i-1] *= post
#             post = post*nums[length-i-1]
#         return(sol)


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         output = []
#         already_multiplied = []

#         for i in range(len(nums)):
#             current = nums.pop(0)
#             result = 1
#             for num in nums:
#                 result *= num
#             for num in already_multiplied:
#                 result *= num
#             output.append(result)
#             already_multiplied.append(current)
#         return output

# WINNER! for speed and memory
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         result = 1
#         output = []
#         # create list of products of all elements to the left of each element
#         for num in nums:
#             output.append(result)
#             result *= num
#         result = 1
#         # Start at top and walk backwards, for each element in output entry
#         # multiply by the product of all elements to the right of each element
#         for i in range(len(nums) - 1, -1, -1):
#             output[i] *= result
#             result *= nums[i]
#         return output


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans: list[int] = [1] * len(nums)
        pre = 1
        post = 1
        for i in range(len(nums)):
            ans[i] *= pre
            ans[-1 - i] *= post
            pre *= nums[i]
            post *= nums[-1 - i]
        return ans


nums = [1, 2, 3, 4]
expected = [24, 12, 8, 6]

print("Actual:  ", Solution().productExceptSelf(nums))
print("Expected:", expected)
