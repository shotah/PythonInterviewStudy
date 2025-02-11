from functools import reduce
import json


class Solution:
    t = {
        "1000": "M",
        "900": "CM",
        "500": "D",
        "400": "CD",
        "100": "C",
        "90": "XC",
        "50": "L",
        "40": "XL",
        "10": "X",
        "9": "IX",
        "5": "V",
        "4": "IV",
        "1": "I",
    }

    def intToRoman(self, num: int) -> str:
        result = ""
        for key in self.t.keys():
            while int(key) <= num:
                result += self.t[key]
                num -= int(key)
        return result


num = 9
print(Solution().intToRoman(num))
