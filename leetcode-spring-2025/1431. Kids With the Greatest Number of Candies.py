# class Solution:
#     def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
#         # simple solution: Get the max value in the list, then check every value.
#         max_v = max(candies)
#         results = []
#         for v in candies:
#             results.append(
#                 True if (v + extraCandies) > max_v else False
#             )
#         return results


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_v = max(candies)
        return [(v + extraCandies) >= max_v for v in candies]


candies = [2, 3, 5, 1, 3]
extraCandies = 3
expected = [True, True, True, False, True]
print("Actual:  ", Solution().kidsWithCandies(candies, extraCandies))
print("Expected:", expected)
