class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Rmap = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c in Rmap:
                if stack and Rmap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return stack == []