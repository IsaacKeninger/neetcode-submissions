class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCnt, tCnt = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sCnt[s[i]] = 1 + sCnt.get(s[i], 0)
            tCnt[t[i]] = 1 + tCnt.get(t[i], 0)
        
        if sCnt == tCnt:
            return True
        return False