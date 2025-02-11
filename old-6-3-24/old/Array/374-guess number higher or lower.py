# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    number = 2
    if num > number:
        return -1
    if num < number:
        return 1
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        if n <=1: return n
        bottom = 0
        current_guess = int(n / 2)
        for _ in range(current_guess + 2):
            guess_result = guess(current_guess)
            print(current_guess)
            print(f"{bottom} - {n}")
            print(guess_result)
            if guess_result == 0:
                return current_guess
            if abs(n - current_guess) <= 2:
                current_guess += guess_result
                continue
            if guess_result == 1:
                bottom = current_guess
                current_guess += int((n - current_guess) / 2)
                continue
            if guess_result == -1:
                n = current_guess
                current_guess = bottom + int((current_guess - n) / 2)
                continue
n = 2
print(Solution().guessNumber(n))
