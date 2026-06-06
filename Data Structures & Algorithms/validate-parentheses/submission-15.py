class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rMap = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in rMap:
                if stack and stack[-1] == rMap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return stack == []