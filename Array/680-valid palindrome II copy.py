from copy import deepcopy

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one = s[left:right]
                two = s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left += 1
            right -= 1
        return True

s= "abc"
s= "abca"
s="udvpezejpldkmmdrskmomkmobzvvlsetwrvnsygvuoepggxzjgcacystdvzqcmumjwdczmnyblvivhqyimwsmhftlthdjwbtrisbuluphpcwvcmgludyrwlnxrnpralrfpepjuwtpzpifcrbwxnaduzuxclorbhmfijfvkhgyvrtdofjnyzvrpcpdynbkxnqpaomzcldrtgfltwelrjmbjdugsdubbhvnvuzntviblsvbpgdpfumzukftpptfkuzmufpdgpbvslbivtnzuvnvhbbudsgudjbmjrlewtlfgtrdlczmoapqnxkbnydpcprvzynjfodtrvyghkvfjifmhbrolcxuzudanxwbrcfipzptwujpepfrlarpnrxnlwrydulgmcvwcphpulubsirtbwjdhtltfhmswmiyqhvivlbynmzdcdwjmumcqzvdtsycacgjzxggpeouvgysnvrwteslvvzbomkmomksrdmmkdlpjezepvdu"

print(
  Solution().validPalindrome(s)
)
