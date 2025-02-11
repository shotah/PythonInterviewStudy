class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key = lambda x: x[1])
        count = 0
        print(points)
        end = points[0][0]-1
        for a, b in points:
            if end < a:
                count += 1
                end = b
        return count
    

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
