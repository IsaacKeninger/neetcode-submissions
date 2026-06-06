class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        window = {}
        best = 0

        for r in range(len(s)):

            if s[r] not in window:
                window[s[r]] = 0

            window[s[r]] += 1

            while window[s[r]] > 1:
                # shrink window cause theres dupes
                window[s[l]] -= 1
                l += 1
            best = max(best, r-l+1)
        return best


        