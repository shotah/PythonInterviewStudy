class Solution:
    def __max_water_height(self, index: int, height: list[int]) -> int:
        start_height = height[index]
        max_water = 0
        for cur_idx, cur_height in enumerate(height[index:], index):
            cur_water = (cur_idx - index) * min(cur_height, start_height)
            max_water = max(max_water, cur_water)
        return max_water

    def maxArea(self, height: list[int]) -> int:
        max_water = 0
        for cur_idx in range(len(height)):
            cur_max = self.__max_water_height(cur_idx, height)
            max_water = max(max_water, cur_max)
        return max_water

height= [1,8,6,2,5,4,8,3,7]
# height = [1,1]

sol = Solution().maxArea(height)
print(
    f"\nSolution: {sol}"
)
