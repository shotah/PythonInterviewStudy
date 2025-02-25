# 394. Decode String


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = ""
        num = 0
        for l in s:
            if l.isdigit():
                # move num with * 10 over for append of l
                num = (num * 10) + int(l)
                continue
            if l == "[":
                # setting num... curr should be empty
                stack.append((curr, num))
                curr = ""
                num = 0
                continue
            # Handles the closing bracket and writes the string
            if l == "]":
                last_string, repeat_count = stack.pop()
                curr = last_string + curr * repeat_count
                continue
            curr += l
        return curr


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case
    s = "3[a]2[bc]"
    expected = "aaabcbc"
    actual = Solution().decodeString(s)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {s}, Expected: {expected}, Actual: {actual}"
