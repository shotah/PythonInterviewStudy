# class Solution:
#     def maxOperations(self, nums: list[int], k: int) -> int:
#         result = 0
#         for i in range(len(nums) - 1):
#             print(i)
#             a = nums.pop(i)
#             diff_index = nums.index(k - a)
#             if diff_index:
#                 nums.pop(diff_index)
#                 result += 1
#             else:
#                 nums.insert(i, a)
#         return result


# class Solution:
#     def maxOperations(self, nums: list[int], k: int) -> int:
#         visited = []
#         pairs = 0
#         for i, n in enumerate(nums):
#             looking_for = k - n
#             if looking_for in visited:
#                 pairs += 1
#                 visited.remove(looking_for)
#             else:
#                 visited.append(n)
#         return pairs


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        pairs = 0
        for n in counts.keys():
            looking_for = k - n
            if looking_for in counts and counts[looking_for] > 0:
                if looking_for == n:
                    pairs += counts[n] // 2  # just do the main and insert the pairs
                    counts[n] %= 2  # set it as the remainder
                elif looking_for > n:  # Process pairs only when n < looking_for
                    valid_pairs = min(counts[n], counts[looking_for])
                    pairs += valid_pairs
                    counts[n] -= valid_pairs
                    counts[looking_for] -= valid_pairs
        return pairs


if __name__ == "__main__":
    print("Running inline tests:")

    # Original Test Cases (keep these)
    # Test Case 1
    nums = [1, 2, 3, 4]
    k = 5
    expected = 2
    actual = Solution().maxOperations(nums, k)
    assert actual == expected, f"Test Case 1 Failed: Input: {nums}, Expected: {expected}, Actual: {actual}"

    # Test Case 2
    nums = [3, 1, 3, 4, 3]
    k = 6
    expected = 1
    actual = Solution().maxOperations(nums, k)
    assert actual == expected, f"Test Case 2 Failed: Input: {nums}, Expected: {expected}, Actual: {actual}"

    # Test Case 3
    nums = [3, 5, 1, 5]
    k = 2
    expected = 0
    actual = Solution().maxOperations(nums, k)
    assert actual == expected, f"Test Case 3 Failed: Input: {nums}, Expected: {expected}, Actual: {actual}"

    # --- New Test Cases ---

    # Test Case 4: Pairs of the same number (even k)
    nums = [2, 2, 2, 2]
    k = 4
    expected = 2  # Two pairs of (2, 2)
    actual = Solution().maxOperations(nums, k)
    assert actual == expected, f"Test Case 4 Failed: Input: {nums}, Expected: {expected}, Actual: {actual}"

    # Test Case 5: Mixed numbers, multiple possible pairs, to check for double counting issues
    nums = [1, 2, 3, 4, 1, 2, 3, 4]
    k = 5
    expected = 4  # Two (1, 4) pairs and two (2, 3) pairs
    actual = Solution().maxOperations(nums, k)
    assert actual == expected, f"Test Case 5 Failed: Input: {nums}, Expected: {expected}, Actual: {actual}"

    # Test Case 6: No pairs possible
    nums = [1, 1, 1, 1]
    k = 10
    expected = 0
    actual = Solution().maxOperations(nums, k)
    assert actual == expected, f"Test Case 6 Failed: Input: {nums}, Expected: {expected}, Actual: {actual}"

    # Test Case 7: One number with count > 2, to check count handling
    nums = [1, 2, 2, 2, 3, 3]
    k = 4
    expected = 2  # One (2, 2) pair, one (1, 3) pair
    actual = Solution().maxOperations(nums, k)
    assert actual == expected, f"Test Case 7 Failed: Input: {nums}, Expected: {expected}, Actual: {actual}"

    print("\nInline tests finished.")
