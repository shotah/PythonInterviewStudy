class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        if k == 1:
            return max(nums)
        prefix_sum = sum(nums[0:k])
        results = [prefix_sum / k]
        for i in range(k, len(nums)):
            prefix_sum += nums[i] - nums[i - k]
            results.append(prefix_sum / k)
        return max(results)


if __name__ == "__main__":
    print("Running inline tests:")

    # Original Test Cases (keep these)
    # Test Case 1
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    expected = 12.75000
    actual = Solution().findMaxAverage(nums, k)
    assert actual == expected, f"Test Case 1 Failed: Input: {nums}, Expected: {expected}, Actual: {actual}"

    # Test Case 1
    nums = [5]
    k = 1
    expected = 5.0
    actual = Solution().findMaxAverage(nums, k)
    assert actual == expected, f"Test Case 1 Failed: Input: {nums}, Expected: {expected}, Actual: {actual}"

    # Test Case 1
    nums = [0, 1, 1, 3, 3]
    k = 4
    expected = 2.0
    actual = Solution().findMaxAverage(nums, k)
    assert actual == expected, f"Test Case 1 Failed: Input: {nums}, Expected: {expected}, Actual: {actual}"
