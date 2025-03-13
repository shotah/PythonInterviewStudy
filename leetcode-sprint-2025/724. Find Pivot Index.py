# class Solution:
#     def pivotIndex(self, nums: list[int]) -> int:
#         left_sum = 0
#         right_sum = sum(nums)
#         for idx in range(len(nums)):
#             right_sum -= nums[idx]
#             if left_sum == right_sum:
#                 return idx
#             left_sum += nums[idx]
#         return -1


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for i, n in enumerate(nums):
            right_sum -= n
            if left_sum == right_sum:
                return i
            left_sum += n
        return -1


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case
    nums = [1, 7, 3, 6, 5, 6]
    expected = 3
    actual = Solution().pivotIndex(nums)
    assert actual == expected, f"Test Case Failed: Input: {nums}, Expected: {expected}, Actual: {actual}"

    # Test Case
    nums = [1, 2, 3]
    expected = -1
    actual = Solution().pivotIndex(nums)
    assert actual == expected, f"Test Case Failed: Input: {nums}, Expected: {expected}, Actual: {actual}"

    # Test Case
    nums = [2, 1, -1]
    expected = 0
    actual = Solution().pivotIndex(nums)
    assert actual == expected, f"Test Case Failed: Input: {nums}, Expected: {expected}, Actual: {actual}"
