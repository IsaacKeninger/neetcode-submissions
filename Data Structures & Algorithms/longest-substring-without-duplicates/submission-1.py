class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        best = 0
        l = 0
        char_idx = {} # val : index

        for r in range(len(s)):
            if s[r] in char_idx and char_idx[s[r]] >= l:
                l = char_idx[s[r]] + 1
            char_idx[s[r]] = r
            best = max(best, r-l+1)
        return best
            


        


        