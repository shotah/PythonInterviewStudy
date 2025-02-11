class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            # check for stack and if last entry in stack is c
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return "".join([a*b for a, b in stack])

vals = [
  ["abcd", 2, "abcd"],
  ["deeedbbcccbdaa", 3, "aa"]
]
 
for s, k, expected in vals:
    sol = Solution().removeDuplicates(s, k)
    print(
      f"{sol} == {expected}"
    )
