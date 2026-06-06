class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rmap = {")":'(', ']':'[', '}':'{'}

        for c in s:
            if stack and c in rmap:
                if stack[-1] == rmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return stack == []
                
