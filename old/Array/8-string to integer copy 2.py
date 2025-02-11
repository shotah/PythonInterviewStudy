class Solution:
    def myAtoi(self, incoming_string: str) -> int:
        max_bit_value = 2_147_483_648
        num = 0
        incoming_string = incoming_string.strip()
        if len(incoming_string) == 0:
            return 0
        sign = -1 if incoming_string[0] == "-" else 1
        for curr_char in incoming_string:
            if curr_char.isdigit():
                num = num * 10 + int(curr_char)
            elif curr_char in ["+", "-"]:
                continue
            else:
                break
        num = num * sign
        if -max_bit_value <= num <= max_bit_value - 1:
            return num
        return -max_bit_value if num < 0 else max_bit_value - 1


s = "   -42"
# s="4193 with words"
# s= "words and 987"
s = "-+12"
s = "-91283472332"
# s='3.14159'
# s = "42"
print(Solution().myAtoi(s))
