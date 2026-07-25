class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        best = 0
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            best = max(best, r - l + 1)
        return best
            
        