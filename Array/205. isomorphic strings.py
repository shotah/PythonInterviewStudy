class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_unique_char_length = len(set(s))
        t_unique_char_length = len(set(t))
        mapped_length_of_s_and_t = len(set(zip(s,t)))
        return s_unique_char_length == mapped_length_of_s_and_t == t_unique_char_length

s = "egg"
t = "add"
print(Solution().isIsomorphic(s,t))
