class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1map = {}
        for c in s1:
            s1map[c] = 1 + s1map.get(c, 0)
        
        s2map = {}
        l = 0
        for r in range(len(s2)):
            s2map[s2[r]] = 1 + s2map.get(s2[r], 0)

            if (r - l + 1) > len(s1):
                s2map[s2[l]] -= 1
                if s2map[s2[l]] == 0:
                    del s2map[s2[l]]
                l += 1
            
            if s1map == s2map:
                return True
        
        return False