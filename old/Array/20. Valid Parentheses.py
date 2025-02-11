class Solution:
    def isValid(self, s: str) -> bool:
        opens = ["(", "{", "["]
        closes = [")", "}", "]"]
        valid = []
        for c in s:
            if c in opens:
                valid.append(opens.index(c))
            if c in closes:
                if valid and valid[-1] == closes.index(c):
                    valid.pop()
                else: 
                    return False
        return valid == []


s = "()[]{}"
# s = "(]"
# s = "]"
s = Solution().isValid(s)
print(s)
