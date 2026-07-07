class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False
            
        # Make Counter for s1 to compare with
        s1_wdw = {}
        for c in s1:
            s1_wdw[c] = 1 + s1_wdw.get(c, 0)

        l = 0
        s2_wdw = {}
        for r in range(len(s2)):
            s2_wdw[s2[r]] = 1 + s2_wdw.get(s2[r], 0) # add to wdw

            if (r - l + 1) > len(s1): # if len of wdw is greater, must shrink
                s2_wdw[s2[l]] -= 1
                if s2_wdw[s2[l]] == 0:
                    s2_wdw.pop(s2[l])
                l += 1
            
            if s2_wdw == s1_wdw:
                return True

        return False


        



        