from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ast_lst = []
        if len(asteroids) == 0:
            return ast_lst

        for a in asteroids:
            while len(ast_lst) > 0:
                p_a = ast_lst.pop()
                print(ast_lst)
                print(p_a, a)
                if a > 0 and p_a > 0 or a < 0 and p_a < 0:
                    ast_lst.append(p_a)
                    ast_lst.append(a)
                    break
                print(f"adding {p_a} + {a}")
                a = p_a + a
            ast_lst.append(a)
        return ast_lst


asteroids = [5, 10, -5]
c = Solution()
r = c.asteroidCollision(asteroids)
print(r)
