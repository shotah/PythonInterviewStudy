# class Solution:
#     def maxVowels(self, s: str, k: int) -> int:
#         if k > len(s):
#             return 0
#         vowels = {"a", "e", "i", "o", "u"}
#         trackerList = []
#         output = 0
#         # use sliding window
#         # range minus k plus 1 because we need to include the last character

#         for i in range(len(s)):
#             if s[i] in vowels:
#                 trackerList.append(1)
#             else:
#                 trackerList.append(0)
#             if i >= k:
#                 trackerList[i - k] = 0
#             output = max(output, sum(trackerList))
#             if output >= k:
#                 return k
#         return output


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        lib = {"a", "e", "i", "o", "u"}
        max_vowel = 0
        curr_vowel = 0
        # gets all vowels in the first k characters
        for i in range(k):
            if s[i] in lib:
                curr_vowel += 1
        max_vowel = curr_vowel
        # starts sliding window from k to the end of the string
        for i in range(k, len(s)):
            if s[i - k] in lib:
                curr_vowel -= 1
            if s[i] in lib:
                curr_vowel += 1
            # Early return if curr_vowel is already k
            if curr_vowel == k:
                return k
            max_vowel = max(curr_vowel, max_vowel)
        return max_vowel


s = "abciiidef"
k = 3
expected = 3
print("Actual:  ", Solution().maxVowels(s, k))
print("Expected:", expected)

s = "aeiou"
k = 2
expected = 2
print("Actual:  ", Solution().maxVowels(s, k))
print("Expected:", expected)
