# QUEUE~~
# first in first out!


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue: list[str] = list(senate)
        d_rem: int = 0
        r_rem: int = 0
        while True:
            s = queue.pop(0)
            if s == "R":
                if d_rem > 0:
                    d_rem -= 1
                    continue
                r_rem += 1
            if s == "D":
                if r_rem > 0:
                    r_rem -= 1
                    continue
                d_rem += 1
            if len(r_queue) == 0:
                return "Dire"
            if len(d_queue) == 0:
                return "Radiant"


s = Solution()
senate = "RD"
senate = "RDD"
print(s.predictPartyVictory(senate))
