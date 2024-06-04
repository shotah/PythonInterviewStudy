class Solution:
    t = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }
    def romanToInt(self, s: str) -> int:
        result = 0
        arr_s = list(s)
        for i in range(len(arr_s)):
            if len(arr_s) -1 > i and self.t[arr_s[i]] < self.t[arr_s[i+1]]:
                result -= self.t[arr_s[i]]
            else:
                result += self.t[arr_s[i]]
        return result

# expected 1994
s = "MCMXCIV"
print(
  Solution().romanToInt(s)
)
