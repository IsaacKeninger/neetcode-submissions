class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        res = 0
        fmax = 0
        hm = {}

        for r in range(len(s)):
            hm[s[r]] = 1 + hm.get(s[r], 0)
            fmax = max(fmax, hm[s[r]])

            if (r - l + 1) - fmax > k:
                hm[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res