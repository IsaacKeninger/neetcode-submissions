class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # edge cases
        if len(s) == 0:
            return 0 
        if len(s) == 1:
            return 1


        # [z,x,y,z,x,y,z] O(n)

        char_set = set()
        l = 0
        best = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            best = max(best, r - l + 1)

        return best

        