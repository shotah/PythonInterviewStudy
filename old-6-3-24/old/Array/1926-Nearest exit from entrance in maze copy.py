class Solution:
    traveled_path = []
    def __test_step(self, maze, row: int, column: int) -> bool:
        if row == -1 or column == -1 or [row, column] in self.traveled_path: 
            return False
        try:
            print(f"Testing {maze[row][column]}")
            if maze[row][column] == ".":
                self.traveled_path.append([row, column])
                print(f"traveled_path: {self.traveled_path}")
                return True
        except:
            return False

    def __take_step(self, maze: list[list[str]], location: list[int]) -> list[int]:
        # North
        row = location[0] - 1
        column = location[1]
        if self.__test_step(maze, row, column):
            print("Went North")
            return [row, column]
        # East
        row = location[0]
        column = location[1] + 1
        if self.__test_step(maze, row, column):
            print("Went East")
            return [row, column]
        # South
        row = location[0] + 1
        column = location[1]
        if self.__test_step(maze, row, column):
            print("Went South")
            return [row, column]
        # West
        row = location[0]
        column = location[1] - 1
        if self.__test_step(maze, row, column):
            print("Went West")
            return [row, column]
        # No where to go:
        return location

    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        height = len(maze)
        length = len(maze[0])
        max_steps = height + length
        location = entrance
        self.traveled_path = [location]
        steps = 0
        while steps <= max_steps:
            print(f"location: {location}")
            new_location = self.__take_step(maze, location)
            print(f"new_location: {new_location}")
            if new_location == location:
                return -1
            location = new_location
            steps +=1
            height_broken = 0 >= location[0] or location[0] >= height -1
            length_broken = 0 >= location[1] or location[1] >= length -1
            print(f"height_broken {height_broken}, length_broken {length_broken}")
            if height_broken or length_broken: break
        return steps


maze = [
    ["+","+",".","+"],
    [".",".",".","+"],
    ["+","+","+","."]
]
entrance = [1,2]

maze = [["+","+","+"],[".",".","."],["+","+","+"]]
entrance = [1,0]

maze =[[".","+"]]
entrance = [0,0]

maze = [
    ["+",".","+","+","+","+","+"],
    ["+",".","+",".",".",".","+"],
    ["+",".","+",".","+",".","+"],
    ["+",".",".",".","+",".","+"],
    ["+","+","+","+","+",".","+"]
]
entrance = [0,1]

maze = [
    ["+",".","+","+","+","+","+"],
    ["+",".","+",".",".",".","+"],
    ["+",".","+",".","+",".","+"],
    ["+",".",".",".","+",".","+"],
    ["+","+","+","+","+","+","."]
]
entrance = [0,1]
maze = [
    ["+",".","+","+","+","+","+"],
    ["+",".","+",".",".",".","+"],
    ["+",".","+",".","+",".","+"],
    ["+",".",".",".",".",".","+"],
    ["+","+","+","+",".","+","."]
]
entrance = [0,1]
print(
  Solution().nearestExit(maze, entrance)
)
