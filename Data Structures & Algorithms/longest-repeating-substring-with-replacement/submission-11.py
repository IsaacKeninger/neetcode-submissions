class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = res = 0
        hm = {}
        maxF = 0

        for r in range(len(s)):
            hm[s[r]] = 1 + hm.get(s[r], 0)
            maxF = max(maxF, hm[s[r]])

            if (r - l + 1) - maxF > k:
                hm[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res