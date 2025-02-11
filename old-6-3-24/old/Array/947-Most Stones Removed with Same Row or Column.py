class Solution:
    def __init__(self):
        self.stones_to_remove = []
        self.stone_to_save = []

    def enumerate_stones(self, stones):
        row_with_stones = {}
        column_with_stones = {}
        stones_path = {}
        for idx, stone in enumerate(stones):
            stones_path[idx] = []
            for stone in stones:
                if row_with_stones.get(stone[0]) or column_with_stones.get(stone[1]):
                    self.stones_to_remove.append(stone)
                row_with_stones[stone[0]] = True
                column_with_stones[stone[1]] = True
    
    def remove_stones(self, stones):
        new_stones = []
        for stone in stones:
            if stone not in self.stones_to_remove or stone in self.stone_to_save:
                new_stones.append(stone)
        return new_stones

    def removeStones(self, stones: list[list[int]]) -> int:
        original_stone_quantity = len(stones)
        self.stone_to_save.append(stones[0])
        self.enumerate_stones(stones)
        print(original_stone_quantity, len(self.stones_to_remove))
        
        print(self.stones_to_remove)
        kept_stones = self.remove_stones(stones)
        print("kept_stones", kept_stones)
        
        return original_stone_quantity - len(kept_stones)


stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# 2
stones = [[0,1],[1,0],[1,1]]
# 0
# stones = [[0,0]]
# 4
# stones = [[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]]
print(
  Solution().removeStones(stones)

)
