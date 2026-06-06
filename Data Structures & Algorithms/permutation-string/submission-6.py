class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        goal = {}
        for i in range(len(s1)):
            goal[s1[i]] = 1 + goal.get(s1[i], 0)
        window = {}
        for i in range(len(s1)):
            window[s2[i]] = 1 + window.get(s2[i], 0)

        if goal == window:
            return True
        
        l = 0        
        for r in range(len(s1), len(s2)):
            window[s2[r]] = 1 + window.get(s2[r], 0)

            if window[s2[l]] == 1:
                del window[s2[l]]
            else:
                window[s2[l]] -= 1
            l += 1
            if goal == window:
                return True

        return goal == window
        