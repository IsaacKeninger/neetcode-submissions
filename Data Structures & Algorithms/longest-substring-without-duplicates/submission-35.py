class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        best = 0 
        cset = set()
        for r in range(len(s)):
            while s[r] in cset:
                cset.remove(s[l])
                l += 1
            cset.add(s[r])
            best = max(best, r - l + 1)
        return best

        