class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_f = 0
        res = 0
        cnt = {}
        l = 0
        for r in range(len(s)):
            cnt[s[r]] = 1 + cnt.get(s[r], 0)
            max_f = max(max_f, cnt[s[r]])
            if (r - l + 1) - max_f > k:
                cnt[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
            
