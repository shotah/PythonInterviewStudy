class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        result = 0
        last_index = 0
        for c in list(word):
            c_idx = keyboard.index(c)
            move_cost = last_index - c_idx
            last_index = c_idx
            result += abs(move_cost)
        return result
      
keyboard = "abcdefghijklmnopqrstuvwxyz"
word ="cba"
s = Solution().calculateTime(keyboard, word)
print( 
    s
)
