class Solution:
    def removeStars(self, s: str) -> str:
        r: list = []
        for c in s:
            if c == "*":
                r.pop()
            else:
                r.append(c)
        return "".join(r)
