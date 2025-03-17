# class Solution:
#     def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
#         l_diff = []
#         r_diff = []
#         s_1 = set(nums1)
#         s_2 = set(nums2)
#         for n in s_1:
#             if n not in s_2:
#                 l_diff.append(n)
#         for n in s_2:
#             if n not in s_1:
#                 r_diff.append(n)
#         return [l_diff, r_diff]


class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        return [list(s1 - s2), list(s2 - s1)]


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    expected = [[1, 3], [4, 6]]
    actual = Solution().findDifference(nums1, nums2)
    assert actual == expected, f"Test Case Failed: Input: {nums1}, Expected: {expected}, Actual: {actual}"

    # Test Case
    nums1 = [1, 2, 3, 3]
    nums2 = [1, 1, 2, 2]
    expected = [[3], []]
    actual = Solution().findDifference(nums1, nums2)
    assert actual == expected, f"Test Case Failed: Input: {nums1}, Expected: {expected}, Actual: {actual}"
