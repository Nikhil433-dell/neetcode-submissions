class Solution:
    def lengthOfLongestSubstring(self, s: str):

        # using split maybe there is a better way to use chrs
        maxStr = 0
        window = set()
        l = 0

        for i in range(len(s)):

            while s[i] in window:
                window.remove(s[l])
                l += 1
            
            window.add(s[i])
            maxStr = max(maxStr, i-l+1)
           

        return maxStr
        