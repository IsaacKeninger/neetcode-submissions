class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        stack = []

        for c in s: # all chars in string
            if stack:
                if stack[-1] == "(" and c == ")":
                    stack.pop()
                    continue
                elif stack[-1] == "[" and c == "]":
                    stack.pop()
                    continue
                elif stack[-1] == "{" and c == "}":
                    stack.pop()
                    continue
            if c in (")", "]", "}"): return False
            stack.append(c)
        return stack == []
