class Solution:
    def isValid(self, s: str) -> bool:
        Rmap = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            if c in Rmap: # if its closing
                if stack and Rmap[c] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False
            else:
                stack.append(c)
        
        return stack == []
            

        