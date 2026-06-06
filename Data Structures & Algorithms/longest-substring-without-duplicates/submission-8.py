class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        res = 0
        curr = 0
        window = {}


        for r in range(len(s)):

            if s[r] not in window:
                window[s[r]] = 0
            window[s[r]] += 1

            while window[s[r]] > 1: # its a dupe
                # shrink window
                window[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
        return res


        