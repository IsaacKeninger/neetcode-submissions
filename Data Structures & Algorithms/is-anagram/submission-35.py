class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap, tmap = {}, {}

        if len(t) != len(s):
            return False
        
        for i in range(len(s)):
            tmap[t[i]] = 1 + tmap.get(t[i], 0)
            smap[s[i]] = 1 + smap.get(s[i], 0)
        
        return tmap == smap
        
