class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        res = 0
        charset = set()
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            else:
                res = max(res, r - l + 1)
            charset.add(s[r])
        return res

            