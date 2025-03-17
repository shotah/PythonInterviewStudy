class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        min_len = min(n1, n2)
        result = []
        for i in range(min_len):
            result.append(word1[i])
            result.append(word2[i])
        result.extend(word1[min_len:])
        result.extend(word2[min_len:])
        return "".join(result)


word1 = "abc"
word2 = "pqr"
expected = "apbqcr"

print("Actual:  ", Solution().mergeAlternately(word1, word2))
print("Expected:", expected)
