class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        for idx, char in enumerate(min(strs,key=len)):
            for word in strs:
                if char != word[idx]:
                    return result
            result += char
        return result

# Output: "fl"
strs = ["flower","flow","flight"]
# strs = ["ab", "a"]
print(
  Solution().longestCommonPrefix(strs)
)
