from copy import deepcopy

class Solution:
    def validPalindrome(self, s: str) -> bool:
      arr = list(s)
      for i, c in enumerate(s):
        copy_arr = deepcopy(arr)
        copy_arr.pop(i)
        if copy_arr == copy_arr[::-1]: return True
      return False

s= "abc"
s= "abca"
s="udvpezejpldkmmdrskmomkmobzvvlsetwrvnsygvuoepggxzjgcacystdvzqcmumjwdczmnyblvivhqyimwsmhftlthdjwbtrisbuluphpcwvcmgludyrwlnxrnpralrfpepjuwtpzpifcrbwxnaduzuxclorbhmfijfvkhgyvrtdofjnyzvrpcpdynbkxnqpaomzcldrtgfltwelrjmbjdugsdubbhvnvuzntviblsvbpgdpfumzukftpptfkuzmufpdgpbvslbivtnzuvnvhbbudsgudjbmjrlewtlfgtrdlczmoapqnxkbnydpcprvzynjfodtrvyghkvfjifmhbrolcxuzudanxwbrcfipzptwujpepfrlarpnrxnlwrydulgmcvwcphpulubsirtbwjdhtltfhmswmiyqhvivlbynmzdcdwjmumcqzvdtsycacgjzxggpeouvgysnvrwteslvvzbomkmomksrdmmkdlpjezepvdu"

print(
  Solution().validPalindrome(s)
)
