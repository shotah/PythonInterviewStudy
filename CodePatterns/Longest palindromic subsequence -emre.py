# https://emre.me/coding-patterns/palindromes/

# How to identify?

# Palindromes pattern is very useful to solve Dynamic Programming problems 
# involving palindromes and palindromic strings, substrings, subsequences etc.


# Problem: Longest Palindromic Subsequence
# LeetCode 516 - Longest Palindromic Subsequence [medium]

# Given a string s, find the longest palindromic subsequence’s length in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "bbbab"
# Output: 4
# One possible longest palindromic subsequence is "bbbb".
# Example 2:

# Input: "cbbd"
# Output: 2
# One possible longest palindromic subsequence is "bb".

# Brute Force Solution
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestPalindromeSubseq_recursive(s, 0, len(s) - 1)

    def longestPalindromeSubseq_recursive(self, s, start, end):
        if start > end:
            return 0

        # every sequence with one element is a palindrome of length 1
        if start == end:
            return 1

        # case 1: elements at the beginning and the end are the same
        if s[start] == s[end]:
            return 2 + self.longestPalindromeSubseq_recursive(s, start + 1, end - 1)

        # case 2: skip one element either from the beginning or the end
        subseq1 = self.longestPalindromeSubseq_recursive(s, start + 1, end)
        subseq2 = self.longestPalindromeSubseq_recursive(s, start, end - 1)

        return max(subseq1, subseq2)
    
# Time Complexity: O(2N) because we are making 2 recursive calls in the same function.

# Space Complexity: O(N) which is used to store the recursion stack.

# Top-down Dynamic Programming with Memoization
# start and end are two changing values of our recursive function in the Brute Force Solution. So, we can store the results of all subsequences in a two-dimensional array to memoize them.

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        return self.longestPalindromeSubseq_recursive(memo, s, 0, len(s) - 1)

    def longestPalindromeSubseq_recursive(self, memo, s, start, end):
        if start > end:
            return 0

        # every sequence with one element is a palindrome of length 1
        if start == end:
            return 1

        if memo[start][end] == -1:
            # case 1: elements at the beginning and the end are the same
            if s[start] == s[end]:
                memo[start][end] = 2 + self.longestPalindromeSubseq_recursive(memo, s, start + 1, end - 1)
            else:
                # case 2: skip one element either from the beginning or the end
                subseq1 = self.longestPalindromeSubseq_recursive(memo, s, start + 1, end)
                subseq2 = self.longestPalindromeSubseq_recursive(memo, s, start, end - 1)
                memo[start][end] = max(subseq1, subseq2)

        return memo[start][end]
# Time Complexity: O(N2) because memoization array, memo[len(s)][len(s)]. We will not have more than N*N subsequences.

# Space Complexity: O(N2 + N) == O(N2) because we used N2 for memoization array and N for recursive stack.

# Bottom-up Dynamic Programming with Tabulation
# We can build our two-dimensional memoization array in a bottom-up fashion, adding one element at a time.

# if the element at the start and the end is matching, the length of Longest Palindromic Substring (LPS) is 2 plus the length of LPS till start+1 and end-1.
# if the element at the start does not match the element at the end, we will take the max of LPS by either skipping the element at start or end
# So the overall algorith will be;

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = [[0 for _ in range(len(s))] for _ in range(len(s))]
        # every sequence with one element is a palindrome of length 1
        for i in range(len(s)):
            memo[i][i] = 1
        for start in range(len(s) - 1, -1, -1):
            for end in range(start + 1, len(s)):
                # case 1: elements at the beginning and the end are the same
                if s[start] == s[end]:
                    memo[start][end] = 2 + memo[start + 1][end - 1]
                else:  # case 2: skip one element either from the beginning or the end
                    memo[start][end] = max(memo[start + 1][end], memo[start][end - 1])
        return memo[0][len(s) - 1]

# Time Complexity: O(N2)

# Space Complexity: O(N2) where N is the input sequence.
