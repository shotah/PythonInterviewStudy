class Solution:
    def myAtoi(self, s: str) -> int:
        max_bit_value = 2_147_483_648
        charge_signs = ["+","-"]
        char_list = [str(i) for i in range(10)]
        char_list.extend(["."])
        isDecimal = False
        charge_sign = "+"
        result_list = []
        for c in s:
            if c in charge_signs:
                charge_sign = c
            elif c == " ":
                continue
            elif c not in char_list:
                break
            elif c == ".":
                isDecimal = True
            else:
                result_list.append(c)
        if not result_list: return 0
        result = float("".join(result_list)) if isDecimal else int("".join(result_list))
        if result > max_bit_value:
            result = max_bit_value
        if charge_sign == "-":
            result *= -1
        return format(result)

s= "   -42"
# s="4193 with words"
# s= "words and 987"
s="-+12"
s="-91283472332"
s='3.14159'
s = "42"
print(
    Solution().myAtoi(s)
)
