class Node:
    def __init__(self, location: list[int] = None):
        self.location = location
        self.north: Node = self
        self.east: Node = self
        self.south: Node = self
        self.west: Node = self


class Solution:
    adding_nodes_traveled_path = []
    getting_nodes_traveled_path = []
    max_hight = 0
    max_width = 0

    def __test_step(
        self, maze, location: list[int], visited: list
    ) -> tuple[bool, list]:
        if location[0] == -1 or location[1] == -1 or location in visited:
            return (False, visited)
        try:
            if maze[location[0]][location[1]] == ".":
                visited.append(location)
                return (True, visited)
        except:
            return (False, visited)
        return (False, visited)

    def __add_nodes(
        self, maze: list[list[str]], current_node: Node, visited: list = []
    ) -> Node:
        location = current_node.location
        north = [location[0] - 1, location[1]]
        (available, visited) = self.__test_step(maze, north, visited)
        if available:
            current_node.north = self.__add_nodes(maze, Node(north), visited)
        east = [location[0], location[1] + 1]
        (available, visited) = self.__test_step(maze, east, visited)
        if available:
            current_node.east = self.__add_nodes(maze, Node(east), visited)
        south = [location[0] + 1, location[1]]
        (available, visited) = self.__test_step(maze, south, visited)
        if available:
            current_node.south = self.__add_nodes(maze, Node(south), visited)
        west = [location[0], location[1] + 1]
        (available, visited) = self.__test_step(maze, west, visited)
        if available:
            current_node.west = self.__add_nodes(maze, Node(west), visited)
        print(current_node.location, end=" ")
        return current_node

    def __bfs(self, current_node: Node):
        self.getting_nodes_traveled_path.append(current_node.location)
        steps = 1
        queue = [(current_node, int(steps))]
        # steps need to be inside queue to avoid extra steps
        while queue:
            (queue_node, steps) = queue.pop(0)
            for neighbor_node in [
                queue_node.north,
                queue_node.east,
                queue_node.south,
                queue_node.west,
            ]:
                if neighbor_node.location not in self.getting_nodes_traveled_path:
                    print(neighbor_node.location, end=" ")
                    y = neighbor_node.location[0]
                    x = neighbor_node.location[1]
                    if y <= 0 or y >= self.max_hight or x <= 0 or x >= self.max_width:
                        return steps if not steps == 0 else -1
                    self.getting_nodes_traveled_path.append(neighbor_node.location)
                    queue.append((neighbor_node, int(steps + 1)))
        return -1

    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        self.adding_nodes_traveled_path = [entrance]
        self.max_hight = len(maze) - 1
        self.max_width = len(maze[0]) - 1
        start_node = Node(entrance)
        print("adding nodes")
        self.__add_nodes(maze, start_node)
        print("\nsearching nodes")
        return self.__bfs(start_node)


# Expected 1
maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
entrance = [1, 2]

# Expected 2
maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
entrance = [1, 0]

# Expected -1
# maze =[[".","+"]]
# entrance = [0,0]

# Expected 12
# maze = [
#     ["+",".","+","+","+","+","+"],
#     ["+",".","+",".",".",".","+"],
#     ["+",".","+",".","+",".","+"],
#     ["+",".",".",".","+",".","+"],
#     ["+","+","+","+","+",".","+"]
# ]
# entrance = [0,1]

# result should be -1
# maze = [
#     ["+",".","+","+","+","+","+"],
#     ["+",".","+",".",".",".","+"],
#     ["+",".","+",".","+",".","+"],
#     ["+",".",".",".","+",".","+"],
#     ["+","+","+","+","+","+","."]
# ]
# entrance = [0,1]

# result should be 7
# maze = [
#     ["+",".","+","+","+","+","+"],
#     ["+",".","+",".",".",".","+"],
#     ["+",".","+",".","+",".","+"],
#     ["+",".",".",".",".",".","+"],
#     ["+","+","+","+",".","+","."]
# ]
# entrance = [0,1]

print(Solution().nearestExit(maze, entrance))
