class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Rmap = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in Rmap:
                if stack and stack[-1] == Rmap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return stack == []
        