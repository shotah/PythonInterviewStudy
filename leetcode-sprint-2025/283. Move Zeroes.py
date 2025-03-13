# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         tracker = []
#         for i, n in enumerate(nums):
#             if n == 0:
#                 tracker.append(i)
#         for i, n in enumerate(tracker):
#             nums.pop(n - i)
#             nums.append(0)


class Solution:
    def moveZeroes(self, nums: list) -> None:
        anchor = 0
        for explorer in range(len(nums)):
            if nums[explorer] != 0:
                nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
                anchor += 1


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case
    nums = [0, 1, 0, 3, 12]
    expected = [1, 3, 12, 0, 0]
    Solution().moveZeroes(nums)
    assert nums == expected, f"Test Case Failed: Input: {nums}, Expected: {expected}, Actual: {nums}"

    # Test Case
    nums = [0, 0, 1]
    expected = [1, 0, 0]
    Solution().moveZeroes(nums)
    assert nums == expected, f"Test Case Failed: Input: {nums}, Expected: {expected}, Actual: {nums}"

    print("\nInline tests finished.")
