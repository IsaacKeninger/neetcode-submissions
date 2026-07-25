class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        wdw = {}
        best = 0
        l = 0
        max_freq = 0
        for r in range(len(s)):
            wdw[s[r]] = 1 + wdw.get(s[r], 0)
            max_freq = max(max_freq, wdw[s[r]])
            if (r - l + 1) - max_freq > k:
                wdw[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best
