# class Solution:
#     def uniqueOccurrences(self, arr: list[int]) -> bool:
#         result = {}
#         for num in arr:
#             result[num] = result.get(num, 0) + 1
#         test_arr = []
#         for val in result.values():
#             if val in test_arr:
#                 return False
#             test_arr.append(val)
#         return True


import collections


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counts = collections.Counter(arr)
        return len(set(counts.values())) == len(counts.values())


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case
    arr = [1, 2, 2, 1, 1, 3]
    expected = True
    actual = Solution().uniqueOccurrences(arr)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {arr}, Expected: {expected}, Actual: {actual}"

    # Test Case
    arr = [1, 2]
    expected = False
    actual = Solution().uniqueOccurrences(arr)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {arr}, Expected: {expected}, Actual: {actual}"
