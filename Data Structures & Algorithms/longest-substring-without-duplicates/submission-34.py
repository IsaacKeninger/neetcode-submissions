class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        best = 0
        count = set()
        
        for r in range(len(s)):
            while s[r] in count:
                count.remove(s[l])
                l += 1
            count.add(s[r])
            best = max(best, r - l + 1)
        
        return best


        