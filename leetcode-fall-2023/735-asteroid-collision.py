# from typing import List


# class Solution:
#     moving_right: list = []
#     moving_left: list = []

#     def _calc_asteroids(self, a: int) -> None:
#         if a > 0:
#             # a is moving right
#             b = self.moving_left.pop()
#             if a > b:
#                 self.moving_right.append(a)
#             if a < b:
#                 self.moving_left.append(b)
#         if a < 0:
#             # a is moving left
#             b = self.moving_right.pop()
#             if a > b:


#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         for a in asteroids:
#             self._calc_asteroids(a)
#         return self.moving_left if len(self.moving_left) > 0 else self.moving_right

# from typing import Optional


# class Solution:
#     def asteroidCollision(self, asteroids: list[int]) -> list[int]:
#         s: list[int] = []
#         p: Optional[int] = None
#         for a in asteroids:
#             while True:
#                 if len(s) == 0:
#                     s.append(a)
#                     break
#                 p = s.pop()
#                 if (a > 0 and p > 0) or (a < 0 and p < 0):
#                     print(f"appending p {p} and a {a}")
#                     s.append(p)
#                     s.append(a)
#                     p = a
#                     break
#                 if a > 0 and p < 0:
#                     # previous is moving left, and a is moving right.
#                     s.append(p)
#                     s.append(a)
#                     break
#                 if a < 0 and p > 0:
#                     r = abs(a) - abs(p)
#                     if r > 0:
#                         # a wins, we need a new P!!!
#                         # verify we have any stack left
#                         if len(s) == 0:
#                             s.append(a)
#                             break
#                     elif r < 0:
#                         # p wins, append p back
#                         s.append(p)
#                         break
#                     else:
#                         # they explode:
#                         break
#         return s


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        s = []
        for a in asteroids:
            while s and s[-1] > 0 > a:
                # A wins, keep going
                if s[-1] < -a:
                    s.pop()
                    continue
                # its a tie! they both die
                if s[-1] == -a:
                    s.pop()
                # stack wins do nothing
                break
            # no collision, append a
            else:
                s.append(a)
        return s


s = Solution()
asteroids = [5, 10, -5]
asteroids = [-2, -1, 1, 2]
asteroids = [1, -1, -2, -2]
print(s.asteroidCollision(asteroids))
