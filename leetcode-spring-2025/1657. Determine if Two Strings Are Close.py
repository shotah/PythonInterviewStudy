import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        w1_counts = collections.Counter(word1)
        w2_counts = collections.Counter(word2)

        # Same character set check
        if set(w1_counts.keys()) != set(w2_counts.keys()):
            return False

        # Same sorted counts check
        if sorted(w1_counts.values()) != sorted(w2_counts.values()):
            return False

        return True


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case
    word1 = "abc"
    word2 = "bca"
    expected = True
    actual = Solution().closeStrings(word1, word2)
    assert actual == expected, f"Test Case Failed: Input: {word1}, Expected: {expected}, Actual: {actual}"

    # Test Case
    word1 = "a"
    word2 = "aa"
    expected = False
    actual = Solution().closeStrings(word1, word2)
    assert actual == expected, f"Test Case Failed: Input: {word1}, Expected: {expected}, Actual: {actual}"

    # Test Case
    word1 = "cabbba"
    word2 = "abbccc"
    expected = True
    actual = Solution().closeStrings(word1, word2)
    assert actual == expected, f"Test Case Failed: Input: {word1}, Expected: {expected}, Actual: {actual}"
