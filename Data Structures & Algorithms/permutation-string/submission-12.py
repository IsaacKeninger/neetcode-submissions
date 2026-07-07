class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
            
        s1_count = {}
        for c in s1:
            s1_count[c] = 1 + s1_count.get(c, 0)
            
        l = 0
        s2_count = {}
        
        for r in range(len(s2)):
            # Add new character to window
            s2_count[s2[r]] = 1 + s2_count.get(s2[r], 0)
            
            # Shrink window if it is larger than s1
            if (r - l + 1) > len(s1):
                s2_count[s2[l]] -= 1
                if s2_count[s2[l]] == 0:
                    s2_count.pop(s2[l])
                l += 1
                
            if s2_count == s1_count:
                return True
                
        return False
