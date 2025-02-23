class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        return [False]


candies = [2, 3, 5, 1, 3]
extraCandies = 3
expected = [True, True, True, False, True]
print("Actual:  ", Solution().kidsWithCandies(candies, extraCandies))
print("Expected:", expected)
