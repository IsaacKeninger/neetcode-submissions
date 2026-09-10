class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        numset = set()
        best = 0
        l = 0
        for r in range(len(s)):
            while s[r] in numset:
                numset.remove(s[l])
                l += 1
            else:
                numset.add(s[r])
            best = max(best, r - l + 1)
        return best





            