class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        output = False
        for i in range(len(s)):
            if s[i] in t:
                output = True
                t = t[t.index(s[i]) + 1:]
            else:
                output = False
                break
        return output


s = "abc"
t = "ahbgdc"
expected = True
print("Actual:  ", Solution().isSubsequence(s, t))
print("Expected:", expected)
