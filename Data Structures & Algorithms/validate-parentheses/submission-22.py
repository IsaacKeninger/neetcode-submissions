class Solution:
    def isValid(self, s: str) -> bool:
        # Maps closing brackets to their matching opening brackets
        rMap = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for c in s:
            if c in rMap:
                if not stack or stack.pop() != rMap[c]:
                    return False
            else:
                stack.append(c)
        return not stack