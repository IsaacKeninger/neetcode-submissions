class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        max_f = 0
        wdw = {}
        for r in range(len(s)):
            wdw[s[r]] = 1 + wdw.get(s[r], 0) # add to window the new value
            max_f = max(max_f, wdw[s[r]]) # update max freq
            if (r - l + 1) - max_f > k: # if remainder of non repeating chars over k, shrink window
                wdw[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1) # update res
        return res







        