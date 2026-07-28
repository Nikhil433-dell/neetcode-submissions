class Solution:
    def characterReplacement(self, s: str, k: int):
        countMap = {}
        res = 0

        l = 0
        for r in range(len(s)):
            countMap[s[r]] = 1 + countMap.get(s[r], 0)

            while (r-l+1) - max(countMap.values()) > k:
                countMap[s[l]] -= 1
                l += 1

            res = max(res, r-l+1) # (r-l+1) is the length of the window

        return res

