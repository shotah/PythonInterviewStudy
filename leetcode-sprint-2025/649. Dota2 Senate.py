class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_arr = []
        d_arr = []
        for i, s in enumerate(senate):
            if s == "R":
                r_arr.append(i)
            else:
                d_arr.append(i)
        next_loop = len(senate)
        while r_arr and d_arr:
            r = r_arr.pop(0)
            d = d_arr.pop(0)
            if r < d:
                r_arr.append(next_loop + r)
            else:
                d_arr.append(next_loop + d)
        return "Radiant" if r_arr else "Dire"


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case
    senate = "RD"
    expected = "Radiant"
    actual = Solution().predictPartyVictory(senate)
    assert actual == expected, f"Test Case Failed: Input: {senate}, Expected: {expected}, Actual: {actual}"

    # Test Case
    senate = "RDD"
    expected = "Dire"
    actual = Solution().predictPartyVictory(senate)
    assert actual == expected, f"Test Case Failed: Input: {senate}, Expected: {expected}, Actual: {actual}"
