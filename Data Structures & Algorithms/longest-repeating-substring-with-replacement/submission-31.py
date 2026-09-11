class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        max_f = 0
        hm = {}
        
        l = 0
        for r in range(len(s)):
            hm[s[r]] = 1 + hm.get(s[r], 0)
            max_f = max(max_f, hm[s[r]])

            if (r - l + 1) - max_f > k:
                # shrink
                hm[s[l]] -= 1
                if hm[s[l]] == 0:
                    del hm[s[l]]
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest