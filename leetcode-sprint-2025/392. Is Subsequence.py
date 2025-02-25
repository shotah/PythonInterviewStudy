# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         if s == "":
#             return True
#         list_of_s = list(s)
#         list_of_t = list(t)
#         c = 0
#         for l in list_of_s:
#             if l in list_of_t:
#                 c += 1
#             if c >= len(list_of_s):
#                 return True
#         return False


# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         if not s:
#             return True
#         index_of_s = 0
#         for char_t in t:
#             if char_t == s[index_of_s]:
#                 index_of_s += 1
#             if index_of_s == len(s):
#                 return True
#         return False


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        i = 0
        for j in range(n):
            if i == m:
                return True
            if s[i] == t[j]:
                i += 1
        return i == mhuh


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case
    s = "abc"
    t = "ahbgdc"
    expected = True
    actual = Solution().isSubsequence(s, t)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {s}, Expected: {expected}, Actual: {actual}"

    # Test Case
    s = "acb"
    t = "ahbgdc"
    expected = False
    actual = Solution().isSubsequence(s, t)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {s}, Expected: {expected}, Actual: {actual}"

    print("\nInline tests finished.")
