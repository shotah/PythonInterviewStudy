# class Solution:
#     def asteroidCollision(self, asteroids: list[int]) -> list[int]:
#         s = []
#         for a in asteroids:
#             while s and s[-1] > 0 > a:
#                 # A wins, keep going
#                 if s[-1] < -a:
#                     s.pop()
#                     continue
#                 # its a tie! they both die
#                 if s[-1] == -a:
#                     s.pop()
#                 # stack wins do nothing
#                 break
#             # no collision, append a
#             else:
#                 s.append(a)
#         return s


#  (positive meaning right, negative meaning left).
#  If two asteroids meet, the smaller one will explode.
#  If both are the same size, both will explode.
#  Two asteroids moving in the same direction will never meet.
# class Solution:
#     def asteroidCollision(self, asteroids: list[int]) -> list[int]:
#         stack = []
#         # walk through asteroids...
#         for curr_asteroid in asteroids:
#             # walk through previous asteroids that are bigger
#             while stack and stack[-1] > 0 > curr_asteroid:
#                 prev_asteroid = stack[-1]
#                 # scenarios A Wins
#                 if prev_asteroid < -curr_asteroid:
#                     stack.pop()
#                     # keep going to see if A will keep winning
#                     continue
#                 # scenario Tie and both are removed
#                 elif prev_asteroid == -curr_asteroid:
#                     # remove previous
#                     stack.pop()
#                 # break DO NOT APPEND current
#                 break
#             # if no loop or at end of loop append the asteroid.
#             else:
#                 stack.append(curr_asteroid)
#         return stack


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 > a:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff == 0:
                    stack.pop()
                    a = 0
                else:
                    a = 0
                    break
            if a != 0:
                stack.append(a)
        return stack


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case
    asteroids = [5, 10, -5]
    expected = [5, 10]
    actual = Solution().asteroidCollision(asteroids)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {asteroids}, Expected: {expected}, Actual: {actual}"

    # Test Case
    asteroids = [8, -8]
    expected = []
    actual = Solution().asteroidCollision(asteroids)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {asteroids}, Expected: {expected}, Actual: {actual}"

    # Test Case
    asteroids = [10, 2, -5]
    expected = [10]
    actual = Solution().asteroidCollision(asteroids)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {asteroids}, Expected: {expected}, Actual: {actual}"
