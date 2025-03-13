# class Solution:
#     def maxVowels(self, s: str, k: int) -> int:
#         lib = {"a", "e", "i", "o", "u"}
#         max_vowel = 0
#         curr_vowel = 0
#         # gets all vowels in the first k characters
#         for i in range(k):
#             if s[i] in lib:
#                 curr_vowel += 1
#         max_vowel = curr_vowel
#         # starts sliding window from k to the end of the string
#         for i in range(k, len(s)):
#             if s[i - k] in lib:
#                 curr_vowel -= 1
#             if s[i] in lib:
#                 curr_vowel += 1
#             max_vowel = max(curr_vowel, max_vowel)
#             # Early return if curr_vowel is already k
#             if max_vowel == k:
#                 return k
#         return max_vowel


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        curr_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                curr_vowels += 1
        max_vowels = curr_vowels
        for i in range(k, len(s)):
            # check if the letter we are dropping is a vowel and subtract
            if s[i - k] in vowels:
                curr_vowels -= 1
            # check if the letter we are adding is a vowel
            if s[i] in vowels:
                curr_vowels += 1
            max_vowels = max(max_vowels, curr_vowels)
            if max_vowels == k:
                return k
        return max_vowels


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case
    s = "abciiidef"
    k = 3
    expected = 3
    actual = Solution().maxVowels(s, k)
    assert actual == expected, f"Test Case Failed: Input: {s}, Expected: {expected}, Actual: {actual}"

    # Test Case
    s = "aeiou"
    k = 2
    expected = 2
    actual = Solution().maxVowels(s, k)
    assert actual == expected, f"Test Case Failed: Input: {s}, Expected: {expected}, Actual: {actual}"

    # Test Case
    s = "leetcode"
    k = 3
    expected = 2
    actual = Solution().maxVowels(s, k)
    assert actual == expected, f"Test Case Failed: Input: {s}, Expected: {expected}, Actual: {actual}"

    # Test Case
    s = "weallloveyou"
    k = 7
    expected = 4
    actual = Solution().maxVowels(s, k)
    assert actual == expected, f"Test Case Failed: Input: {s}, Expected: {expected}, Actual: {actual}"
