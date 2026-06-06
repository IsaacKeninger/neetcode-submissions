class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #edge cases
        if len(s) == 0:
            return 0 
        if len(s) == 1:
            return 1 

        best = 0
        l = 0
        char_set = set()
        
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            best = max(r - l + 1, best)
        return best
            
        