class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for tok in tokens:
            if tok in "+-*/":
                r = stk.pop()
                l = stk.pop()

                if tok == "+":
                    stk.append(l + r)
                elif tok == "-":
                    stk.append(l - r)
                elif tok == "*":
                    stk.append(l * r)
                elif tok == "/":
                    stk.append(int(l / r))
            else:
                stk.append(int(tok))
        return stk[0]