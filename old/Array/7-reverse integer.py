class Solution:
    def reverse(self, x: int) -> int:
        reversed_string = int(str(abs(x))[::-1])
        return_value = -reversed_string if x < 0 else reversed_string
        print(return_value.bit_length())
        return return_value if return_value.bit_length() < 32 else 0
            

x = -123
x = 1563847412

print(
    Solution().reverse(x)
)
