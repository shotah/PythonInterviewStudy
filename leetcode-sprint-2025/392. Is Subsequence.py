class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        list_of_s = list(s)
        list_of_t = list(t)
        c = 0
        for l in list_of_s:
            if l in list_of_t:
                c += 1
            if c >= len(list_of_s):
                return True
        return False


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
