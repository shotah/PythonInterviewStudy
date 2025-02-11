# https://emre.me/coding-patterns/longest-common-substring-subsequence/


# How to identify?

# Longest Common Substring / Subsequence pattern is very useful 
# to solve Dynamic Programming problems involving longest / 
# shortest common strings, substrings, subsequences etc.


# Problem: Longest Common Subsequence
# LeetCode 1143 - Longest Common Subsequence [medium]

# Given two strings text1 and text2, return the length of their longest common subsequence.

# A common subsequence of two strings is a subsequence that is common to both strings. If there is no common subsequence, return 0.

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
# Constraints:

# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# The input strings consist of lowercase English characters only.

# Brute Force Solution
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.longestCommonSubsequence_recursive(text1, text2, 0, 0)

    def longestCommonSubsequence_recursive(self, text1, text2, i, j):
        if i == len(text1) or j == len(text2):
            return 0
        if text1[i] == text2[j]:
            return 1 + self.longestCommonSubsequence_recursive(text1, text2, i + 1, j + 1)

        return max(self.longestCommonSubsequence_recursive(text1, text2, i + 1, j),
                   self.longestCommonSubsequence_recursive(text1, text2, i, j + 1))
        
# Time Complexity: O(2N+M) where N and M are the lengths of two input strings.

# Space Complexity: O(N + M) which is used to store the recursion stack.

# Top-down Dynamic Programming with Memoization
# We can use a two-dimensional array to store the already solved subproblems.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        return self.longestCommonSubsequence_recursive(memo, text1, text2, 0, 0)

    def longestCommonSubsequence_recursive(self, memo, text1, text2, i, j):
        if i == len(text1) or j == len(text2):
            return 0
        if memo[i][j] == -1:
            if text1[i] == text2[j]:
                memo[i][j] = 1 + self.longestCommonSubsequence_recursive(memo, text1, text2, i + 1, j + 1)
            else:
                memo[i][j] = max(self.longestCommonSubsequence_recursive(memo, text1, text2, i + 1, j),
                                 self.longestCommonSubsequence_recursive(memo, text1, text2, i, j + 1))
        return memo[i][j]
# Time Complexity: O(N * M) where N and M are the lengths of two input strings.

# Space Complexity: O(N * M)

# Bottom-up Dynamic Programming with Tabulation
# Lets create our two dimensional array in a bottom-up fashion.

# if the characters text1[i] matches text2[j], the length of the common subsequence would be one plus the length of the common subsequence until the i-1 and j-1 indexes.
# if the characters text1[i] and text2[j] does not match, we take the longest sequence by skipping one character either from ith string or jth character from respective strings.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        max_length = 0
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    memo[i][j] = 1 + memo[i - 1][j - 1]
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
                max_length = max(max_length, memo[i][j])
        return max_length
# Time Complexity: O(N * M) where N and M are the lengths of two input strings.

# Space Complexity: O(N * M)
