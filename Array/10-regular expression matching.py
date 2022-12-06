class Solution:
    def __test_astrict(self, s: str, p: str) -> bool:
        arr = p.replace(".*", ",ANY,")
        arr = arr.replace("*", ",MANY,")
        arr = arr.replace(".", ",SINGLE,")
        
        arr = arr.split(",")
        arr = list(filter(None, arr))
        print(f"broken arr={','.join(arr)}")
        it = iter(arr)
        for match, char in list(zip(it,it)):
            print(char)
            for string in list(filter(None, s.split(match))):
                print(f"looking for: {match} w/{char} in {string}, Remaining to parse: {s}")
                if char == "ANY":
                    print(f"Replacing {match} in {s}")
                    s = s.replace(match, "", 1)
                    print(f"Replacing {string} in {s}")
                    s = s.replace(string, "", 1)
                    break
                if char == "MANY":
                    print(f"Replacing {match} in {s}")
                    s = s.replace(match, "", 1)
                    char_match = list(match)[-1]
                    string_match = list(string)[0]
                    while char_match == string_match:
                        print(f"Replacing {string_match} in {s}")
                        s = s.replace(string_match, "", 1)
                        string = string.replace(char_match, "", 1)
                        string_match = list(string)[0]
                    break
                if char == "SINGLE":
                    print(f"Replacing {match} in {s}")
                    s = s.replace(match, "", 1)
                    char_match = list(match)[-1]
                    string_match = list(string)[0]
                    if char_match == string_match:
                        print(f"Replacing {string_match} in {s}")
                        s = s.replace(string_match, "", 1)
                    break
        print(s)
        if len(s) > 1:
            return False
        return True


    def isMatch(self, s: str, p: str) -> bool:
        if s == p: return True
        if not "." in p and not "*" in p:
            return False
        return self.__test_astrict(s, p)


s = "aa"
p = "a"
# expected False


# s = "aab"
# p = "c*a*b"
# # expected True
# s = "aa"
# p = "a*"
# expected true

# s = "mississippi"
# p = "mis*is*ip*."
# expected True

# s = "mississippi"
# p = "mis*is*p*."

# expected False
tests = [
    ["aa", "a", False],
    ["aab", "c*a*b", True],
    ["aa", "a*", True],
    ["mississippi", "mis*is*ip*.", True],
    ["mississippi", "mis*is*p*.", False],
]
for s, p, e in tests:
    print(f"Testing: {s},{p}")
    print(f"Result: {Solution().isMatch(s, p)} == {e}")
    print("\n")

