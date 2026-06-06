class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", ']': '[', '}': '{'}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]: # if match valid
                    stack.pop()
                else:
                    return False # parentheses dont match
            else:
                stack.append(c)
        
        return stack == []
        