class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given: s(str), t(str)
        Doing: Checking if t is an anagram of s
        Returning: True if yes, False if no
        """
        # lower bound is O(n) + O(n) = O(n).

        """
        Naive Solution:
            for each letter in S:
                for each letter in t:
                    if letter_s == letter_t:
                        shared += letter_s
            
            if shared == S:
                return True
            return False
        """

        if len(s) != len(t):
            return False

        sMap, tMap = {}, {}

        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            tMap[t[i]] = 1 + tMap.get(t[i], 0)
        
        if sMap == tMap:
            return True
        
        return False