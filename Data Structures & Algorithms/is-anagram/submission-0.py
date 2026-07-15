class Solution:
    def isAnagram(self, s: str, t: str):

        if sorted(s) == sorted(t): 
            return True
        return False