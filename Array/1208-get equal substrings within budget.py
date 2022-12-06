
class Solution:
    costs = []
    def __get_costs(self, s: str, t: str):
        for s_c, t_c in zip(s, t):
            s_ch = bytes((s_c), 'utf-8')
            t_ch = bytes((t_c), 'utf-8')
            self.costs.append(t_ch[0] - s_ch[0])

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        if not maxCost: return 1
        self.__get_costs(s, t)
        curr_length = 0
        max_length = curr_length
        running_cost = maxCost
        i = 0
        while i < len(self.costs):
            value = self.costs[i]
            if abs(value) <= running_cost:
                print(f"{i}: {running_cost} - {abs(value)}, {running_cost - abs(value)}")
                curr_length += 1
                running_cost -= abs(value)
                i += 1
            else:
                #print("looking for next substring")
                max_length = max(max_length, curr_length)
                running_cost = maxCost
                curr_length = 0
            print(f"current cost: {running_cost}")
        return max_length

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
