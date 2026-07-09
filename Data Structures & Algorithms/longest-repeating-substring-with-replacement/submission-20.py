class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_f = 0
        res = 0
        l = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_f = max(max_f, count[s[r]])
            if ((r - l + 1) - max_f) > k:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    count.pop(s[l])
                l += 1
            res = max(res, r - l + 1)
        return res
        