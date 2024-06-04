class Solution:
    def area(self, x1,y1,x2,y2):
        return (x2-x1)*(y2-y1)
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        """Length: gets the lowest point of x2, and the upper most of x1, then return 0 or above"""
        xOverlap = max(min(ax2,bx2)-max(ax1,bx1), 0)
        """Width: gets the lowest point of y2, and the upper most of y1, then return 0 or above"""
        yOverlap = max(min(ay2,by2)-max(ay1,by1), 0)
        overlapArea = xOverlap*yOverlap
        return self.area(ax1,ay1,ax2,ay2) + self.area(bx1,by1,bx2,by2) - overlapArea

ax1 = -3
ay1 = 0
ax2 = 3
ay2 = 4
bx1 = 0
by1 = -1
bx2 = 9
by2 = 2
print(Solution().computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))
