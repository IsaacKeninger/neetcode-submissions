class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1Count = {}
        for c in s1:
            s1Count[c] = 1 + s1Count.get(c, 0)
        
        s2Count = {}
        l = 0
        for r in range(len(s2)):
            s2Count[s2[r]] = 1 + s2Count.get(s2[r], 0)
            if r - l + 1 > len(s1):
                s2Count[s2[l]] -= 1
                if s2Count[s2[l]] == 0:
                    del s2Count[s2[l]]
                l += 1
            if s2Count == s1Count:
                return True
        return False
        
        