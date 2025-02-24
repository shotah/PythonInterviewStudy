# Bad solution as it assumes the indexes will be in a row
# class Solution:
#     def increasingTriplet(self, nums: list[int]) -> bool:
#         start_index = 2
#         for i in range(start_index, len(nums)):
#             if nums[i - 2] <= nums[i - 1] <= nums[i]:
#                 return True
#         return False


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        f = float("inf")
        s = float("inf")
        for n in nums:
            if n <= f:
                f = n
            elif n <= s:
                s = n
            else:
                return True
        return False


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case 1
    nums = [1, 2, 3, 4, 5]
    expected = True
    actual = Solution().increasingTriplet(nums)
    assert (
        actual == expected
    ), f"Test Case 1 Failed: Input: {nums}, Expected: {expected}, Actual: {actual}"

    # Test Case 2
    nums = [5, 4, 3, 2, 1]
    expected = False
    actual = Solution().increasingTriplet(nums)
    assert (
        actual == expected
    ), f"Test Case 2 Failed: Input: {nums}, Expected: {expected}, Actual: {actual}"

    # Add more test cases here in the same format
    # Test Case 3 (Example)
    nums = [2, 1, 5, 0, 4, 6]
    expected = True
    actual = Solution().increasingTriplet(nums)
    assert (
        actual == expected
    ), f"Test Case 3 Failed: Input: {nums}, Expected: {expected}, Actual: {actual}"

    # Add more test cases here in the same format
    # Test Case (Example)
    nums = [20, 100, 10, 12, 5, 13]
    expected = True
    actual = Solution().increasingTriplet(nums)
    assert (
        actual == expected
    ), f"Test Case 4 Failed: Input: {nums}, Expected: {expected}, Actual: {actual}"

    print("\nInline tests finished.")
