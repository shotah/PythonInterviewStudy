import json

class Solution:
    def frequencySort(self, s: str) -> str:
        h = {}
        r = ""
        for c in list(s):
            if c in h:
                h[c] +=1
            else:
                h[c] =1
        sorted_x = sorted(h.items(), key=lambda kv: kv[1], reverse=True)
        for k,v in sorted_x:
            r += k * v
        return r 
t=[
    ["tree", "eert"],
    ["cccaaa", "cccaaa"]
]

for s, expected in t:
    r = Solution().frequencySort(s)
    print(
        f"{s}, {r} == {expected}"
    )
