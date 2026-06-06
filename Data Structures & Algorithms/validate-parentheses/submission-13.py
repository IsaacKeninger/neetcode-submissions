class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rMap = {')':'(', ']':'[', '}': '{'}

        for c in s:
            if c in rMap:
                if stack and stack[-1] == rMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return stack == []