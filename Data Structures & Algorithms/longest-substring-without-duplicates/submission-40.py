class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        longest = 0
        numset = set()
        for r in range(len(s)):
            while s[r] in numset:
                numset.remove(s[l])
                l += 1
            numset.add(s[r])
            longest = max(longest, r - l + 1)
        return longest



            