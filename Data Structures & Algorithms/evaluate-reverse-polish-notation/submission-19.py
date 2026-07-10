class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for tok in tokens:
            if tok == '+':
                stk.append(stk.pop() + stk.pop())
            elif tok == '-':
                a,b = stk.pop(), stk.pop()
                stk.append(b-a)
            elif tok == '*':
                stk.append(stk.pop() * stk.pop())
            elif tok == '/':
                a,b = stk.pop(), stk.pop()
                stk.append(int(float(b) / a))
            else:
                stk.append(int(tok))
        return stk[0]