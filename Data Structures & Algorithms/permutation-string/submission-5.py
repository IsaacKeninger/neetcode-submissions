class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False

        l, r = 0, len(s1) - 1
        s1_count = {}
        s2_count = {}

        for i in range(len(s1)):
            s1_count[s1[i]] = 1 + s1_count.get(s1[i], 0)
            s2_count[s2[i]] = 1 + s2_count.get(s2[i], 0)
        
        for r in range(len(s1), len(s2)):
            if s1_count == s2_count:
                return True
            if s2_count[s2[l]] > 1:
                s2_count[s2[l]] -= 1
            else:
                del s2_count[s2[l]]
            l += 1
            s2_count[s2[r]] = 1 + s2_count.get(s2[r], 0)
        
        return s1_count == s2_count