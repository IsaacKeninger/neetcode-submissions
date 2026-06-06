class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                # Pop operands in reverse order
                right = stack.pop()
                left = stack.pop()
                
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                elif token == '/':
                    # Use int(a/b) to truncate toward zero
                    stack.append(int(left / right))
            else:
                # Token is a number, push to stack
                stack.append(int(token))
        
        # The final result is the only item left
        return stack[0]
