class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tok in tokens:
            if tok in "+-*/":
                r = stack.pop()
                l = stack.pop()

                if tok == "+":
                    stack.append(l+r)
                elif tok == "-":
                    stack.append(l-r)
                elif tok == "*":
                    stack.append(l*r)
                elif tok == "/":
                    stack.append(int(l/r))
            else:
                stack.append(int(tok))
        return stack[0]

        
                



