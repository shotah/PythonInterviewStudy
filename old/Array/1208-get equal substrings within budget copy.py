
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        result = 0
        for s_c, t_c in zip(s, t):
            while maxCost > 0 and s_c != t_c:
                s_ch = bytes((s_c), 'utf-8')
                t_ch = bytes((t_c), 'utf-8')
                print(f"{s_ch[0]} < {t_ch[0]}")
                if s_ch[0] < t_ch[0]:
                    s_c = bytes([s_ch[0] + 1]).decode("utf-8")
                else:
                    s_c = bytes([s_ch[0] - 1]).decode("utf-8")
                print(s_c, t_c, maxCost)
                maxCost -=1
            if s_c == t_c:
                result += 1
            if not maxCost:
                return result
        return result

vals = [
#   ["abcd", "bcdf", 3, 3],
#   ["abcd", "cdef", 3, 1],
#   ["abcd", "acde", 0, 1],
  ["krrgw", "zjxss", 19, 2]
]

for s, t, maxCost, expected in vals:
    sol = Solution().equalSubstring(s, t, maxCost)
    print(
      f"{sol} == {expected}"
    )
