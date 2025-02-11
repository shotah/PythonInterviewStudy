class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        previous_s = None
        while previous_s != s:
            for char in list(s):
                char_to_remove = char * k
                s = s.replace(char_to_remove, "")
            previous_s = s
        return s

vals = [
  ["abcd", 2, "abcd"],
  ["deeedbbcccbdaa", 3, "aa"]
]
 
for s, k, expected in vals:
    sol = Solution().removeDuplicates(s, k)
    print(
      f"{sol} == {expected}"
    )
