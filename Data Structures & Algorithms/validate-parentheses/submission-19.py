class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rmap = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c in rmap:
                if stack and rmap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return stack == []
        