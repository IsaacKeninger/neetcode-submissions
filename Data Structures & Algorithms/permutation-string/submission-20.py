class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        wdw1, wdw2 = {}, {}

        if len(s1) > len(s2):
            return False

        for c in s1:
            wdw1[c] = 1 + wdw1.get(c, 0)
        
        l = 0
        for r in range(len(s2)):
            wdw2[s2[r]] = 1 + wdw2.get(s2[r], 0)

            while (r - l + 1) > len(s1):
                wdw2[s2[l]] -= 1
                if wdw2[s2[l]] == 0:
                    del wdw2[s2[l]]
                l += 1

            if wdw2 == wdw1:
                return True

        return False
        

        