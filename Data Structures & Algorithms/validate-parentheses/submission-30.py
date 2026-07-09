class Solution:
    def isValid(self, s: str) -> bool:
        r_map = {')':'(', ']':'[', '}':'{'}
        stack = []
        for c in s:
            if c in r_map:
                if stack and r_map[c] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(c)
        return stack == []
        