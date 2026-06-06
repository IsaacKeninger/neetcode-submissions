class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # edge cases
        if len(s) == 0:
            return 0 
        if len(s) == 1:
            return 1


        # [z,x,y,z,x,y,z] O(n)

        hashset = set()
        best = 0
        l = 0

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            best = max(best, r - l + 1)

        return best



        