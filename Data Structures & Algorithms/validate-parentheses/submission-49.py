class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rmap = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in rmap:
                if stack and stack[-1] == rmap[c]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(c)
        return stack == []