class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l,r = 0,0
        curr_chars = set()
        while r < len(s):
            while s[r] in curr_chars:
                curr_chars.remove(s[l])
                l += 1
            curr_chars.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1

        return longest