class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_to_test = str(x)
        length = len(str_to_test) -1
        for i in range(length):
            if str_to_test[i] != str_to_test[length -i]:
                return False
        return True
x = 121
x = 1221
x = 1121
print(
    Solution().isPalindrome(x)
)
