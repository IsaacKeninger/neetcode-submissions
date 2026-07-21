class Solution:
    def isValid(self, s: str) -> bool:
        rmap = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            if c in rmap:
                if stack and stack[-1] == rmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return stack == []