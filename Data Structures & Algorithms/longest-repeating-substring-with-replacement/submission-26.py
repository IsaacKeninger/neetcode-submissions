class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        l = 0
        best = 0
        max_freq = 0

        for r in range(len(s)):
            cnt[s[r]] = 1 + cnt.get(s[r], 0)
            max_freq = max(cnt[s[r]], max_freq)
        
            if (r - l + 1) - max_freq > k:
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0:
                    del cnt[s[l]]
                l += 1
            
            best = max(best, r - l + 1)
        
        return best
        