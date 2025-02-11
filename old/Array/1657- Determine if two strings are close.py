class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        return True
      
t =[
    ["abc", "bca", True],
    ["a", "aa", False],
    ["cabbba", "cabbba", True],
    ["cabbba", "aabbss", False],
]
for word1, word2, expected in t:
    s = Solution().closeStrings(word1, word2)
    print(f"\n {word1}, {word2}")
    print(f"\t {s} should be {expected}")
