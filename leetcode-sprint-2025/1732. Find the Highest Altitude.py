# class Solution:
#     def largestAltitude(self, gain: list[int]) -> int:
#         max_elevation = 0
#         rolling_sum = 0
#         for n in gain:
#             rolling_sum += n
#             max_elevation = max(max_elevation, rolling_sum)
#         return max_elevation

import itertools


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        return max(list(itertools.accumulate([0] + gain)))


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case
    gain = [-5, 1, 5, 0, -7]
    expected = 1
    actual = Solution().largestAltitude(gain)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {gain}, Expected: {expected}, Actual: {actual}"

    # Test Case
    gain = [-4, -3, -2, -1, 4, 3, 2]
    expected = 0
    actual = Solution().largestAltitude(gain)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {gain}, Expected: {expected}, Actual: {actual}"
