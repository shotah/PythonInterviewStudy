class Solution:
    def __find_overlap(self, x: list[int], y: list[int]) -> list[int]:
        if not x: return y
        left = max(x[0], y[0])
        right = min(x[1], y[1])
        return [left, right]

    def __find_overlaps(self, points: list[list[int]]) -> int:
        count = 0
        overlap = []
        pre_overlap = []
        run = 0
        for idx, point in enumerate(points):
            if idx == len(points) -1 and pre_overlap != []:
                count +=1
            print(f"point: {point}")
            overlap = self.__find_overlap(overlap, point)
            print(f"if {overlap} != {pre_overlap} and {overlap[0]} > {overlap[1]}")
            if overlap != pre_overlap and overlap[0] > overlap[1]:
                if run == 1:
                    count +=1
                count += 1
                print(f"count: {count}")
                overlap = []
                run = 0
            else:
                run += 1
            pre_overlap = overlap
        if points and count == 0: return 1
        return count
    
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])
        print(f"/n points: {points}")
        return self.__find_overlaps(points)
t=[
    [[[10,16],[2,8],[1,6],[7,12]], 2],
    [[[1,2],[3,4],[5,6],[7,8]], 4],
    [[[1,2],[2,3],[3,4],[4,5]], 2],
    [[[2,3],[2,3]], 1],
    [[[-1,1],[0,1],[2,3],[1,2]], 2]
]

for points, expected in t:
    r = Solution().findMinArrowShots(points)
    print(
        f"{r} == {expected} \n"
    )
