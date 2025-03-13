class Solution:
    def removeStars(self, s: str) -> str:
        r: list = []
        for c in s:
            if c == "*":
                r.pop()
            else:
                r.append(c)
        return "".join(r)


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case
    s = "leet**cod*e"
    expected = "lecoe"
    actual = Solution().removeStars(s)
    assert actual == expected, f"Test Case Failed: Input: {s}, Expected: {expected}, Actual: {actual}"
