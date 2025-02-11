class Solution:
    def computeAreaOfSquare(self, x1: int, y1: int, x2: int, y2: int) -> int:
        """computer the area of a single square."""
        length = abs(x1) + abs(x2)
        width = abs(y1) + abs(y2)
        return length * width

    # def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    #     return(
    #         self.computeAreaOfSquare(ax1, ay1, ax2, ay2) +
    #         self.computeAreaOfSquare(bx1, by1, bx2, by2)
    #     )
    def calculateAreaToRemove(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        """calculates area to remove from square A"""
        a = [ax1, ay1, ax2, ay2]
        b = [bx1, by1, bx2, by2]

        a_upper_left_corner = [ax1, ay2]
        a_lower_left_corner = [ax1, ay1]
        a_upper_right_corner = [ax2, ay2]
        a_lower_right_corner = [ax2, ay1]

        b_upper_left_corner = [bx1, by2]
        b_lower_left_corner = [bx1, by1]
        b_upper_right_corner = [bx2, by2]
        b_lower_right_corner = [bx2, by1]

        if (
            a_upper_left_corner[0] < b_lower_right_corner[0]
            and a_upper_left_corner[1] < b_lower_right_corner[1]
        ):
            print(a_upper_left_corner, b_lower_right_corner)
            print("a_upper_left_corner overlaps with b_lower_right_corner")

        if (
            a_lower_left_corner[0] < b_upper_right_corner[0]
            and a_lower_left_corner[1] < b_upper_right_corner[1]
        ):
            print(a_lower_left_corner, b_upper_right_corner)
            print("a_lower_left_corner overlaps with b_upper_right_corner")

        if (
            a_upper_right_corner[0] < b_lower_left_corner[0]
            and a_upper_right_corner[1] < b_lower_left_corner[1]
        ):
            print(a_upper_right_corner, b_lower_left_corner)
            print("a_upper_right_corner overlaps with b_lower_left_corner")

        if (
            a_lower_right_corner[0] < b_upper_left_corner[0]
            and a_lower_right_corner[1] < b_upper_left_corner[1]
        ):
            print(a_lower_right_corner, b_upper_left_corner)
            print("a_lower_right_corner overlaps with b_upper_left_corner")
        return 1

    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        self.calculateAreaToRemove(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)


ax1 = -3
ay1 = 0
ax2 = 3
ay2 = 4
bx1 = 0
by1 = -1
bx2 = 9
by2 = 2
print(Solution().computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))
