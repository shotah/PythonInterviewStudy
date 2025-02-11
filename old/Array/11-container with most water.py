class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_water = 0
        left_index = 0
        right_index = len(height) - 1
        while left_index < right_index:
            width = abs(left_index - right_index)
            area = width * min(height[left_index], height[right_index])
            max_water = max(area, max_water)
            if height[left_index] > height[right_index]:
                right_index -= 1
            else:
                left_index += 1
        return max_water


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# height = [1,1]

sol = Solution().maxArea(height)
print(f"\nSolution: {sol}")
