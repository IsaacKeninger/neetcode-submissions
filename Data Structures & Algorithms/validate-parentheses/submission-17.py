class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        r_map = {')':'(', ']':'[','}':'{'}

        for c in s:
            if c in r_map:
                if stack and r_map[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return stack == []