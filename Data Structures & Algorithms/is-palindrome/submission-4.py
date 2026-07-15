import string

class Solution:
    def isPalindrome(self, s: str):

        if s != None and len(s) <= 1000:

            newS = s.replace(" ", "").replace("?", "").replace(",", "").replace("!", "").replace("'", "").replace(".", "").replace(":", "").lower()
            reversedS = newS[::-1]

            if newS == reversedS:
                return True
            
        return False
        