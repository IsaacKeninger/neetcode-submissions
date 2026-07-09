class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        s1Ct = {}
        for c in s1:
            s1Ct[c] = s1Ct.get(c, 0) + 1
        
        l = 0
        s2Ct = {}
        for r in range(len(s2)):
            s2Ct[s2[r]] = 1 + s2Ct.get(s2[r], 0)

            if (r - l + 1) > len(s1):
                s2Ct[s2[l]] -= 1
                if s2Ct[s2[l]] == 0:
                    del s2Ct[s2[l]]
                l += 1
            if s2Ct == s1Ct:
                return True
        
        return False
        