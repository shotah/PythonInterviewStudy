class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        wordlist1 = list(word1)
        wordlist2 = list(word2)
        while len(wordlist1) > 0 or len(wordlist2) > 0:
            output += wordlist1.pop(0) if len(wordlist1) > 0 else ""
            output += wordlist2.pop(0) if len(wordlist2) > 0 else ""
        return output


word1 = "abc"
word2 = "pqr"
expected = "apbqcr"

print("Actual:  ", Solution().mergeAlternately(word1, word2))
print("Expected:", expected)
