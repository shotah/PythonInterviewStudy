# # You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# # Find two lines that together with the x-axis form a container, such that the container contains the most water.

# # Return the maximum amount of water a container can store.


# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         max_water = 0
#         left_index = 0
#         right_index = len(height) - 1
#         while left_index < right_index:
#             width = abs(left_index - right_index)
#             area = width * min(height[left_index], height[right_index])
#             max_water = max(area, max_water)
#             if height[left_index] > height[right_index]:
#                 right_index -= 1
#             else:
#                 left_index += 1
#         return max_water


# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         left = 0
#         right = len(height) - 1
#         maxWater = 0
#         while left < right:
#             maxWater = max(maxWater, (right - left) * min(height[left], height[right]))
#             if height[left] < height[right]:
#                 left += 1
#             else:
#                 right -= 1
#         return maxWater


# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         left, right = 0, len(height) - 1
#         max_area = 0
#         while left < right:
#             area = (right - left) * min(height[left], height[right])
#             max_area = max(max_area, area)
#             if height[left] < height[right]:
#                 left += 1
#             else:
#                 right -= 1
#         return max_area


class Solution:
    def maxArea(self, height: list[int]) -> int:
        # lets start with two pointers on either side of the array.
        left = 0
        right = len(height) - 1
        max_water = 0
        # Okay lets walk through until the meet in the middle.
        while left < right:
            # length times height to get the area..
            current_water_area = (right - left) * min(height[left], height[right])
            max_water = max(max_water, current_water_area)
            # step the smaller entry:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    expected = 49
    actual = Solution().maxArea(height)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {height}, Expected: {expected}, Actual: {actual}"

    print("\nInline tests finished.")
