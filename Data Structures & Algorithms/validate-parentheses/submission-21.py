class Solution:
    def isValid(self, s: str) -> bool:
        # Maps closing brackets to their matching opening brackets
        rMap = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for c in s:
            # If the character is a closing bracket
            if c in rMap:
                # Pop the top of the stack if it exists, otherwise use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the popped opening bracket doesn't match the current closing one
                if rMap[c] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(c)
                
        # If the stack is empty, all brackets were matched perfectly
        return not stack
