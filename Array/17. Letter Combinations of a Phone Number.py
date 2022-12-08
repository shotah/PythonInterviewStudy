# class Solution:
#     def letterCombinations(self, digits):
#         dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", '8':"tuv", '9':"wxyz"}
#         cmb = [''] if digits else []
#         for d in digits:
#             cmb = [p + q for q in dict[d] for p in cmb]
#         return cmb

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", '8':"tuv", '9':"wxyz"}
        cmb = [''] if digits else []
        for d in digits:
            for c in cmb:
                for l in dict[d]:
                    cmb.extend(c + l)
        return cmb
 

digits = "23"
# digits = "2"
s = Solution().letterCombinations(digits=digits)
print(
    s
)

