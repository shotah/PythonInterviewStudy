class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        for i in range(len(flowerbed)):
            can_plant_here = flowerbed[i] == 0
            is_left_plot_empty = (i == 0) or (flowerbed[i - 1] == 0)
            is_right_plot_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
            if can_plant_here and is_left_plot_empty and is_right_plot_empty:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False
