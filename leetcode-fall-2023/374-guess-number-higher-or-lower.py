class Solution:
    def guessNumber(self, m: int) -> int:
        n = 1
        while n <= m:
            c = n + (m - n) // 2
            r = guess(c)
            if r == 0:
                return c
            elif r == 1:
                n = c + r
            else:
                m = c + r
