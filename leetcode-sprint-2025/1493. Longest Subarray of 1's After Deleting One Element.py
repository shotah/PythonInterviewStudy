class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        k = 1
        left, right = 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case
    nums = [1, 1, 0, 1]
    expected = 3
    actual = Solution().longestSubarray(nums)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {nums}, Expected: {expected}, Actual: {actual}"

    # Test Case
    nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    expected = 5
    actual = Solution().longestSubarray(nums)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {nums}, Expected: {expected}, Actual: {actual}"
