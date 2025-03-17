class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[: self.gcd(len(str1), len(str2))]


str1 = "ABCABC"
str2 = "ABC"
expected = "ABC"
print("Actual:  ", Solution().gcdOfStrings(str1, str2))
print("Expected:", expected)
