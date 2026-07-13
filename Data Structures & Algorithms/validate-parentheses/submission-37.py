class Solution:
    def isValid(self, s: str) -> bool:
        rmap = {')':'(', ']':'[', '}':'{'}
        stack = []
        for c in s:
            if c in rmap:
                if stack and rmap[c] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(c)
        return stack == []