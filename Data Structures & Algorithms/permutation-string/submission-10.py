class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        goal = {}
        for c in s1:
            goal[c] = 1 + goal.get(c, 0)
        
        wdw = {}
        for i in range(len(s1)):
            wdw[s2[i]] = 1 + wdw.get(s2[i], 0)
        
        if wdw == goal:
            return True

        l = 0
        for r in range(len(s1),len(s2)):

            wdw[s2[r]] = 1 + wdw.get(s2[r], 0)

            if wdw[s2[l]] == 1:
                del wdw[s2[l]]
            else:
                wdw[s2[l]] -= 1
            l += 1
            if wdw == goal:
                return True
        
        return wdw == goal