# class Solution:
#     def decodeString(self, s: str) -> str:
#         l = list(s)
#         r: list[str] = []
#         num: int = 0
#         prev: str = ""
#         while len(l) > 0:
#             ps = l.pop(0)
#             if ps == "[":
#                 num = int(prev)
#                 prev = ""
#                 continue
#             if ps == "]":
#                 r += prev * num
#                 num = 0
#                 prev = ""
#                 continue
#             prev = f"{prev}{ps}"
#         return "".join(r)


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = ""
        num = 0

        for letter in s:
            if letter.isdigit():
                # move num with * 10 over for append of l
                num = (num * 10) + int(letter)
                continue
            if letter == "[":
                stack.append((curr, num))
                curr = ""
                num = 0
                continue
            if letter == "]":
                last_string, repeat_count = stack.pop()
                curr = last_string + curr * repeat_count
                continue
            curr += letter
        return curr


sol = Solution()
s = "3[a]2[bc]"
s = "3[a2[c]]"
print(sol.decodeString(s))
