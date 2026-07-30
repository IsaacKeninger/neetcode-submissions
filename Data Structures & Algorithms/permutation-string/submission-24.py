class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        cnt1 = {}
        for c in s1:
            cnt1[c] = cnt1.get(c, 0) + 1

        cnt2 = {}
        l = 0
        for r in range(len(s2)):
            cnt2[s2[r]] = 1 + cnt2.get(s2[r], 0)

            if r - l + 1 > len(s1):
                cnt2[s2[l]] -= 1
                if cnt2[s2[l]] == 0:
                    del cnt2[s2[l]]
                l += 1

            if cnt1 == cnt2:
                return True

        return False
        