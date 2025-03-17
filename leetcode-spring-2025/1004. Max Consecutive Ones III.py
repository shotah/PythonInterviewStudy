class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left, right = 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        # convert index diff to length diff.
        return right - left + 1


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    expected = 6
    actual = Solution().longestOnes(nums, k)
    assert actual == expected, f"Test Case Failed: Input: {nums}, Expected: {expected}, Actual: {actual}"
