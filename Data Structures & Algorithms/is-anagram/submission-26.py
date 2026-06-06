class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smp,tmp = {}, {}

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            smp[s[i]] = 1 + smp.get(s[i], 0)
            tmp[t[i]] = 1 + tmp.get(t[i], 0)

        if tmp != smp:
            return False
        return True

        